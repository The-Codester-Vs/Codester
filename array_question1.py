# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


# solution
exp = [2200, 2350, 2600, 2130, 2190]

# 1
print(f"In feb,Dollars spent extra compare to jan are: {exp[1] - exp[0]} ")

# 2
print(f'The total expense in first three months are {exp[1]+exp[2]+exp[0]}')

# 3
print(f"Did I spent 2000 in any month:{2000 in exp}")

# 4
exp.append(1980)
print(f"adding exp of june in the list: {exp}")

# 5
exp[3] = exp[3] - 200
print(f'return 200$ in april month {exp}')
