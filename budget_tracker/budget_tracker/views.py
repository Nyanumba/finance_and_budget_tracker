from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from transactions.models import Transaction, Category
from django.db.models import Sum
import csv
from django.http import HttpResponse

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'type', 'category', 'date', 'description']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get user from view
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)  # Filter categories by user

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    summary = {
        'total_income': transactions.filter(type='Income').aggregate(Sum('amount'))['amount__sum'] or 0,
        'total_expenses': transactions.filter(type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0,
    }
    summary['balance'] = summary['total_income'] - summary['total_expenses']
    transactions_data = [
        {'id': t.id, 'amount': str(t.amount), 'type': t.type, 'category': {'name': t.category.name}, 'date': str(t.date), 'description': t.description}
        for t in transactions
    ]
    return render(request, 'dashboard.html', {'summary': summary, 'transactions': transactions_data})

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction_list.html', {'transactions': transactions})

@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, user=request.user)  # Pass user to form
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(user=request.user)  # Pass user to form
    return render(request, 'transaction_form.html', {'form': form})

@login_required
def transaction_edit(request, pk):
    transaction = Transaction.objects.filter(user=request.user, pk=pk).first()
    if not transaction:
        return redirect('transaction_list')
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction, user=request.user)  # Pass user to form
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction, user=request.user)  # Pass user to form
    return render(request, 'transaction_form.html', {'form': form})

@login_required
def transaction_delete(request, pk):
    transaction = Transaction.objects.filter(user=request.user, pk=pk).first()
    if request.method == 'POST' and transaction:
        transaction.delete()
    return redirect('transaction_list')

@login_required
def transaction_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Date', 'Amount', 'Type', 'Category', 'Description'])
    transactions = Transaction.objects.filter(user=request.user)
    for t in transactions:
        writer.writerow([t.id, t.date, t.amount, t.type, t.category.name, t.description])
    return response

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name, user=request.user)
            return redirect('category_list')
    return render(request, 'category_form.html')