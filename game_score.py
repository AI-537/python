player_name = input("Enter the player's name: ")
games_played = int(input("Enter the number of games played: "))
total_score = int(input("Enter the total score achieved: "))
average_score = total_score / games_played
print(f"Player Name: {player_name}")
print(f"Games Played: {games_played}")
print(f"Total Score: {total_score}")
print(f"Average Score per Game: {average_score:.2f}")