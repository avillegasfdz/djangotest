from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    #path('', views.index, name='index'),  # localhost:8000/sampleapp
    path('thanks/', views.added, name='added'),
    path('<int:admin_id>/', views.customer_form,  name='customer_insert'),
    path('<int:admin_id>/customers/<int:id>/', views.customer_form, name='customer_update'),  # localhost:8000/sampleapp
    path('<int:admin_id>/customers/<int:id>/list', views.account_list,  name='account_list'),  # localhost:8000/sampleapp
    path('<int:admin_id>/customers/<int:id>/accounts', views.account_form,  name='add_account'),  # localhost:8000/sampleapp
    path('<int:admin_id>/customers/<int:id>/list/<int:account_id>/delete', views.account_delete, name='account_delete'),
    path('<int:admin_id>/customers/<int:id>/delete', views.customer_delete, name='customer_delete'),
    path('<int:admin_id>/list/', views.customer_list, name='customer_list'), # localhost:8000/sampleapp/list
]