# Create a program that prints the multiplication table of a given number using a while loop

num = int(input("Enter a number to print it table"))
i = 1

while i<= 10:
    print(f"{num}x{i} = {num * i}")
    i += 1