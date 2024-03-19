#Ask for user input
name= input("What is your name")
age= int(input("How old are you, "+name+"?"))
location= input("Where are you from,"+name+"?")

#Print out a personalized message 
print("\nHello" +name+ "!")
print ("Next year, you will be " +str(age + 1)+".")
print("I've heard"+ location+" is a great place!")