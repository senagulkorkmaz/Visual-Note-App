from planner import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='planlayıcı-create'),
    path('list/', views.ListView.as_view(), name='planlayıcı-list'),
    path('update/<str:pk>/', views.UpdateView.as_view(), name='planlayıcı-update'),
    path('delete/<str:pk>/', views.DeleteView.as_view(), name='planlayıcı-delete'),
]
