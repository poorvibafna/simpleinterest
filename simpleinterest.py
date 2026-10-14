
def simple_interest(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p = int(input("enter principal amt: "))
    i = int(input("enter interest: "))
    t = int(input("enter time in months: "))

    print("simple interest is:", simple_interest(p, i, t))