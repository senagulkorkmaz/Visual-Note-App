from folder import views
from django.urls import path
#

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='folder-create'),
    path('list/', views.ListView.as_view(), name='folder-list'),
    path('update/<str:pk>/', views.UpdateView.as_view(), name='folder-update'),
    path('delete/<str:pk>/', views.DeleteView.as_view(), name='folder-delete'),
]
