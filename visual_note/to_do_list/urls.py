from to_do_list import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='yapılacaklar-create'),
    path('list/', views.ListView.as_view(), name='yapılacaklar-list'),
    path('update/<str:pk>/', views.UpdateView.as_view(),
         name='yapılacaklar-update'),
    path('delete/<str:pk>/', views.DeleteView.as_view(),
         name='yapılacaklar-delete'),
]
