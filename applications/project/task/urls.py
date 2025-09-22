from django.urls import path
from .views import OrderCreateView, OrderListView, OrderCrudView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('list/', OrderListView.as_view(), name='list'),
    path('edit/<int:pk>/', OrderCrudView.as_view(), name='edit'),
]
    
