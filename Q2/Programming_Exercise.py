#Exercise 1 
for Jolibee in range(2, 21, 2):
  print(Jolibee)


#Exercise 2
for Mcdo in range(10, 0, -1):
  print(Mcdo)
print("Time's up!")

#Exercise 3
for num in range(1, 16):
    if num % 3 == 0:
        continue
    print(num)

#Exercise 4
def show_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


num = int(input("Enter a number: "))

show_table(num)
