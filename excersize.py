
# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

letter = input('Enter a letter from the alphabet (a-z or A-Z): ').lower()
if letter in 'a e i o u':
  print(f'The letter {letter} is a vowel')
else:
  print(f'The letter {letter} is a consonant')


# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = ''
while phrase != 'quit':
  phrase = input('Enter word or phrase: ')
  print(f'What you entered is {len(phrase)} characters long')

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

dog_years = int(input("Input the dog age: "))
if dog_years < 3:
  human_years = dog_years * 10
else:
  human_years = 20 + (dog_years - 2) * 7
print(f"The dog age in human years is {human_years}")

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter lengths for the sides of a triangle:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == b and b == c:
  print(f'A triangle with {a}, {b} & {c} is an equalateral triangle')
elif a != b and a != c and b != c:
  print(f'A triangle with {a}, {b} & {c} is a scalene triangle')
else:
  print(f'A triangle with {a}, {b} & {c} is an isosceles triangle')

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

term = 0
a = 0
b = 1
while term < 50:
  if term < 2:
    print(f'term: {term} / number: {term}')
  else:
    num = a + b
    print(f'term: {term} / number: {num}')
    a = b
    b = num
  term += 1

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

month = input('Enter the abbreviated month of the seasons (Jan - Dec): ')
day = int(input('Enter the date of that month: '))
if month in ('Jan', 'Feb', 'Mar'):
  season = 'Winter'
elif month in ('Apr', 'May', 'Jun'):
  season = 'Spring'
elif month in ('Jul', 'Aug', 'Sep'):
  season = 'Summer'
else:
  season = 'Fall'
if month == 'Mar' and day > 20:
  season = 'Spring'
elif month == 'Jun' and day > 20:
  season = 'Summer'
elif month == 'Sep' and day > 21:
  season = 'Fall'
elif month == 'Dec' and day > 21:
  season = 'Winter'
print(f'{month} {day} is in {season}')