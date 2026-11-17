#Exercise 1 
#range(start, stop, step): start at 2, stop at 21(and excluded), multiples of or jump by 2 
#stop is 21 because range doesn't include the stop value and we need 20
for Jolibee in range(2, 21, 2):
  print(Jolibee)


#Exercise 2
#Using the explanation for exercise 1, we start at 10, end at 0, and -1 because we minus 1 for every step
for Mcdo in range(10, 0, -1):
  print(Mcdo)
print("Time's up!")
#print("Time's up!") is not indented because we need to mention the phrase at the end once
#if print("Time's up!") is indented then it would be mentioned every step

#Exercise 3
#Go through 1 to 15 (stop is 16 because range excludes last value)
for num in range(1, 16):
    # n % 3 gives the remainder when dividing by 3.
    # A remainder of 0 means n is a multiple of 3.
    if num % 3 == 0:
        continue
      #Just skip to the next number if a multiple of 3 appears 
    print(num)


 
#Exercise 4
def show_table(number):
    for jolibee in range(1, 11):
      #Starts at 1 but stops at 11(but excluded)
        print(number, "x", jolibee, "=", number * jolibee)
      #Multiply the number by the range and equal to the product equation 
      


num = int(input("Enter a number: "))
#Get the input

show_table(num)
#Calls the function and gives it the number entered by the user


