from django.urls import path
from . import views 

app_name = 'tests'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('store/<int:pk>', views.StoreView.as_view(), name='store'),
    path('like/<int:pk>', views.like, name='like'),
]
