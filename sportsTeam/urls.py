from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sportsTeam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello-world/$', 'sportsApp.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)