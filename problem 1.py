#student name:Rokaya Maged Mohammed ID:20236036
#student name:Mohamed Tamer Younes ID:20235027 


                     #Problem 1

def validate_number(number, base): #checks input if vaild
    valid_digits = set('0123456789ABCDEF'[:base])
    return all(digit.upper() in valid_digits for digit in str(number)) # converts lower case letters to upper case letters

def convert_to_decimal(number, from_base):
    decimal_number = 0  #initialize a variable to store the decimal eqivalent
    base_multiplier = 1

    for digit in reversed(str(number)):# passes thhrough each digit in a reverse order
        if digit.isnumeric(): #checks if digit is numeric or alphabetic
            digit_value = int(digit) # if true converts number to integer
        else:
            digit_value = ord(digit.upper()) - ord('A') + 10 # if false converts the alphabetic character to its decimal equivalent

        decimal_number += digit_value * base_multiplier #multiplies digit value by base multiplier and adds the value to decimal number
        base_multiplier *= from_base # updates the base multiplier

    return decimal_number
    
def convert_from_decimal(number, from_base, to_base):  #a function to convert the number to it's decimal equivalent
    decimal_number = convert_to_decimal(number, from_base) # brings decimal number from help ro convert function
    result = ''
    while decimal_number > 0:
        remainder = decimal_number % to_base
        result = str(remainder) + result # convert remainder to string and adds it to result
        decimal_number //= to_base # divides decimal number by base

    return result
        
def decimal_to_hexadecimal(number, from_base):
    decimal_number = convert_to_decimal(number, from_base)
    
    hex_digits = "0123456789ABCDEF"  #to match remainders to their corresponding hexadecimal digits
    hex_result = ''

    while decimal_number > 0:
        remainder = decimal_number % 16
        hex_result = hex_digits[remainder] + hex_result #finds corrisponding digit in hexadecimal and adds it to the result from left
        decimal_number //= 16

    return hex_result

def main():
    while True:
        print("- Numbering System Converter -")
        print("A) Insert a new number")
        print("B) Exit program")

        choice_menu_1 = input("Please select an option (A/B): ").upper() #takes the choice and converts lower case letters

        if choice_menu_1 == 'B':
            print("Exiting the program")
            break # exit the loop
        elif choice_menu_1 == 'A':
            number = input("Please insert a number: ").upper() #taking number as input and if letter converts it to uppercase
            #knowing from which base is the inserted number
            from_base = int(input("Enter the base of the number (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal): "))
     
            if not validate_number(number, from_base):
                print("Invalid input. Please enter a valid number.")
                continue

            print("- Please select the base you want to convert the number to -")
            print("A) Decimal")
            print("B) Binary")
            print("C) Octal")
            print("D) Hexadecimal")

            choice_menu_2 = input("Please select a base (A/B/C/D): ").upper() # taking base user wants to convert to

            if choice_menu_2 not in ['A', 'B', 'C', 'D']:
                print("Error: Please select a valid base (A/B/C/D).")
                continue

            if choice_menu_2 == 'D': #if user chooses hexadecimal get result from decimal to hexadecimal
                result = decimal_to_hexadecimal(number, from_base)
            else:
                to_base = {'A': 10, 'B': 2, 'C': 8}[choice_menu_2] #if user chooses other choice than hexadecimal get result from convert from decimal
                result = convert_from_decimal(number, from_base, to_base)

            print("The result is:", result)
            
        else:
              print("please select a valid choice")  # if user didn't choose a or b from choice menu 1

if __name__ == "__main__": #executes main function when the script is run directly
    main() 
