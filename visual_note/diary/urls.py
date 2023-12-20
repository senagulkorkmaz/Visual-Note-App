from diary import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='gunluk-create'),
    path('list/', views.ListView.as_view(), name='gunluk-list'),
    path('update/<str:pk>/', views.UpdateView.as_view(), name='gunluk-update'),
    path('delete/<str:pk>/', views.DeleteView.as_view(), name='gunluk-delete'),
]
