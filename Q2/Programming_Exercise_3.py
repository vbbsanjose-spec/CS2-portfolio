#Problem 1: Science Club Supply Organizer
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

#Problem 2: Classroom Attendance Counter
print("===Classroom Attendance Counter===")

#make the list using a variable
Initial_Data_attendance = ["Present", "Absent", "Present", "Present", "Absent", "Present"]

#set the student_no to one for first try
student_no = 1
#loop through each record 
for a in Initial_Data_attendance:
  print("student", student_no,":", a)
  student_no = student_no + 1

#display the attendance summary using len() and count()
print("\nAttendance Summary")
print("Total Students:", len(Initial_Data_attendance))
print("Present:", Initial_Data_attendance.count("Present"))
print("Absent:", Initial_Data_attendance.count("Absent"))



