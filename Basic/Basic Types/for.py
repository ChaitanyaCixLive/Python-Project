words = ['cat', 'dog', 'elephant']

for w in words:
    print(w, len(w))

for i in range(5):
    print(i)

print()
for i in range (1, 10, 3):      # does not include 10
    print(i)

print()
for i in range (-1, -10, -2):
    print(i)

print(range(10))

listA = list(range(5))
print(listA)

# Loop statements may have an else clause; it is executed when the loop terminates
# through exhaustion of the list (with for) or when the condition becomes false (with while),
# but not when the loop is terminated by a break statement. This is exemplified by the following loop,
# which searches for prime numbers:

for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print(i, 'equals', j, '*', i//j)
            break
    else:
        print(i, "is a prime number")

