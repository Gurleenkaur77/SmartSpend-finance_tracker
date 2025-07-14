from django import forms
from .models import Expense, MonthlyIncome
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Form to add monthly income
class MonthlyIncomeForm(forms.ModelForm):
    class Meta:
        model = MonthlyIncome
        fields = ['month', 'amount']
        widgets = {
            'month': forms.DateInput(attrs={'type': 'date'})  # Uses a calendar input
        }

# Form to add a new expense
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # Uses a calendar input
        }

# Form to register a new user
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
