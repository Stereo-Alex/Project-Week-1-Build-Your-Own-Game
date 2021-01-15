def cpu_function_range2():
    low = int(input("Set the lower limit of the game, this gives the computer a chance to narrow it down"))
    high = int(input("Set the higher limit of the game"))
    return low, high



def player_game(low, high):
    import random
    random_number = random.randrange(low, high)
    print(random_number)
    try_counter = 0
    print(f"the game has started, your scoreboard is at {try_counter}")
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
        print(f"you guessed right! The secret number was:  {random_number}")
        
    final_result = print(f"you guessed the number in {try_counter}, turns")    

    return final_result


low, high = cpu_function_range2()
player_game(low, high)



def pick_a_game():
    game_choice = input("Wellcome to the game, do you want to play yourself or make the computer play?"
                        ", if you want to play yourself please input 1, if you would prefer the computer to play then press 2")
    if game_choice == 1:
        return game_choice
    elif game_choice == 2:
        return game_choice 
