# Function to handle user commands
def handle_command(command):
    cmd = command.lower()
    if cmd == 'hello' or cmd == 'hi' or cmd == 'hey':
        return "Hello! How can I help you? \U0001F44B"  
    elif cmd == 'bye':
        return "Goodbye! Have a great day. \U0001F44B" 
    elif cmd == 'help':
        return "Available commands: hello, hi, hey, bye, help"
    else:
        return "Sorry, I don't understand that command. Type 'help' for available commands."

# Main function 
def main():
    print("Welcome to the Python Prompt Bot!")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("Vall: ")
        
        if user_input.lower() == 'bye':
            print("Babe: Goodbye! \U0001F44B")  
            break
        
        response = handle_command(user_input)
        print("Babe:", response)

if __name__ == "__main__":
    main()
