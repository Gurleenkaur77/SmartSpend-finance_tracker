from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Rent', 'Rent'),
    ('Travel', 'Travel'),
    ('Shopping', 'Shopping'),
    ('Other', 'Other'),
]

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ⛔ Removed null=True
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"

class MonthlyIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ⛔ Removed null=True
    month = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.month.strftime('%B %Y')} - ₹{self.amount}"

    class Meta:
        unique_together = ('user', 'month')  # ✅ To allow per-user monthly income
