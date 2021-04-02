from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from blog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('save-session-data/', views.save_session_data, name='save_session_data'),
    path('access-session-data/', views.access_session_data, name='access_session_data'),
    path('delete-session-data/', views.delete_session_data, name='delete_session_data'),
    path('test-delete/', views.test_delete, name='test_delete'),
    path('test-session/', views.test_session, name='test_session'),
    path('track_user/', views.track_user, name='track_user'),
    path('stop-tracking/', views.stop_tracking, name='stop_tracking'),
    path('cookie/', views.test_cookie, name='cookie'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('cadmin', include('django.contrib.auth.urls')),
    #path('', views.index, name='blog_index'),
    path('',include('blog.urls')),
    path('cadmin/',include('cadmin.urls')),

    # url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    # url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    # url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
