import os,sys

score_change = {
  "rock": 1,
  "paper": 2,
  "scissors": 3,
  "lose": 0,
  "draw": 3,
  "win": 6
}

my_score = 0
opponent_score = 0

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
            return score_change["rock"]
        case "Paper":
            return score_change["paper"]
        case "Scissors":
            return score_change["scissors"]

def outcome(my_total,opponent_total):
    if my_total == max(my_total,opponent_total):
        return "I win with " + str(my_total) + " points. The opponent scored " + str(opponent_total) + " points."
    elif opponent_total == max(my_total,opponent_total): 
        return "The elf wins with " + str(opponent_total) + " points. I scored " + str(my_total) + " points."
    elif my_total == opponent_total:
        return "The scores are tied at " + str(my_total) + " points."

with open(os.path.join(sys.path[0], "input.txt"), "r") as file_content:
    lines = file_content.readlines()
    for i in lines:
        i = str(i).strip()
        opponent_hand_sign = hand_sign(i[0])
        my_hand_sign = hand_sign(i[-1])
        opponent_score += score_increase(opponent_hand_sign)
        my_score += score_increase(my_hand_sign)
        
        if opponent_hand_sign == my_hand_sign:
            opponent_score += score_change["draw"]
            my_score += score_change["draw"]
        elif opponent_hand_sign == "Rock" and my_hand_sign == "Paper":
            my_score += score_change["win"]
        elif opponent_hand_sign == "Rock" and my_hand_sign == "Scissors":
            opponent_score += score_change["win"]
        elif opponent_hand_sign == "Paper" and my_hand_sign == "Rock":
            opponent_score += score_change["win"]
        elif opponent_hand_sign == "Paper" and my_hand_sign == "Scissors":
            my_score += score_change["win"]
        elif opponent_hand_sign == "Scissors" and my_hand_sign == "Paper":
            opponent_score += score_change["win"]
        elif opponent_hand_sign == "Scissors" and my_hand_sign == "Rock":
            my_score += score_change["win"]

print(outcome(my_score,opponent_score))