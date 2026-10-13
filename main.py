def main():
    print("AI-Assistant")
    print("Welcome Zenith, your AI assistant is ready to help you with your tasks.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AI-Assistant: Goodbye!")
            break
        else:
            # Here you can add logic to process the user input and generate a response
            print(f"AI-Assistant: You said '{user_input}'")

if __name__ == "__main__": #what does this mean? ans:The line `if __name__ == "__main__":` is a common Python idiom that checks whether the script is being run directly or being imported as a module in another script.
    main() #calling it 