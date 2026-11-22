# Exercise 1


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

  
