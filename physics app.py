from physics_module import *
while True:
     try:
         print("WELCOME TO SMT JAMB PHYSICS PAST QUESTIONS")
         m =input("enter your year of interest:")
         if m=="2021":
             physics_year_2021()
             t = input("do you wish to restart(type yes or no):")
             while t.lower() != "no":
                 if t .lower()== "yes":
                     physics_year_2021()
                 t= input("do you wish to restart(type yes or no):")
                 if t.lower() == "no":
                     break
         elif m.lower()=="stop":
             break
         elif m.lower()=="2017":
             physics_2017()
             t = input("do you wish to restart(type yes or no):")
             while t.lower() != "no":
                 if t.lower() == "yes":
                     physics_2017()
                 t = input("do you wish to restart(type yes or no):")
                 if t.lower() == "no":
                     break
     except:
         m = int(input("you must enter your year of interest or type no to stop:"))
