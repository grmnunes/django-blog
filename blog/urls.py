from django.urls import path
from django.views.generic.detail import DetailView
from . import views
import blog

app_name = blog

urlpatterns = [
  path('', views.PostListView.as_view(), name='list'),
  path('<slug:slug>/', views.views.PostDetailView.as_view(), name='detail')
]