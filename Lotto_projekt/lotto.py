
import random


# a function to check the unique lottery numbers
def CheckForUnikNumbers(num):
  for k in range(len(lucky_numbers)):
    if lucky_numbers[k] == num:
      return False

  return True


# a funcktion that returns a random number between 1-25
def GetRandom():
  return random.randint(1, 1000)


lucky_numbers = []  # samling for holding 5 lycky numbers
print('Welcome to the lottery program')
print('\n')
print('Choose your five lucky numbers\n')

# read 5 lucky numbers and check at the same time if numbers lies between 1-25.
# when the reading is successfull, the program will break the loop.abs
number_conter = 1
while True:
  num = int(input(f'Nummer {number_conter} ?'))
  if num >= 1 and num <= 100:  # check the interval 1-25
    # if interval is ok, then check if number is not entered earlier.
    # following function will check the number is unique.
    # if number is unique you will get True, otherwise False
    res = CheckForUnikNumbers(num)
    if res:  # if True then save the numbers in the samling
      lucky_numbers.append(num)
      number_conter = number_conter +1
      # when the length of the lycky_number list if 5 break the loop.
      # that also means we have collected 5 lycky numbers
      if len(lucky_numbers) == 5:
        break
    else:
      print('Number is already entered earlier')

  else:
    print('Choose a number 1-100')

print('\nYou have entered follwing Lycky numbers!\n')
print(lucky_numbers)

# second part will draw the lottery,
# variables to to hold the number of right match for every number,
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

ans = input('\nEnter \'y\' to start the lottery!! ')

if (ans == 'y'):
  #run a loop to 100000 rounds (numbers of draws)
  for i in range(100000):
    # get a random number in every round. We call a fucmtion to get that number.
    rn = GetRandom()
    # run an a loop and check match between random number and the lycky numbers
    for p in range(len(lucky_numbers)):
      if (lucky_numbers[p] == rn):  # if you found a match
        if p == 0:
          num1 = num1 + 1
          break
        if p == 1:
          num2 = num2 + 1
          break
        if p == 2:
          num3 = num3 + 1
          break
        if p == 3:
          num4 = num4 + 1
          break
        if p == 4:
          num5 = num5 + 1
          break

print('\n')
# following print statements can be programmed using a for loop
print(f'Lucky Number {lucky_numbers[0]} gets {num1} matches!')
print(f'Lucky Number {lucky_numbers[1]} gets {num2} matches!')
print(f'Lucky Number {lucky_numbers[2]} gets {num3} matches!')
print(f'Lucky Number {lucky_numbers[3]} gets {num4} matches!')
print(f'Lucky Number {lucky_numbers[4]} gets {num5} matches!')

total_points = num1 + num2 + num3 + num4 + num5

print(f'\nTotal matches {total_points}')

win = total_points * 0.1

print(f'\nYou win {win:.2f} kr!!')
