print("Welcome to the Income Calculator!")

print("Please input how much you are expected to make per hour: ", end=' ')
hourlypay = float(input())

print("Please input how many hours you expect to work per week: ", end=' ')
hoursweek = float(input())

monthly_income = ((hourlypay * hoursweek) * 52 / 12)

print(
    f"If you get paid at a rate of ${hourlypay} and perform {hoursweek} hours of work, you can expect to make "
    f"${round(monthly_income, 2)} each month!")
