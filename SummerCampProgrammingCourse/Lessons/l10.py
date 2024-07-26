# rock, scissors, paper game























# import random
#
#
# running = True
#
# ai_choice_dictionary = {
#     1: "rock",
#     2: "scissors",
#     3: "paper"
# }
#
# while running:
#     print("""
# 1. Rock
# 2. Scissors
# 3. Paper
# """)
#     choice = input('> ')
#     choice = int(choice)
#
#     ai_choice_number = random.randint(1, 3)
#     ai_choice = ai_choice_dictionary[ai_choice_number]
#
#     print(f"AI chose {ai_choice}.")
#
#     if choice == ai_choice_number:
#         print("It's a draw!")
#     elif choice == 1 and ai_choice == ai_choice_dictionary[2] or choice == 2 and ai_choice == ai_choice_dictionary[3] or choice == 3 and ai_choice == ai_choice_dictionary[1]:
#         print("You win")
#     else:
#         print("You lose")
