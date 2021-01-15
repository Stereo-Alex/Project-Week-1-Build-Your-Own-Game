def cpu_function_range():
    return 100, 200

def cpu_game_choice(low, high):
    while True:
        num = int(input(f"Enter a number between {low} and {high} for the computer to guess: "))
        if low > num or num > high:
            print(f"Must be in range [{low}, {high}], please stick to the range im already having a hard enough time")
            continue
            
        else:
            print("Number picked, the computer will now try to guess", num)
            return num


def computer_guess(num, low, high):
    guess = None
    while guess != num:
        guess = (high - low) // 2 + low
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")

low, high = cpu_function_range()
computer_guess(cpu_game_choice(low, high), low, high)