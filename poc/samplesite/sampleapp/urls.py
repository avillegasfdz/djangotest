from django.urls import path

from . import views

urlpatterns = [


    path('', views.index, name='index'),  # localhost:8000/sampleapp
    path('thanks/', views.added, name='added'),
    path('<int:id>/', views.customer_form,  name='customer_update'),  # localhost:8000/sampleapp
    path('delete/<int:id>/', views.customer_delete, name='customer_delete'),
    path('list/', views.customer_list, name='customer_list') # localhost:8000/sampleapp/list
]