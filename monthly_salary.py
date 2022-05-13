#!/usr/bin/env python

import sys

run = True

while run:
    print(f"Please input your annual salary per year: ", end=' ')  # produces statement with a space
    salary = float(input())  # float for salary, salary can possibly have decimals

    monthly_income = (salary / 12)
    print(f"If you get paid an annual salary of ${round(salary, 2)} you should receive ${round(monthly_income, 2)} per "
          f"month!")

    run_again = input("Would you attempt with different values?: ").lower()  # accepts lowercase input
    while True:
        if run_again == 'yes':
            run = True
            break
        elif run_again == 'no':
            play = False
            sys.exit()
        else:
            run_again = input('Invalid input! Enter "yes" to continue or "no" to exit the calculator: ')
