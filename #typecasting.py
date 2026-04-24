#IF STATEMENTS
#CALCULATOR
operator = input("WHAT DO YOU WANT TO DO?: WEIGHT CONVERTOR (WC), TEMPERATURE CONVERTOR(TC) DISTANCE CONVERTOR(DC) CALCULATOR (M) ")
if operator == "WC":
    w = input("Is your actual weight in (KG) or (LB)?  ")
    if w == "LB":
        weight = float(input("please enter a weight in pounds: "))
        weight = round(weight / 2.205,2)
        print(f"{weight}kg")
    if w == "KG":
        weight = float(input("please enter a weight in kilograms: "))
        weight = round(weight * 2.205, 2)
        print(f"{weight}Lb") 
    else:
        print(f"{w} is/are not valid")
elif operator == "M":
    op2 = input("Enter an operator (+,-,*,/,^)  ")
    if op2 == "^":
        number = float(input("Please enter a number: "))
        power = float(input("Enter a power: "))
        result =round(pow(number, power))
        print(result)
    if op2 == "+":
        num1 = float(input("enter a value: "))
        num2 = float(input("enter another value: "))
        result = round(num1 + num2, 3)
        print(result)
    if op2 == "-":
        num1 = float(input("enter a value: "))
        num2 = float(input("enter another value: "))
        result = round(num1 - num2, 3)
        print(result)
    if op2 == "/":
        num1 = float(input("enter a value: "))
        num2 = float(input("enter another value: "))
        result = round(num1 / num2, 3)
        print(result)
    if op2 == "*":
        num1 = float(input("enter a value: "))
        num2 = float(input("enter another value: "))
        result = round(num1 * num2, 3)
        print(result)
    else:
        print(f"{op2} is/are not valid")
elif operator == "TC":
    gr = input("Currently your temperature is in Celsius(C), Farenheit(F) or Kelvin(K)?  ")
    if gr == "C":
        Decision = input("Do you want to convert to Farenheit(F) or Kelvin(K)? ")
        if Decision == "F":
            Degrees = float(input("enter a degree in Celsius (C): "))
            result = round((Degrees * 1.8) +32, 2)
            print(f"{result}°F")
        if Decision == "K":
            Degrees = float(input("enter a degree in Celsius (C): "))
            result = round(Degrees + 273.15, 2)
            print(f"{result}°K")
    elif gr == "F":
        Decision = input("Do you want to convert to Celsius(C) or Kelvin(K)? ")
        if Decision == "C":
            Degrees = float(input("enter a degree in Farenheit (F): "))
            result = (Degrees - 32) / 1.8
            print(f"{result}°C")
        if Decision == "K":
            Degrees = float(input("enter a degree in Farenheit (F): "))
            result = round((Degrees-32.0)/1.8 + 273.15, 2)
            print(f"{result}°K")
    elif gr == "K":
        Decision = input("Do you want to convert to Celsius(C) or Farenheit(F)? ")
        if Decision == "C":
            Degrees = float(input("enter a degree in Kelvin (K): "))
            result = round(Degrees - 273.15, 2)
            print(f"{result}°C")
        if  Decision == "F":
            Degrees = float(input("enter a degree in Kelvin (K): "))
            result = round( (1.8 * (Degrees - 273)) + 32)
            print(f"{result}°F")    
    else:
        print(f"{gr} is/are not valid")  
