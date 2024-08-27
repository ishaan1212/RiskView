from django.urls import path
from RiskView import views

app_name = 'RiskView'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('kri/', views.add_kri, name='kri'),
    path('perfreport/', views.add_metric, name='perfreport'),
    path('portfolio/', views.add_portfolio, name='portfolio')
]