#student name:Mohamed Tamer Younes ID:20235027 
#student name:Rokaya Maged Mohamed ID:20236036
#Lab 3 DR Laila
                     #Problem 2

def binary_calculator():
    while True:
        print("\nBinary Calculator **")
        print("A) Insert new numbers")#If user enter (A) user should input 2 binary numbers 
        print("B) Exit")#If user enter (B) program Exit
        print("**")
        choice = input("Please choose a valid choice: ")

        if choice.upper() == 'A':
            while True:
                num1 = input("\nEnter the first binary number: ")#Ask user to enter first binary number
                if is_binary(num1):#if number is true 
                    break# stop
                else:#if number not true
                    print("Error: Please insert a valid binary number.")#Ask user to enter new valid number

            while True:
                num2 = input("\nEnter the second binary number: ")#Ask user to enter second binary number
                if is_binary(num2):#if number is true
                    break#stop
                else:#if number not true
                    print("Error: Please insert a valid binary number.")#Ask user to enter new valid number

            print("\nResult:")
            print("Addition: ", add_binary(num1, num2))#Adding the two binary number entered by user
            print("Subtraction: ", subtract_binary(num1, num2))#subtract the two binary number entered by user
            print("One's complement of first number: ", ones_complement(num1))
            print("One's complement of second number: ", ones_complement(num2))
            print("Two's complement of first number: ", twos_complement(num1))
            print("Two's complement of second number: ", twos_complement(num2))

        elif choice.upper() == 'B':
            print("\nExiting...")
            break

        else:
            print("\nError: Please select a valid choice.")


# Define a function named is_binary that takes a string representation of a binary number as input.
def is_binary(number):
    # Iterate through each digit in the binary number.
    for digit in number:
        # Check if the current digit is not '0' and not '1'.
        if digit != '0' and digit != '1':
            # If the current digit is not a valid binary digit, return False.
            return False
    # If all digits are valid binary digits, return True.
    return True


def add_binary(num1, num2):
    # Determine the maximum length of the binary numbers
    max_len = max(len(num1), len(num2))
    # Left-fill the binary numbers with zeros to make them of equal length
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    # Initialize variables to keep track of carry and the final result
    carry = 0
    result = ''

    # Iterate through the binary numbers from right to left
    for i in range(max_len-1, -1, -1):
        # Initialize the sum of the current bits with the carry
        bit_sum = carry
        # Add the current bit from num1 to bit_sum (convert '1' to 1, '0' to 0)
        bit_sum += 1 if num1[i] == '1' else 0
        # Add the current bit from num2 to bit_sum (convert '1' to 1, '0' to 0)
        bit_sum += 1 if num2[i] == '1' else 0
        # Determine if there is a carry for the next iteration
        carry = 1 if bit_sum >= 2 else 0
        # Append the current bit result to the left side of the result string
        result = ('1' if bit_sum == 1 else '0') + result

    # If there is a carry after the last iteration, add it to the result
    if carry != 0:
        result = '1' + result

    # Return the final binary sum
    return result



# Define a function to subtract two binary numbers
def subtract_binary(num1, num2):
    # Determine the maximum length of the binary numbers
    max_len = max(len(num1), len(num2))
    
    # Left-fill the binary numbers with zeros to make them of equal length
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    # Initialize variables for borrowing and the result
    borrow = 0
    result = ''

    # Iterate through each bit of the binary numbers from right to left
    for i in range(max_len-1, -1, -1):
        # Calculate the difference for the current bit, considering borrowing
        bit_diff = borrow
        bit_diff += 1 if num1[i] == '1' else 0
        bit_diff -= 1 if num2[i] == '1' else 0
        
        # Update borrowing for the next iteration
        borrow = 0 if bit_diff >= 0 else 1
        
        # Append the current bit to the result string
        result = ('1' if bit_diff == 1 else '0') + result

    # Return the final result of the binary subtraction
    return result


# Define a function to calculate the one's complement of a binary number.
def ones_complement(number):
    # Use a list comprehension to create a new binary string where '0' is replaced by '1' and vice versa.
    return ''.join('1' if bit == '0' else '0' for bit in number)

# Define a function to calculate the two's complement of a binary number.
def twos_complement(number):
    # Obtain the one's complement of the binary number.
    complement = ones_complement(number)
    # Add 1 to the one's complement to get the two's complement.
    return add_binary(complement, '1')  # Assuming you have a function add_binary that performs binary addition.

