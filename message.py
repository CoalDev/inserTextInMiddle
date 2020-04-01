from insertTextInMiddle import insertText
import pyperclip as pc

def main():
    # This is the word variable to put in the middle
    word = " סייבר "

    # Getting user input, the string that we will insert
    message = input("Enter the message: ")

    # Calling the function inserText and get the final text
    finalText = insertText(message.split(), word)

    # Copying the finalText to the clipboard
    pc.copy(finalText)

if __name__ == "__main__":
    main()