# Stage 4/4 of the credit calculator project
import sys
import math
import argparse

#args = sys.argv

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, choices=["diff", "annuity"], required=False)
parser.add_argument("--principal", type=float, required=False)
parser.add_argument("--periods", type=int, required=False)
parser.add_argument("--payment", type=float, required=False)
parser.add_argument("--interest", type=float, required=False)


args, leftovers = parser.parse_known_args()

if args.type is not None and args.principal is not None and args.periods is not None and args.interest is not None:

    credit_principal = args.principal
    periods = args.periods
    credit_interest = args.interest
    nominal_interest = credit_interest / (12 * 100)

    if args.type == 'diff':
        if credit_principal >=0 and periods >= 0 and credit_interest >= 0:

            sum_diff_payments = 0
            for i in range(1, periods + 1):
                montly_diff_payment = math.ceil(credit_principal / periods + nominal_interest * (
                        credit_principal - credit_principal * (i - 1) / periods))
                sum_diff_payments += montly_diff_payment
                print(f"Month {i}: payment is {montly_diff_payment}")
            print("\nOverpayment =", int(sum_diff_payments - credit_principal))

    elif args.type == 'annuity':
        if credit_principal >=0 and periods >= 0 and credit_interest >= 0:

            annuity = math.ceil(credit_principal * (nominal_interest * math.pow(1 + nominal_interest, periods) / (
                    math.pow(1 + nominal_interest, periods) - 1)))
            print(f"Your annuity payment =  {annuity}!")
            print("Overpayment =", int(annuity * periods - credit_principal))

    else:
        print("Incorrect parameters")
        sys.exit()

elif args.type is not None and args.payment is not None and args.periods is not None and args.interest is not None:

    annuity = args.payment
    periods = args.periods
    credit_interest = args.interest
    nominal_interest = credit_interest / (12 * 100)

    if args.type == 'annuity' and annuity >= 0 and periods >= 0 and credit_interest >= 0:

        credit = math.floor(annuity / ((nominal_interest * math.pow(1 + nominal_interest, periods)) / (
                math.pow(1 + nominal_interest, periods) - 1)))
        print(f"Your credit principal = {credit}!")
        print("Overpayment = ", annuity * periods - credit)

    else:
        print("Incorrect parameters")
        sys.exit()

elif args.type is not None and args.principal is not None and args.payment is not None and args.interest is not None:

    credit_principal = args.principal
    payment = args.payment
    credit_interest = args.interest
    nominal_interest = credit_interest / (12 * 100)

    if args.type == 'annuity' and credit_interest >= 0 and payment >= 0 and credit_principal >= 0:

        months = math.ceil(math.log(payment / (payment - nominal_interest * credit_principal),
                                    1 + nominal_interest))
        years = months // 12
        months = months % 12
        if months != 0:
            print(f"You need {years} years and {months} months to repay this credit!")
        else:
            print(f"You need {years} ", "years" if years > 1 else "year", "to repay this credit!")

        print("Overpayment =", int(payment * (years * 12 + months) - credit_principal))

    else:
        print("Incorrect parameters")
        sys.exit()
else:
    print("Incorrect parameters")
    sys.exit()

