print(f"Please input your annual salary per year: ", end=' ')

salary = float(input())

monthly_income = (salary / 12)
print(f"If you get paid an annual salary of ${round(salary, 2)} you should receive ${round(monthly_income, 2)} per "
      f"month!")

