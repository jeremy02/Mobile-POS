from django.conf.urls import patterns, include, url

# At the top of your urls.py file, add the following line:
from django.conf import settings

from django.contrib import admin
admin.autodiscover()
#import pos_app.views as entry_point

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^polls/', include('polls.urls')),

    #url(r'^/pos_app', include('pos_app.urls')), # ADD THIS NEW TUPLE!
    url(r'^pos_app/', include('pos_app.urls')), # ADD THIS NEW TUPLE!
    #url(r'^', ), # ADD THIS NEW TUPLE!
    #url(r'^', entry_point.register),

    #url(r'^about/', include('polls.urls')), # ADD THIS NEW TUPLE!

    url(r'^admin/', include(admin.site.urls)),
)

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
