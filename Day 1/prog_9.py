# Create a program that stops printing numbers when it encounters a number greater than 5 using the
# break statement.

for i in range(1,11):
    if i>5:   # skip all number greater then 5
        continue
    else:
        print(i)