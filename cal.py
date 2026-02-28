HISTORY_FILE = "history.txt"

def show_History():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("ther is not found in the txt file")
    else:
        for line in reversed(lines):
            print(line.strip())    #strip() display lines one by  one
    file.close()

def clear_history():
    file = open(HISTORY_FILE , 'w')
    file.close()
    print("history cleard")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculation(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input !, use format")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == "0":
            print("invalid input")
            return
        result = num1 / num2
    elif op == "%":
        if num2 == "0":
            print("invalid input")
            return
    else:
        print("Invalid operator")
    
    if int(result) == result:
        result = int(result)
    print("Result:" ,result)
    save_to_history(user_input, result)

def main():
    print("Simple calculation")
    while True:
        user_input = input("Enter calculation or command ").strip().lower()
        # add multiple inputs
        if user_input == "exit":
            print("Goodbye")
            break
        elif user_input == "clear":
            clear_history()
        elif user_input == "history":
            show_History()
        else:
            calculation(user_input)

main()