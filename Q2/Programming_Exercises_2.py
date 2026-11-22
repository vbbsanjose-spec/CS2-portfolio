# Exercise 1

destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

print("All travel destinations:")
for a in destinations:
  print(a)

print("\nIndex 1 to 3(slice 1:4): ")
print(destinations[1:4])

place = input(str("\nWhere do you want to go?")).strip()

if place in destinations:
  print("Your destination is on the list!")

else:
  print("Your destination is not on the list.")



  
  
  
