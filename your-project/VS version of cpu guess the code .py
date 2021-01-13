def cpu_function_range():
    list_of_range = []
    for number in range(1, 1001):
        list_of_range.append(number)
    return list_of_range

def cpu_game_choice():
    num = int(input("Enter a number between 0 and 1000 for the computer to guess: "))
    if num < 1:
        print("Must be in range [1, 1000], please stick to the range im already having a hard enough time")
        cpu_game_choice()
        
    elif num > 1000:
        print("Must be in range [1, 1000], please stick to the range im already having a hard enough time")
        cpu_game_choice()
    
    else:
        print("Number picked, the computer will now try to guess", num)
        return num


def computer_guess(num, list_of_range):
    low = 1
    high = len(list_of_range)
    guess = len(list_of_range) //2
    while guess != num:
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")

computer_guess(cpu_game_choice(), cpu_function_range())