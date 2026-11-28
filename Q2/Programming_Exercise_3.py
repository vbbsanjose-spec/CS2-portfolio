print("===Science Club Supply Organizer===")

#make the variable, list the supplies, and then display it
supplies = ["Glue", "Scissors", "Paper"]
print("Original Supplies:", supplies)

#Adding tape using append() and then display the new list
supplies.append("Tape")
print("After Adding Tape:", supplies)

#Inserting markers in index 1 using insert() and then display the new list again:>
supplies.insert(1, "Markers")
print("After Inserting Markers:", supplies)

#Throwing out Glue using remove() and then display the final list
supplies.remove("Glue")
print("After Removing Glue:", supplies)
#Displaying the number of supplies
print("Total Supplies:", len(supplies))




