from PIL import Image
import uuid
from django.conf import settings
import os


def mkdir(path):
    if path in ('', '/'):
        return
    if not os.path.exists(os.path.dirname(path)):
        mkdir(os.path.dirname(path))
    if not os.path.exists(path):
        os.mkdir(path)


def save_img(img, prefix, filename):
    filename_path = os.path.join(
        'upload',
        prefix,
        filename
    )
    path = os.path.join(
        settings.MEDIA_ROOT,
        filename_path)
    mkdir(os.path.dirname(path))
    with open(path, 'wb') as fd:
        img.save(fd, 'JPEG', quality=100)
    return filename_path


def resize_image(img, width, height):
    W, H = img.size
    w, h = W, H
    if W > width:
        w, h = width, H * width / W
    elif H > height:
        w, h = W * height / H, height
    return img.resize((w, h), Image.ANTIALIAS)


def get_crop_offset(cur_width, cur_height, W, H):
    """Calculates optimal crop offsets for an image with size
    ``cur_width`` and ``cur_height`` to have the same width/height ratio
    as an image with ``W`` width and ``H`` height.

    Returns four integers - offsets from left, top, right and bottom
    sides in pixels."""
    ratio = float(W) / H
    cur_ratio = float(cur_width) / cur_height
    left, top, right, bottom = (0, 0, 0, 0)
    if cur_ratio <= ratio:
        new_height = int(cur_width / ratio)
        gc = int(cur_height - new_height)
        top = gc / 2
        bottom = (gc / 2) + (gc % 2)
    else:
        new_width = int(cur_height * ratio)
        gc = int(cur_width - new_width)
        left = gc / 2
        right = (gc / 2) + (gc % 2)
    return (left, top, right, bottom)


def center_crop(img, W, H):
    """Crops an image ``img`` if required to comply given ratio ``W/H``"""
    if img is None:
        return
    off = get_crop_offset(img.size[0], img.size[1], W, H)
    if off != (0, 0, 0, 0):
        img = img.crop((
            off[0], off[1], img.size[0] - off[2],
            img.size[1] - off[3]))
    if img.size != (W, H):
        img = img.resize((W, H))
    return img


def thumb_image(prefix, id, f, size):
    main_img = Image.open(f)
    if main_img.mode == "CMYK":
        main_img = main_img.convert("RGB")
    filename = id + ".jpg"
    image = center_crop(main_img, *size)
    return save_img(
        image, prefix, filename)
