total = 0
expense = []

num_expense = int(input("Enter the number of expenses: \n"))

for i in range(num_expense):
    expense.append(float(input("Enter an expense: \n")))

total = sum(expense)

print("You spend $", total, sep='')