from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import Payment
from Account.models import UserBankAccount
from Transfer.models import TransferMoney
import decimal
# from django.template import get_default_context




@login_required(login_url='/login/')
def process_payment(request):
    # print(get_default_context(request))
    Acc_no = UserBankAccount.objects.get(user_id=request.user.id)
    
    if request.method == 'POST':
        form = Payment(request.POST)
        status = None

        if form.is_valid():
            x = form.cleaned_data['payor']
            y = form.cleaned_data['payee']
            z = decimal.Decimal(form.cleaned_data['amount'])

            payor = UserBankAccount.objects.select_for_update().get(account_no=x)
            payee = UserBankAccount.objects.select_for_update().get(account_no=y)

            with transaction.atomic():
                try:
                    if payor.balance >= z and payor.balance >= 0:
                        payor.balance -= z
                        payee.balance += z
                        status = "Paid"
                    else:
                        status = "Insufficient balance"

                    payor.save()
                    payee.save()

                    report_balance = TransferMoney.objects.create(
                        From_accno=payor,
                        To_accno=payee,
                        amount=z,
                        status=status,
                        transaction_balance=payor.balance
                    )

                    report_balance.save()

                    if report_balance.status == 'Paid':
                        messages.success(request, f"Amount Paid Successfully ₹ {z} Remaining Bal: ₹ {payor.balance}")
                    elif report_balance.status == 'Insufficient balance':
                        messages.error(request, f"Insufficient Funds Your Bal: ₹ {payor.balance}, Attempted amount: ₹ {z}")
                    
                    return redirect('/')
                except UserBankAccount.DoesNotExist:
                    payee = None
                    messages.error(request, "Oops Something Went Wrong Kindly Check Account Details, Check Account number")
                    return redirect('/')

    else:
        form = Payment()
        status = ''

    return render(request, 'transfer.html', {'form': form, 'Acc_no': Acc_no})
