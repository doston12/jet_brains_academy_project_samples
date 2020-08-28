# Stage 2/4 of the credit calculator project
import math

print("What do you want to calculate?\n",
      'type "n" for the count of months,\n',
      'type "a" for the annuity monthly payment,\n',
      'type "p" for the credit principal: ')
option = input()

if option == 'n':
    credit_principal = float(input("Enter the credit principal: "))
    monthly_payment = float(input("Enter the monthly payment: "))
    credit_interest = float(input("Enter the credit interest: "))

    nominal_interest = credit_interest / (12 * 100)
    months = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_interest * credit_principal), 1+nominal_interest))
    years = months // 12
    months = months % 12
    if months != 0:
        print(f"You need {years} years and {months} months to repay this credit!")
    else:
        print(f"You need {years} ", "years" if years > 1 else "year", "to repay this credit!")
elif option == 'a':
    credit_principal = float(input("Enter the credit principal: "))
    periods = int(input("Enter the number of periods: "))
    credit_interest = float(input("Enter the credit interest: "))

    nominal_interest = credit_interest / (12 * 100)
    annuity = math.ceil(credit_principal * (nominal_interest * math.pow(1+nominal_interest, periods) / (math.pow(1+nominal_interest, periods) - 1)))
    print(f"Your annuity payment =  {annuity}!")
elif option == 'p':
    annuity = float(input("Enter the annuity payment: "))
    periods = int(input("Enter the count of periods: "))
    credit_interest = float(input("Enter the credit interest: "))

    nominal_interest = credit_interest / (12 * 100)
    credit = math.floor(annuity / ((nominal_interest * math.pow(1+nominal_interest, periods)) / (math.pow(1+nominal_interest, periods) - 1)))
    print(f"Your credit principal = {credit}!")