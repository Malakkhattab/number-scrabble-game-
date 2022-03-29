def player1_input(available_numbers):
    player1_numbers = int(input(f"Player 1 Please choose a number from {available_numbers} "))

    if player1_numbers < 1 or player1_numbers > 9:
        player1_numbers = int(input(f"invalid number, Please choose another number from {available_numbers}"))

    if player1_numbers >= 1 and player1_numbers <= 9:
        for i in range(0, len(available_numbers)):
            while player1_numbers in chosen_numbers:
                player1_numbers = int(input(f"Number is already chosen, Please choose another number from {available_numbers}"))
            if player1_numbers == available_numbers[i]:
                player1_numbers_list.append(player1_numbers)
                chosen_numbers.append(player1_numbers)
                available_numbers.pop(i)
                available_numbers.insert(i, 0)
                break

def player2_input(available_numbers):
    player2_numbers = int(input(f"Player 2 Please choose a number from {available_numbers} "))

    if player2_numbers < 1 or player2_numbers > 9:
        player2_numbers = int(input(f"invalid number, Please choose another number from {available_numbers}"))
    if player2_numbers >= 1 and player2_numbers <= 9:
        for i in range(0, len(available_numbers)):
            while player2_numbers in chosen_numbers:
                player2_numbers = int(input(f"Number is already chosen, Please choose another number from {available_numbers}"))
            if player2_numbers == available_numbers[i]:
                player2_numbers_list.append(player2_numbers)
                chosen_numbers.append(player2_numbers)
                available_numbers.pop(i)
                available_numbers.insert(i, 0)
                break

def calculate_results():
    player1_results = 0
    player2_results = 0

    for i in range(len(player1_numbers_list)):
        player1_results += player1_numbers_list[i]
    for i in range(len(player2_numbers_list)):
        player2_results += player2_numbers_list[i]

    if player1_results == 15:
        print("player 1 win")

    if player2_results == 15:
        print("player 2 win")

    if player1_results != 15 and player2_results != 15:
        print("Draw")
        if len(available_numbers) != 0:
            player1_input(available_numbers)
            player2_input(available_numbers)
            available_numbers.clear()
            calculate_results()





available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chosen_numbers = []
turn_count = 0
player1_numbers_list = []
player2_numbers_list = []

while turn_count < 3:

    player1_input(available_numbers)
    player2_input(available_numbers)
    turn_count += 1
calculate_results()

