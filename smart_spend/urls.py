
from django.contrib import admin
from django.urls import path , include
from expenses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses.urls')),
    path('', views.home, name='home'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),  
]

