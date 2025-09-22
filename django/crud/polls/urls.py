from django.urls import path, include
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:Questions_id>/', views.detail, name='detail'),
    path('<int:Questions_id>/results/', views.results, name='results'),
    path('<int:Questions_id>/v/', views.vote, name='vote')

]