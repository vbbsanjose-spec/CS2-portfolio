score = int(input("Yow, how many did you get from the Computer Science 100 items exam?: "))
#Here, we ask for the student's score

if score < 0 or score > 100:
  print("What!? You have an Invalid Score! The score that you must get only extends from 0 to 100!")
#But first, we must validate if the score is not included from 0 to 100

#Now, we sort the scores from their respective identification
elif score >= 90: 
   print("WOW! Your score is Outstanding!!! Good job!")

elif score >= 80:
  print("Nice! Your score is very satisfactory, good job!")

elif score >= 75:
  print("Your score is satisfactory, good job!")

else:
  print("Your score Needs Improvement, and that is ok! Come back stronger, bro")
  
