print('Welcome to the love Calculator')
name_1 = input('What is your name? \n')
name_2 = input("What is your lover's name \n ")
name = name_1 + name_2

t = name.lower().count('t')
r = name.lower().count('r')
u = name.lower().count('u')
e = name.lower().count('e')

l = name.lower().count('l')
o = name.lower().count('o')
v = name.lower().count('v')
e = name.lower().count('e')

first_Score = t + r + u + e
second_Score = l + o + v + e

score = str(first_Score) + str(second_Score)
if score <= '10' or score >= '90':
    print(f'Your score is {score}, you go together like coke and mentos')
elif score >= '40' or score <= '50':
    print(f'Your score is {score}, you are alright together')
else:
    print(f'Your score is {score}')
