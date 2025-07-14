from django.urls import path
from . import views

urlpatterns = [
     path('add-expense/', views.add_expense, name='add_expense'),
    path('add-income/', views.add_income, name='add_income'),
    path('savings/', views.savings_view, name='savings'),
    path('expenses/history/', views.expense_history, name='expense_history'),
    path('signup/', views.signup_view, name='signup'),
path('login/', views.login_view, name='login'),

    path('', views.home, name='home'),]
