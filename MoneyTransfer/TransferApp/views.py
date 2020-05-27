from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from TransferApp.models import Customer, Transaction
from TransferApp.forms import UserForm, CustomerForm, TransactionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q


@login_required(login_url='/sign-in/')
def create_transaction(request):
    form = TransactionForm

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            sender = request.user.customer
            transaction = form.save(commit=False)
            transaction.sender = sender
            receiver = transaction.receiver
            receiver.balance += transaction.amount
            receiver.save()
            transaction.save()
            sender.balance -= transaction.amount
            sender.save()
            return redirect(account_report)

    return render(request, 'create_transaction.html', {
        "form": form
    })

@login_required(login_url='/sign-in/')
def transfer_home(request):
    return redirect(account_report)

@login_required(login_url='/sign-in/')
def account_report(request):
    transactions = Transaction.objects.filter(Q(sender=request.user.customer) | Q(receiver=request.user.customer))
    return render(request, 'report.html', {"transactions": transactions})

def customer_sign_up(request):
    user_form = UserForm()
    customer_form = CustomerForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_customer = customer_form.save(commit=False)
            new_customer.user = new_user
            new_customer.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(transfer_home)

    return render(request, 'sign_up.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })

