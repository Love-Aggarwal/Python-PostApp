from django.conf.urls import  include,url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('activate/account/', views.activate_account, name='activate'),
    #path('password-change/', views.password_change,name='passwod_Change'),
    #path('password-change-done/',auth_views.password_change, {'template_name': 'cadmin/password_change_done.html'},name='password_change_done'),
    #path('password-change/',auth_views.password_change, {'template_name': 'cadmin/password_change.html','post_change_redirect': 'password_change_done'},name='password_change'),
    path('register/', views.register, name='register'),
    path('category/', views.category_list, name='category_list'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('category/add/$', views.category_add, name='category_add'),
    path('tag/', views.tag_list, name='tag_list'),
    url(r'^category/update/(?P<pk>[\d]+)/$', views.category_update, name='category_update'),
    url(r'^category/delete/(?P<pk>[\d]+)/$', views.category_delete, name='category_delete'),
    url(r'^post/delete/(?P<pk>[\d]+)/$', views.post_delete, name='post_delete'),
    path('accounts/logout/', auth_views.LogoutView,{'template_name': 'blog/logout.html'}, name='logout'),
    path('post/add/', views.post_add, name='post_add'),
    path('tag/add/', views.tag_add, name='tag_add'),
    
    path('account-info/', views.account_info, name='account_info'),
    url(r'^tag/delete/(?P<pk>[\d]+)/$', views.tag_delete, name='tag_delete'),
    url(r'^tag/update/(?P<pk>[\d]+)/$', views.tag_update, name='tag_update'), 
    url(r'^post/update/(?P<pk>[\d]+)/$', views.post_update, name='post_update'),
]