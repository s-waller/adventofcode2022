import os,sys

rock_score = 1
paper_score = 2
scissors_score = 3

def hand_sign(type):
    match type:
        case "A" | "X":
            return "Rock"
        case "B" | "Y":
            return "Paper"
        case "C" | "Z":
            return "Scissors"

def score_increase(janken_play):
    match janken_play:
        case "Rock":
            return rock_score
        case "Paper":
            return paper_score
        case "Scissors":
            return scissors_score
 

lose_score = 0
draw_score = 3
win_score = 6
my_score = 0
opponent_score = 0


with open(os.path.join(sys.path[0], "input.txt"), "r") as file_content:
    lines = file_content.readlines()
    for i in lines:
        i = str(i).strip()
        opponent_hand_sign = hand_sign(i[0])
        my_hand_sign = hand_sign(i[-1])
        opponent_score += score_increase(opponent_hand_sign)
        my_score += score_increase(my_hand_sign)
        
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