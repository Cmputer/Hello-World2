def printMessage():                                                                 # A simple method to print the message at the end
                                                        
    print("This is a simple java class that can be cloned and used \n" +
          "by the user to learn more about GitHub. This same program is \n" +
          "available in multiple different languages to give a good idea\n" +
          "of how repositories work. Please refer to the README.md file in \n" +
          "this repo to learn more about adding this to your OWN GitHub\n" +
          "and how to eventually showcase your own code!")

def main():
    print("Hello World!")                                                           # Print "Hello World!" to the console
    print("Press the enter key to continue...")                                     # Prompt the user to press enter

    input_str = input()                                                             # Read a line of input from the user and store it in the 'input_str' variable

    while input_str:                                                                # Enter a loop that will continue as long as the user enters non-empty input
        print("Incorrect input. Please just press enter!")                          # Print an error message indicating that the input was incorrect
        input_str = input()                                                         # Read another line of input from the user

    printMessage()                                                                  # Call the printMessage() function after the correct input is provided

if __name__ == "__main__":
    main()
