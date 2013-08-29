from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from rbp import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('promotions.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
