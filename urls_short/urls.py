from django.conf.urls import url

from urls_short import views

urlpatterns = [
    url(r'^$', views.urls_list, name='index'),
    #url(r'^add/$', views.URLCreateView.as_view(), name='add'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
    url(r'^(?P<pk>\d+)/', views.detail, name='detail'),
    url(r'^/(?P<pk>\d+)/$', views.urls_list, name='index'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^share/(?P<pk>\d+)/$', views.share, name='share'),
    ]