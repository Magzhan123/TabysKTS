import os

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^django-admin/', include(admin.site.urls)),
    # url(r'^admin/', include(wagtailadmin_urls)),
    # url(r'^search/', include(wagtailsearch_urls)),
    # url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^test/$', 'core.views.test', name='test'),
    url(r'^about/$', 'core.views.about', name='about'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home_page'}, name='logout'),
    url(r'^contact/$', 'core.views.contact', name='contact'),
    url(r'^register/$', 'core.views.register', name='register'),
    url(r'^checkout/$', 'core.views.checkout', name='checkout'),
    url(r'^avtivations/$', 'core.views.activations', name='activations'),
    url(r'^product/$', 'core.views.product', name='product'),
    url(r'^uslug/$', 'core.views.uslug', name='uslug'),
    url(r'^blogs/$', 'core.views.main', name='blogs'),
    url(r'^single/$', 'core.views.single', name='single'),
    url(r'^admin/$', 'core.views.admin_products', name='admin/index'),
    url(r'^switch/$', 'core.views.switch_lang', name='switch'),
    url(r'^admin/news$', 'core.views.admin_posts', name='admin/news'),
    url(r'^$', 'core.views.home_page', name='home_page'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'', include('social_auth.urls')),
    # url(r'', include(wagtail_urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
