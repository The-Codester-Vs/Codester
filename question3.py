# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

odd_numbers = []
max = int(input('Enter the number: '))

for i in range(max):
    if i % 2 == 1:
        odd_numbers.append(i)

print(f"Odd numbers:{odd_numbers }")
