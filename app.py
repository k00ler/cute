
counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is 12 + 2?")
  print("   a) 10")
  print("   b) 24")
  print("   c) 14")
  print("   d) 6")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is not subtraction."
    score -=1
  elif answer == "b":
    output = "Wrong. This is not multiplication."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. This is not division."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "The chemical formula H2 represents")
  print("   a) one hydrogen molecule")
  print("   b) two hydrogen atoms")
  print("   c) one hydrogen atom")
  print("   d) two hydrogen molecules")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. If so, then it will be written as H and H - two hydrogen atoms."
    score -=1
  elif answer == "c":
    output = "Wrong. Clearly the number 2 in the formulae must mean something?"
    score -=1
    
  elif answer == "d":
    output = "Wrong. What's the difference between a molecule and an atom?"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "whats the speed of light?")
  print("   a) 3.0 x 10^8 m/s")
  print("   b) 330 m/s)
  print("   c) 1.24x10^8 m/s")
  print("   d) 2.0 x 10^8 m/s")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "correct!"
    score -=1
  elif answer == "b":
    output = "Wrong. This is the speed of sound  "
    score -=1
  elif answer == "c":
    output = "Wrong. This is the speed of light in diamond"
    score -=1
    
  elif answer == "d":
    output = "wrong. this is the speed of light in glass"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
