from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mypolls.views.home', name='home'),

    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'),
        name='contact'),

    url(r'^about/$', TemplateView.as_view(template_name='about.html'),
        name='about'),

    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += staticfiles_urlpatterns()