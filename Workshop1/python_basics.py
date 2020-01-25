"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    ##number = input("give me a number: ")
    if(num % 2 == 0):
        print("even")
    else:
        print("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """

    genNum = random.randint(1,9)
    userInput = "tgh"

    while(userInput != "exit"):
        userInput = input("What's your guess? ")
        if(userInput == "exit"):
           break
        if(int(userInput) < genNum):
            print("Too low")
        elif(int(userInput) > genNum):
            print("Too high")
        else:
            print("Exactly")
        genNum = random.randint(1,9)


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    isTrue = True;
    for x in range(len(string)):
        if(string[x] != string[len(string)-x - 1]):
            print("False")
            isTrue = False;
            break
    if(isTrue):
        print("True")

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

    fileStream = open(filename, "w")
    newUN = base64.b64encode(username.encode('utf-8'))
    newPass = base64.b64encode(password.encode('utf-8'))
    fileStream.write(newUN.decode('utf-8') + "\n")
    fileStream.write(newPass.decode('utf-8'))
    fileStream.close()

    
def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    fileStream = open(filename, "r")
    lines = fileStream.readlines()
    fileStream.close()
    if(password == None):
        for i in lines:
            print(base64.b64decode(i.encode('utf-8')).decode('utf-8'))
    else:
        user = base64.b64decode((lines[0]).encode('utf-8')).decode('utf-8')
        print(user)
        print(password)
        part4a(filename, user, password)
        
    
    
if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
