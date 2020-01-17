from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),  # localhost:8000/sampleapp
    path('thanks/', views.added, name='added'),
    path('', views.customer_form,  name='customer_insert'),
    path('<int:id>/', views.customer_form, name='customer_update'),  # localhost:8000/sampleapp
    path('<int:id>/list', views.account_list,  name='account_list'),  # localhost:8000/sampleapp
    path('<int:id>/accounts', views.account_form,  name='add_account'),  # localhost:8000/sampleapp
    path('<int:id>/list/<int:account_id>/delete', views.account_delete, name='account_delete'),
    path('delete/<int:id>/', views.customer_delete, name='customer_delete'),
    path('list/', views.customer_list, name='customer_list') # localhost:8000/sampleapp/list
]