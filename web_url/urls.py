from django.conf.urls import include, url
from django.contrib import admin
from web_url import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'web_url.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.url, name="index"),
    url(r'^urls/', include('urls_short.urls', namespace="urls_short")),
    url(r'^admin/', include(admin.site.urls)),
  #  url(r'^$', views.urls_list, name="index"),
 #   url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
]
