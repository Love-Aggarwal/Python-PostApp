from django.conf.urls import url
from django.urls import path
from .views import(today_is)
from django.contrib.flatpages import views as flat_views
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap


sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    # url(r'^(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    # url(r'^(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    #url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    path('login/', views.login, name='blog_login'),
    path('about/', flat_views.flatpage, {'url': '/about/'}, name='about'),
    path('sitemap.xml/', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    path('eula/', flat_views.flatpage, {'url': '/eula/'}, name='eula'),
    path('logout/', views.logout, name='blog_logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('',views.post_list, name='post_list'),
    path('lousy-login/', views.lousy_login, name='lousy_login'),
    path('lousy-secret/', views.lousy_secret, name='lousy_secret'),
    path('lousy-logout/', views.lousy_logout, name='lousy_logout'),
    path('feedback/', views.feedback, name='feedback'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/(?P<post_slug>[\w\d-]+)$', views.post_detail, name='post_detail'),
    
   
]