# You have a function call to binary_calculator(), but it's not defined in the provided code.
binary_calculator()


# Define a function to check if a given string is a valid binary number.
def check_binary(input_number):
    # Iterate through each character in the input number.
    for i in input_number:
        # Check if the character is either '0' or '1'.
        if i not in '01':
            # If a character is not '0' or '1', return False (indicating it's not a valid binary number).
            return False
    # If all characters are either '0' or '1', return True (indicating it's a valid binary number).
    return True


# Define a function to display the menu options
def menu1():
    print("\n** please select the operation")
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) addition")
    print("D) subtraction")

# Define a function to compute the one's complement of a binary number
def one_complement(input_number):
    result = ""
    # Iterate through each bit in the input binary number
    for i in input_number:
        # If the bit is '0', append '1' to the result; otherwise, append '0'
        if i == '0':
            result += '1'
        else:
            result += '0'
    return result

# Define a function to compute the two's complement of a binary number
def two_complement(input_number):
    result = ""
    # Iterate through each bit in the input binary number
    for i in input_number:
        # If the bit is '0', append '1' to the result; otherwise, append '0'
        if i == '0':
            result += '1'
        else:
            result += '0'
    return result


# Define a function for binary addition taking two binary numbers as input
def addition(num1, num2):
    # Determine the maximum length of the two binary numbers
    max_len = max(len(num1), len(num2))

    # Left-fill the binary numbers with zeros to make them of equal length
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    # Initialize an empty string to store the result of the addition
    result = ""

    # Initialize a carry variable to handle carryovers during addition
    carry = 0

    # Iterate through the binary numbers from right to left
    for i in range(max_len - 1, -1, -1):
        # Calculate the sum of bits at the current position along with the carry
        bit_sum = carry
        bit_sum += 1 if num1[i] == '1' else 0
        bit_sum += 1 if num2[i] == '1' else 0

        # Update the carry for the next iteration
        carry = 1 if bit_sum >= 2 else 0

        # Add the least significant bit of the sum to the result
        result = ('1' if bit_sum == 1 else '0') + result

    # Left-fill the final result with zeros to maintain the correct length
    return result.zfill(max_len)


# Define a function for binary subtraction taking two binary numbers as input
def subtraction(num1, num2):
    # Determine the maximum length of the two binary numbers
    max_len = max(len(num1), len(num2))

    # Left-fill the binary numbers with zeros to make them of equal length
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    # Initialize an empty string to store the result of the subtraction
    result = ""

    # Initialize a borrow variable to handle borrowing during subtraction
    borrow = 0

    # Iterate through the binary numbers from right to left
    for i in range(max_len - 1, -1, -1):
        # Calculate the difference of bits at the current position along with the borrow
        bit_diff = borrow
        bit_diff += 1 if num1[i] == '1' else 0
        bit_diff -= 1 if num2[i] == '1' else 0

        # Update the borrow for the next iteration
        borrow = 1 if bit_diff < 0 else 0

        # Add the least significant bit of the difference to the result
        result = ('1' if bit_diff == 1 else '0') + result

    # Left-fill the final result with zeros to maintain the correct length
    return result.zfill(max_len)


# Main function to handle user input and execute operations
def main():
    # Infinite loop for user interaction
    while True:
        # Display menu options
        menu1()

        # Get user input for the desired operation
        operation = input("Please enter the operation (A, B, C, D): ")

        # Perform operations based on user choice
        if operation in ('A', 'B'):
            # Handle one's and two's complement operations
            input_number = input("Please insert the number: ")
            if check_binary(input_number):
                if operation == 'A':
                    print("One's complement result: ", one_complement(input_number))
                else:
                    print("Two's complement result: ", two_complement(input_number))
            else:
                print("Invalid binary number!")

        elif operation in ('C', 'D'):
            # Handle addition and subtraction operations
            num1 = input("Please insert the first number: ")
            num2 = input("Please insert the second number: ")
            if check_binary(num1) and check_binary(num2):
                if operation == 'C':
                    print("Addition result: ", addition(num1, num2))
                else:
                    print("Subtraction result: ", subtraction(num1, num2))
            else:
                print("Invalid binary number!")

        else:
            # Display message for invalid operation
            print("Invalid operation!")

        # Ask the user if they want to try again
        again = input("Do you want to try again (yes/no)? ")
        if again.lower() != 'yes':
            # Exit the loop if the user does not want to try again
            break

# Execute the main function if the script is run as the main module
if _name_ == "_main_":
    main()