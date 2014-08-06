from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^polls/', include('polls.urls')),
    url(r'^pos_app/', include('pos_app.urls')), # ADD THIS NEW TUPLE!

    #url(r'^about/', include('polls.urls')), # ADD THIS NEW TUPLE!

    url(r'^admin/', include(admin.site.urls)),
)
