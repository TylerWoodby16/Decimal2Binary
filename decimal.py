"""
Tyler Woodby
November 13 2017
The purpose of this code is to convert binary numbers to decimals so they can be added or subtracted, Once they have been added or subtracted that number is converted back into binary
"""



def decimal_to_binary(number): #Turns decimals into binary numbers
  binary_list = []
  old_number = number 
  while (number > .5):
    if number % 2 != 0:
      binary_list.append("1")
    else:
      binary_list.append("0")
    number /= 2
    number = int(number)

  print("The binary form " + str(old_number) + " is: ")
  print(binary_list[::-1])
  return binary_list[::-1]

def binaryListToString(binaryList): #Joins the strings printed in function decimal_to_binary for printing 
  return (''.join(binaryList))

def binary_to_decimal(binary_list, binary_length): #Turns binary into decimal numbers 
  index = 0 
  power = binary_length - 1
  total = 0

  while(power >= 0):
    total += (int(binary_list[index])) * (2**(power))
    index += 1
    power -=1
  print(total)
  return total

def main():
  loop = 0 
  while(loop == 0):
    switch = 0
    firstNumber = ""
    secondNumber = ""
    result = 0

    while(switch == 0):
      binary_number = input("please enter a binary number: ")
      binary_number_list = list(binary_number)
      binary_length = len(binary_number_list)

      isInvalidInput = 0
      for bit in binary_number_list:
        if(int(bit) != 0 and int(bit) != 1):
          print('Invalid binary number, only use 0s and 1s')
          isInvalidInput = 1
          break
      if(binary_length > 8):
        print("please do not print a number longer than 8 bits")
        isInvalidInput = 1
      if isInvalidInput:
        break
      if firstNumber:
        switch = 1
        secondNumber = binary_to_decimal(binary_number_list,binary_length)
        print("Second number has been assigned")
      else:
        firstNumber = binary_to_decimal(binary_number_list,binary_length)
        print("First number has been assigned")

    while (switch == 1):
      operation = input("Enter (1) ADD (2) SUBTRACT (3) CLOSE PROGRAM: ")
      if operation == "1":
        result = (int(firstNumber)) + (int(secondNumber))
      elif operation == "2":
        result = (int(firstNumber)) - (int(secondNumber))
      elif operation == "3":
        print("The program has been terminated.")
        loop = 1
      else:
        print("Not a valid input.")
        break
      resultB = binaryListToString(decimal_to_binary(result))
      print("Result in decimal is: " + str(result) + " AND binary is: " + resultB)
      if not resultB:
        print("Since the result is negative, it cannot be represented as a binary number.")
      switch = 2

     

main() 

