salary = float(input("Enter the starting salary: "))
total_cost = 1000000
down_payment = 0.25 * total_cost
r = 0.04
raise_rate = 0.07

low, high =0,10000
steps = 0

def savings(rate):
    current = 0
    monthly_salary = salary / 12

    for m in range(0,37):
        current += current * r / 12
        current += monthly_salary * rate
        if (m) % 6 == 0:
            monthly_salary *= (1 + raise_rate)
    return current

if savings(1) < down_payment - 100:
    print("It is not possible to pay the down payment in three years.")
else:
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000
        s = savings(rate)

        if abs(s - down_payment) <= 100:
            print("Best savings rate:",(rate))
            print("Steps in bisection search:", steps)
            break
        elif s < down_payment:
            low = mid + 1
        else:
            high = mid - 1