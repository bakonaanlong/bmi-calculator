welcome = input("Hey, Fatass, wanna know your BMI? ")

if welcome == "yes" :
    kg = float(input("Alright, Enter your weight in kg "))
    height = float(input("Now, Enter your height in metres "))

    def h2(height):
        return height * height
    h2result = h2(height)

    def bmi(kg, h2result):
        return kg/h2result
    finalbmi = bmi(kg, h2result)

    print ("Your BMI is " + str(finalbmi) + "!")
    if finalbmi < 18.5:
            print ("You're underweight")
    elif finalbmi > 18.5 and finalbmi < 24.9:
            print ("You're Normal")
    elif finalbmi > 25 and finalbmi <29.9:
            print ("You're Overweight")
    else:
            print ("You're obese")

else:
    print ("Then what the fuck are you here for? ")

