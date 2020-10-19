def bmi_calc():
  name = input("please enter your name here")
  print("Name: " + name)
  #5 feet is equal to 60 inch, if your height is 
  height_in = input("Please enter you Height(in)('5 feet = 60 in'):")
  height_in = int(height_in)
  print("Height(in): " + str(height_in) + " Inches")
  weight_lb = input("Please enter you Weight(lb)")
  weight_lb = int(weight_lb)
  print("Weight(lb): " + str(weight_lb) + " Pounds")
  bmi = 703 * (weight_lb / height_in**2)
  print("Your bmi: {b:1.2f}".format(b=bmi))
  
  if bmi < 25 and bmi > 18:
    print(name + ": You are doing great! Keep it Going!")
  elif bmi < 18:
    print(name + ": You are a bit under-weight. You need to eat more.")
  else:
    print(name + ': You are a bit over-weight. You need to eatless and hit the gym at least 3X a week')
