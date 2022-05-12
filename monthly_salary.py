run = True

while run:
    print(f"Please input your annual salary per year: ", end=' ')

    salary = float(input())

    monthly_income = (salary / 12)
    print(f"If you get paid an annual salary of ${round(salary, 2)} you should receive ${round(monthly_income, 2)} per "
          f"month!")

    run_again = input("Would you attempt with different values?: ").lower()
    while True:
        if run_again == 'yes':
            run = True
            break
        elif run_again == 'no':
            play = False
            break
        else:
            run_again = input('Invalid input! Enter "yes" to continue or "no" to exit the calculator: ')
