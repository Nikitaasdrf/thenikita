from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
      path('', views.homePage, name='homePage'),
      path('blog/', views.blog, name='blog'),
      path('useres/', views.useres, name='useres'),
      path('video/', views.video, name='video'),
      path('feedback/', views.feedback, name='feedback'),
      path('contacts/', views.contacts, name='contacts'),
      path('about/', views.about, name='about'),
      path('addarticle/', views.addarticle, name='addarticle'),
      path('blogcontent/<int:pk>', views.blogcontent, name='blogcontent'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)