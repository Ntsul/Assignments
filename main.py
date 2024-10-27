
###########
#task1
#########
number = int(input('enter the number:'))
print(number)

while number > 0:

    print(number)
    number -= 1

###############
#task2
########


# total_sum = 0
#
while True:
    num = input('Enter a positive number or type "sum" to show the total: ')
    if num == 'sum':
        print(total_sum)
        break
    elif int(num) > 0:  #  positive integer
        total_sum += int(num)
    else:
        print("Please enter a valid number.")

##################
#######task3
################
#
import random
random_number = random.randint(0, 15)
print(random_number)
num_of_lives = 5
# num2 = int(input('Enter the number: '))
while num_of_lives > 0:
    chance = int(input('Guess the number: '))
    if random_number == chance:
        print("Congrats, you have guessed the number")

    if random_number < chance:
        print('Entered number is greater')
    elif random_number > chance:
        print('entered number is less')
    else:
        break
    num_of_lives -=1

