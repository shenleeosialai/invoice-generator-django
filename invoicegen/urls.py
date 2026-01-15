from django.urls import path
from . import views

app_name = 'invoicegen'

urlpatterns = [
    path('<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('', views.invoice_list, name='invoice_list')
]