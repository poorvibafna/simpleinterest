def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

if __name__ == "__main__":
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))

    interest = simple_interest(principal, rate, time)

    print("Simple Interest is:", interest)