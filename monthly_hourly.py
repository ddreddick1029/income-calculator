import sys

run = True

while run:

    print("Welcome to the Income Calculator!")

    print("Please input how much you are expected to make per hour: ", end=' ')
    hourlypay = float(input())

    print("Please input how many hours you expect to work per week: ", end=' ')
    hoursweek = float(input())

    monthly_income = ((hourlypay * hoursweek) * 52 / 12)

    print(
        f"If you get paid at a rate of ${hourlypay} and perform {hoursweek} hours of work, you can expect to make "
        f"${round(monthly_income, 2)} each month!")

    run_again = input("Would you attempt with different values?: ")
    while True:
        if run_again == 'yes':
            run = True
            break
        elif run_again == 'no':
            sys.exit()  # when user inputs "no", the program will exit
        else:
            run_again = input('Invalid input! Enter "yes" to continue or "no" to exit!: ')
