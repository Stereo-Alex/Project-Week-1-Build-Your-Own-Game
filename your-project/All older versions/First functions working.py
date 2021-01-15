def game():
    import random
    random_number = random.randrange(-1, 9)
    print(random_number)
    try_counter = 0
    print("the game has started, your scoreboard is at", try_counter)
    player_guess = 0
    while player_guess != random_number:
        player_guess = int(input("Please enter your guess: "))
        if player_guess < random_number:
            print("Your guess is too low")
            try_counter = try_counter + 1
        if player_guess > random_number:
            print("Your guess is too high")
            try_counter = try_counter + 1
        else:
            print("you guessed right! The secret number was: ", random_number)

    final_result = print("you guessed the number in", try_counter, "turns")

    return final_result




def range_setter():
    range_of_game = []
    lower_range = int(input("what minimun value would you like to set? negatinve numbers are allowed"))
    higher_range = int(input("what maximun value would you like to set?"))
    range_of_game.append(lower_range)
    range_of_game.append(higher_range)
    return range_of_game





def computer_guess(num):
    low = 1
    high = 100
    guess = 50
    while guess != num:
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")
