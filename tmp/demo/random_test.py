import random

for i in range(1):
    print(random.randrange(20))

for i in range(1):
    print(random.randrange(5, 20))

for i in range(1):
    print(random.randrange(10, 21, 5))
print("######")
for i in range(1):
    print(random.randint(1, 4))
    print(random.random())
    print(random.uniform(4, 2))

print(random.choice([1, 23, 5, 6]))
print("######")
a = [1, 5, 7, 3, 9]
print(random.choices(a, weights=[1, 5, 1, 1, 1], k=5))
print(random.choices(a, cum_weights=[1, 2, 3, 4, 5], k=5))
b=[{"a":1},{"b":2}]
random.shuffle(b)
print(b)

print(random.sample([1, 33, 7, 3], 3))
