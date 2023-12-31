def loan_emi(amount,duration,rate,down_payment=0):
   loan_amount = amount - down_payment
   emi=loan_amount*rate*((1+rate)**duration)/(((1+rate)**duration)-1)
   return emi
p = loan_emi(1250000,8*12,0.1/12,3e5)
print(p)
