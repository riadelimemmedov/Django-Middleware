from django import forms

#!Payment
class PaymentForm(forms.Form):
    payor = forms.CharField(max_length=30)#odeyen
    payee = forms.CharField(max_length=30)#alan
    amount = forms.CharField(max_length=30)