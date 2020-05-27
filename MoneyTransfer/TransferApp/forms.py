from django import forms
from TransferApp.models import Customer, Transaction
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('phone',)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('receiver', 'amount', 'reason')
