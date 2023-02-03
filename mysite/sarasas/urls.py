from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mytasks/', views.UserTasksListView.as_view(), name="mytasks"),
    path('mytasks/new/', views.UserTaskCreateView.as_view(), name='newtask'),
    path('mytasks/<int:pk>/update', views.UserTaskUpdateView.as_view(), name='updatetask'),
    path('mytasks/<int:pk>/delete', views.UserTaskDeleteView.as_view(), name='deletetask'),
]