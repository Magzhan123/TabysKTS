from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'trydjango.views.about', name='about'),
    url(r'^login/$', 'trydjango.views.login', name='login'),
    url(r'^contact/$', 'trydjango.views.contact', name='contact'),
    url(r'^register/$', 'trydjango.views.register', name='register'),
    url(r'^checkout/$', 'trydjango.views.checkout', name='checkout'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)