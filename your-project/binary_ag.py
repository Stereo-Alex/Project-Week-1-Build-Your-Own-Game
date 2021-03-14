def cpu_function_range():
    low = int(input("Set the lower limit of the game, this allows the computer to narrow it down"))
    high = int(input("Set the higher limit of the game"))
    return low, high


def cpu_game_choice(low, high):
    while True:
        num = int(input(f"Enter a number between {low} and {high} for the computer to guess: "))
        if low > num or num > high:
            print(f"Must be in range [{low}, {high}], please stick to the range im already having a hard enough time")
            continue

        else:
            print("Number picked, the computer will now try to guess: ", num)
            return num


def computer_guesses(num, low, high):
    guesses = []
    guess = None
    while guess != num:
        guess = (high - low) // 2 + low
        guesses.append(guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1
    return guesses


def print_guesses(guesses):
    for guess in guesses[:-1]:
        print(f"The computer has guessed: {guess}")
    print(f"The computer guessed {guesses[-1]} and it was correct!")


def cpu_function_range_2(bound):
    return int(input(f"Set the {bound} limit of the game"))


def player_game(low, high):
    import random
    random_number = random.randrange(low, high)
    #print(random_number)
    try_counter = 0
    print(f"The game has started, your scoreboard is at {try_counter}")
    player_guess = 0
    while player_guess != random_number:
        player_guess = int(input("Please input your guess: "))
        if player_guess < random_number:
            print("Your guess is too low")
            try_counter = try_counter + 1
        if player_guess > random_number:
            print("Your guess is too high")
            try_counter = try_counter + 1
    else:
        print(f"You guessed right! The secret number was:  {random_number}")

    final_result = print(f"You have guessed the number in {try_counter}, turns")

    return final_result




def main():
    game_choice = input("Wellcome to the game."
                        "\n"
                        "Do you want to play yourself or make the computer play?"
                        "\n"
                        "If you want to play yourself please input 1,"
                        "\n"
                        "if you would prefer the computer to play then press 2")

    if game_choice == "1":
        return player_game(cpu_function_range_2("lower"), cpu_function_range_2("upper"))

    elif game_choice == "2":
        low, high = cpu_function_range()
        guesses = computer_guesses(cpu_game_choice(low, high), low, high)
        return print_guesses(guesses)

main()
        