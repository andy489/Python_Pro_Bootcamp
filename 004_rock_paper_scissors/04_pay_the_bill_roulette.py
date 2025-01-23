import random as rand

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
who_will_pay_the_bill_1 = rand.choice(friends)
# Option 2
who_will_pay_the_bill_2 = friends[rand.randint(0, len(friends))]

print(who_will_pay_the_bill_1)
print(who_will_pay_the_bill_2)
