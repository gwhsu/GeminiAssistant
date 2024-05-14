# main.py

from assistant import Assistant

def main():
    assistant = Assistant()
    
    while True:
        user_input = input("Input your question (type 'exit' or 'q' to quit): ")
        if user_input.lower() == ('exit' or 'q'):
            break
        response = assistant.ask_question(user_input)
        print(response)

if __name__ == "__main__":
    main()
