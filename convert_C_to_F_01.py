# FILE NAME - convert_C_to_F_01.py

# NAME: Bailey Orlick
# DATE: 2/15/2025
# BRIEF DESCRIPTION: This will output the conversion, Celcius to Fahrenheit. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########

C = int(input('Enter a temperature in Celcius: '))

F = C * 9/5 + 32

print(f'{C} degrees Celcius is {F} degrees Fahrenheit.')



########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?

Float means floating-point number



2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?

The solution to the equation should be an exact number, including a decimal, as opposed to an integer, which only outputs the whole number, without the decimal.



'''