elif operator == "DC":
    Me = input("is your distance currently in milimeters (mm), centimeters (cm), meters (m), feet (ft), inches (in), Kilometers (km)? ")
    if Me == "mm":
        Decision = input("What do you want them to be? centimeters (cm), meters (m), feet (ft), inches (in), Kilometers (km):  ")
        if Decision == "cm":
            do = int(input("Enter the current value: "))
            re = round(do / 10 , 2)
            print(f"{re}cm")
        if Decision == "m":
            do = int(input("Enter the current value: "))
            re = round(do / 1000 , 2)
            print(f"{re}m")
        if Decision == "ft":
            do = int(input("Enter the current value: "))
            re = round(do / 304.8 , 2)
            print(f"{re}ft")
        if Decision == "in":
            do = int(input("Enter the current value: "))
            re = round(do / 25.4 , 2)
            print(f"{re}in")
        if Decision == "km":
            do = int(input("Enter the current value: "))
            re = round(do / 1000000 , 2)
            print(f"{re}km")
    if Me == "cm":
        Decision = input("What do you want them to be? milimeters (mm), meters (m), feet (ft), inches (in), Kilometers (km):  ")
        if Decision == "mm":
            do = int(input("Enter the current value: "))
            re = round(do * 10 , 2)
            print(f"{re}mm")
        if Decision == "m":
            do = int(input("Enter the current value: "))
            re = round(do / 100 , 2)
            print(f"{re}m")
        if Decision == "ft":
            do = int(input("Enter the current value: "))
            re = round(do / 30.48 , 2)
            print(f"{re}ft")
        if Decision == "in":
            do = int(input("Enter the current value: "))
            re = round(do / 2.54 , 2 )
            print(f"{re}in")
        if Decision == "km":
            do = int(input("Enter the current value: "))
            re = round(do / 100000 , 2)
            print(f"{re}km")
    if Me == "m":
        Decision = input("What do you want them to be? milimeters (mm), centimeters (cm), inches (in), Kilometers (km):  ")
        if Decision == "mm":
            do = int(input("Enter the current value: "))
            re = round(do * 1000 , 2)
            print(f"{re}mm")
        if Decision == "cm":
            do = int(input("Enter the current value: "))
            re = round(do * 100 , 2)
            print(f"{re}cm")
        if Decision == "ft":
            do = int(input("Enter the current value: "))
            re = round(do * 3.28084 , 2)
            print(f"{re}ft")
        if Decision == "in":
            do = int(input("Enter the current value: "))
            re = round(do * 39.3701 , 2)
            print(f"{re}in")
        if Decision == "km":
            do = int(input("Enter the current value: "))
            re = round(do / 1000 , 2)
            print(f"{re}km")
    if Me == "ft":
        Decision = input("What do you want them to be? milimeters (mm), centimeters (cm), meters (m), inches (in), Kilometers (km):  ")
        if Decision == "mm":
            do = int(input("Enter the current value: "))
            re = round(do * 304.8 , 2)
            print(f"{re}mm")
        if Decision == "cm":
            do = int(input("Enter the current value: "))
            re = round(do * 30.48 , 2)
            print(f"{re}cm")
        if Decision == "m":
            do = int(input("Enter the current value: "))
            re = round(do / 3.28084 , 2)
            print(f"{re}m")
        if Decision == "in":
            do = int(input("Enter the current value: "))
            re = round(do * 12 , 2)
            print(f"{re}in")
        if Decision == "km":
            do = int(input("Enter the current value: "))
            re = round(do / 3280.84 , 2)
            print(f"{re}km")
    if Me == "in":
        Decision = input("What do you want them to be? milimeters (mm), centimeters (cm), meters (m), feet (ft), Kilometers (km):  ")
        if Decision == "mm":
            do = int(input("Enter the current value: "))
            re = round(do * 25.4 , 2)
            print(f"{re}mm")
        if Decision == "cm":
            do = int(input("Enter the current value: "))
            re = round(do * 2.54 , 2)
            print(f"{re}cm")
        if Decision == "m":
            do = int(input("Enter the current value: "))
            re = round(do / 39.3701 , 2)
            print(f"{re}m")
        if Decision == "ft":
            do = int(input("Enter the current value: "))
            re = round(do / 12 , 2)
            print(f"{re}ft")
        if Decision == "km":
            do = int(input("Enter the current value: "))
            re = round(do / 39370 , 2)
            print(f"{re}km")
    if Me == "km":
        Decision = input("What do you want them to be? milimeters (mm), centimeters (cm), meters (m), feet (ft), inches (in):  ")
        if Decision == "mm":
            do = int(input("Enter the current value: "))
            re = round(do * 100000 , 2)
            print(f"{re}mm")
        if Decision == "cm":
            do = int(input("Enter the current value: "))
            re = round(do * 100000 , 2)
            print(f"{re}cm")
        if Decision == "m":
            do = int(input("Enter the current value: "))
            re = round(do * 1000 , 2)
            print(f"{re}m")
        if Decision == "ft":
            do = int(input("Enter the current value: "))
            re = round(do * 3280.84 , 2)
            print(f"{re}ft")
        if Decision == "in":
            do = int(input("Enter the current value: "))
            re = round(do * 39370.1 , 2)
            print(f"{re}in")
else:
    print(f"{operator} is/are not valid")


