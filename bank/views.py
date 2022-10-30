from django.shortcuts import render,HttpResponseRedirect
import decimal
from django.db.models import F
from django.db import transaction
from django.template.response import TemplateResponse
from .models import *
from .forms import *


# Create your views here.

#?DemoException
class DemoException(Exception):
    print('DemoException WORKING...')
    pass

#!process_payment
def process_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST or None)
        if form.is_valid():
            x = form.cleaned_data.get('payor')
            y = form.cleaned_data.get('payee')
            z = decimal.Decimal(form.cleaned_data.get('amount'))
            
            payor = Customer.objects.select_for_update().get(name=x)#~odeyen
            payee = Customer.objects.select_for_update().get(name=y)#~alan
            #Essentially, an atomic transaction ensures that any commit you make finishes the entire operation successfully. Or, in cases of a lost connection in the middle of an operation, the database is rolled back to its state prior to the commit being initiated
            
        with transaction.atomic():
            payor.balance -= z
            payor.save()
            
            payee.balance += z
            payee.save()
            
            #!Or
            # Customer.objects.filter(name=x).update(balance=F('balance')-z)
            # Customer.objects.filter(name=y).update(balance=F('balance')+z)
            
            return HttpResponseRedirect('/')
    else:
        form = PaymentForm()
    
    #if return error request
    #raise DemoException('Error coming from view,when request to this view') => this DemoException class writing for,test process_exception function,if not Exception or Error not working process_exception middleware
    
    return TemplateResponse(request,'index.html',{'form':form})#TemplateResponse is useful for modifying a response before it is rendered, which cannot be done with a traditional static HttpResponse object.
    
    
#A TemplateResponse() => delays the rendering of the template until after the view is finished
#The render() => shortcut immediately renders the template and returns a HttpResponse.