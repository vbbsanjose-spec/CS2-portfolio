# Exercise 1

# Create a list containing five school supplies school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]
school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

#Display all five items individually using their index positions (without using a loop)
print("===School items===")
print("•", school_items[0])
print("•", school_items[1])
print("•", school_items[2])
print("•", school_items[3])
print("•", school_items[4])

#Display the first item separately using index 0
print("\nThe first item is a", school_items[0])
#Display the first item separately using negative indexing (-1 refers to the last element)
print("\nThe last item is a", school_items[-1])


# Exercise 2

#Create a list of five travel destinations
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

#Iterate through the list with a for loop and print each destination
print("All travel destinations:")
for a in destinations:
  print("•", a)

#Slice the list from index 1 up to (excluding) index 4, returning indices 1, 2, and 3
print("\nIndex 1 to 3(slice 1:4): ")
print(destinations[1:4])

#Prompt the user for a destination name and remove extra whitespace around it
place = input(str("\nEnter your desired place: ")).strip().title()

#Check whether the entered destination is present in the list
if place in destinations:
  print("\nYour destination is on the list!")

else:
  print("\nYour destination is not on the list.")

#Replace the element at index 2 ("Davao") with "Iloilo"
destinations[2] = "Iloilo"
#Display the modified list
print("The updated list is", destinations)

  
