from django.shortcuts import render, redirect
from .models import Expense, MonthlyIncome
from .forms import ExpenseForm, MonthlyIncomeForm, SignUpForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Home view showing total income, expenses, and savings
@login_required
def home(request):
    incomes = MonthlyIncome.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    total_income = sum(income.amount for income in incomes)
    total_expense = sum(exp.amount for exp in expenses)
    savings = total_income - total_expense
    over_budget = total_expense > total_income

    return render(request, 'expenses/home.html', {
        'savings': savings,
        'total_income': total_income,
        'total_expense': total_expense,
        'over_budget': over_budget
    })

# View for current month's savings calculation
@login_required
def savings_view(request):
    today = timezone.now().date()
    current_month = today.month
    current_year = today.year

    income_entry = MonthlyIncome.objects.filter(
        user=request.user,
        month__month=current_month,
        month__year=current_year
    ).first()

    income = income_entry.amount if income_entry else 0

    expenses = Expense.objects.filter(
        user=request.user,
        date__month=current_month,
        date__year=current_year
    )
    total_expenses = sum(exp.amount for exp in expenses)

    savings = income - total_expenses
    over_budget = savings < 0

    return render(request, 'expenses/savings.html', {
        'income': income,
        'total_expenses': total_expenses,
        'savings': savings,
        'over_budget': over_budget,
        'over_budget_amount': abs(savings),
    })

# View to list user's expense history
@login_required
def expense_history(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses/expense_history.html', {'expenses': expenses})

# View to add monthly income
@login_required
def add_income(request):
    if request.method == 'POST':
        form = MonthlyIncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('home')
    else:
        form = MonthlyIncomeForm()
    return render(request, 'expenses/add_income.html', {'form': form})

# View to add a new expense
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

# Signup view to create a new user
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'expenses/signup.html', {'form': form})

# Login view for existing users
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'expenses/login.html', {'form': form})
