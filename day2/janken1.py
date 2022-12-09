import os,sys

rock_score = 1
paper_score = 2
scissors_score = 3
lose_score = 0
draw_score = 3
win_score = 6
my_score = 0
opponent_score = 0


with open(os.path.join(sys.path[0], "input.txt"), "r") as file_content:
    lines = file_content.readlines()
    for i in lines:
        i = str(i).strip()
        opponent_hand_sign = i[0]
        match opponent_hand_sign:
            case "A":
                opponent_hand_sign = "Rock"
                opponent_score += rock_score
            case "B": 
                opponent_hand_sign = "Paper"
                opponent_score += paper_score
            case "C":
                opponent_hand_sign = "Scissors"
                opponent_score += scissors_score
            case _:
                exit
        my_hand_sign = i[-1]
        match my_hand_sign:
            case "X":
                my_hand_sign = "Rock"
                my_score += rock_score
            case "Y":
                my_hand_sign = "Paper"
                my_score += paper_score
            case "Z":
                my_hand_sign = "Scissors"
                my_score += scissors_score
            case _:
                exit
        
        if opponent_hand_sign == my_hand_sign:
            opponent_score += 3
            my_score += 3
        elif opponent_hand_sign == "Rock" and my_hand_sign == "Paper":
            my_score += 6
        elif opponent_hand_sign == "Rock" and my_hand_sign == "Scissors":
            opponent_score += 6
        elif opponent_hand_sign == "Paper" and my_hand_sign == "Rock":
            opponent_score += 6
        elif opponent_hand_sign == "Paper" and my_hand_sign == "Scissors":
            my_score += 6
        elif opponent_hand_sign == "Scissors" and my_hand_sign == "Paper":
            opponent_score += 6
        elif opponent_hand_sign == "Scissors" and my_hand_sign == "Rock":
            my_score += 6

winning_score = max(my_score,opponent_score)
losing_score = min(my_score,opponent_score)

if winning_score == my_score:
    winner = "me"
    loser = "the other guy"
else: 
    winner = "the other guy"
    loser = "me"
    
print ("The winner is " + winner + " with " + str(winning_score) + " points.")
print("The loser is " + loser + " with " + str(losing_score) + " points")