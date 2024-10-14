"""

def addNumbers(input1, input2):
    input3 = input1 + input2
    return input3

print(addNumbers(23,54))

"""

def encoding_function(message_in_number):
    numbers = message_in_number.split()
    result = ""
    for number in numbers:
        num = int(number)
        if num in my_dict:
            result += my_dict[num]
        else:
            print("The numbers/alphabets are not in the range")

    print(f"The encoded message is: {result}")

    return result

num_list = [0,1,2,3,4,5,6,7,8,9]
num_alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
my_dict = dict(zip(num_list, num_alph))
print(my_dict)
print("enter the numbers with a space between them")
encoded_string = input()
encoding_function(encoded_string)