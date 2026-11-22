# Exercise 1

school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

print("===School items===")
print(school_items[0])
print(school_items[1])
print(school_items[2])
print(school_items[3])
print(school_items[4])

print("\nThe first item is a", school_items[0])
print("\nThe last item is a", school_items[-1])


# Exercise 2

destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

print("All travel destinations:")
for a in destinations:
  print(a)

print("\nIndex 1 to 3(slice 1:4): ")
print(destinations[1:4])

place = input(str("\nEnter your desired place: ")).strip().title()

if place in destinations:
  print("\nYour destination is on the list!")

else:
  print("\nYour destination is not on the list.")

destinations[2] = "Iloilo"
print("The updated list is", destinations)

  
