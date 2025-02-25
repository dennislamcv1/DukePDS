# calculate retirement savings
#  start_age is the age (in months) when we start the calculation
#  initial is the initially saved balance at the start
#  working is a three tuple (months, contribution, rate of return)
#  retired is a three tuple (months, contribution, rate of return)


def print_balance(age_months, balance):
    age_years = age_months // 12
    months = age_months % 12
    print(f"Age {age_years:3d} month {months:2d} you have ${balance:.2f}")


def grow_balance(start_age, initial, period_info):
    months, contribution, rate_of_return = period_info
    balance = initial

    for month in range(months):
        print_balance(start_age + month, balance)
        balance += balance * rate_of_return
        balance += contribution

    return balance, start_age + months


def calculateRetirement(start_age, initial, working, retired):
    # Calculate the working period
    end_balance, age_after_working = grow_balance(start_age, initial, working)

    # Calculate the retirement period
    grow_balance(age_after_working, end_balance, retired)


def main():
    working = (489, 1000, 0.045 / 12)
    retired = (384, -4000, 0.01 / 12)
    calculateRetirement(327, 21345, working, retired)


if __name__ == "__main__":
    main()
