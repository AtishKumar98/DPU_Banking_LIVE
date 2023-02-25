from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect
from .forms import Payment
from django.contrib import messages
from Account.models import UserBankAccount
from Transfer.models import TransferMoney
from django.db.models import F
import decimal
from django.db import transaction

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def process_payment(request):
  if request.method == 'POST':
    form = Payment(request.POST)
    status = None
    kk=None
    if form.is_valid():
      x = form.cleaned_data['payor']
      y = form.cleaned_data['payee']
      z = decimal.Decimal(form.cleaned_data['amount'])
      if UserBankAccount.objects.filter(account_no=x).exists() and UserBankAccount.objects.filter(account_no=x).exists():
        payor = UserBankAccount.objects.select_for_update().get(account_no=x)
        payee = UserBankAccount.objects.select_for_update().get(account_no=y)
      else:
        kk='Invalid Account'

        # print(kk, '$$$$$$$$$$$$')
        return redirect ('/')
        

    with transaction.atomic():
     
        if payor.balance >= z and payor.balance >=0:
          payor.balance -= z
          payee.balance += z
          status = "Paid"

        else:
          status = "Insufficent balance"
        # current_user = request.user.account.all()
        # status.save()
          payor.save()
          payee.save()
        

        # payor.save()
        # payee.save()
        report_balance = TransferMoney.objects.create(
            # name =  request.user,
            From_accno = payor,
            To_accno = payee,
            amount = z,
            status = status,
            transaction_balance = payor.balance
        )
        report_balance.save()
        try:
          if report_balance.status =='Paid':
            messages.success(request , "Amount Paid Successfully") 
          elif report_balance.status =='Insufficent balance':
            messages.error(request , "Insufficent Funds Check Your Balance")
          elif UserBankAccount.objects.filter(account_no=x).exists() and UserBankAccount.objects.filter(account_no=x).exists():
            kk='Invalid'
            print(kk, '$$$$$$$$$$$$')
            messages.error(request , "Oops Something Went Wrong Kindly Check Account Details ,Check Account number")
            print(messages)
            return redirect ('/')
        except:
          messages.error(request , "Oops Something Went Wrong Kindly Check Account Details ,Check Account number")
        return redirect ('/') 
      
      
      # customer.objects.filter(name=x).update(balance=F('balance') - z)
      # customer.objects.filter(name=y).update(balance=F('balance') + z)

      # return HttpResponseRedirect('/transfer/')
  else:
    form = Payment()
    status = ''
    kk=''
  return render(request, 'transfer.html' , {'form': form ,'kk':kk})




# def report(request,pk):
#   current_user_file = UserBankAccount.objects.filter(user = request.user)
#   transfer_report = TransferMoney.objects.get(pk=id)
#   print(transfer_report)
#   # transfer_report = TransferMoney.objects.get()
#   transfer_report1 = request.user.account.all()
#   context= {
#     'report':transfer_report,
#     'b':transfer_report1,
#     }
#   return render (request, 'report.html',context)