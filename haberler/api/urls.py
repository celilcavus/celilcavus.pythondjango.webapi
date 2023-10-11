from django.urls import path
from haberler.api import views as api_views

urlpatterns = [
    path('get',api_views.Get,name='makale'),
    path('get/<int:pk>',api_views.GetDetail,name='makale-detay'),
    path('post',api_views.Post,name='makale-ekle'), 
    path('delete/<int:pk>',api_views.Delete,name='makale-sil'),
    path('update/<int:pk>',api_views.Update,name='makale-update')
]
