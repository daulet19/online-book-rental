from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zhanry/', views.zhanry, name='zhanry'),
    path('onas/', views.onas, name='onas'),
    path('avtory/', views.avtory, name='avtory'),
    path('', views.BookListView.as_view(), name='books'),
]
