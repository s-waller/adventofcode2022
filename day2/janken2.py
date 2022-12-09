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

def get_opponent_hand_sign(type):
    match type:
        case "A":
            return "rock"
        case "B":
            return "paper"
        case "C":
            return "scissors"

def get_my_hand_sign(response):
    match response:
        case "X": # lose desired
            if opponent_hand_sign == "rock":
                return "scissors"
            elif opponent_hand_sign == "paper":
                return "rock"
            elif opponent_hand_sign == "scissors":
                return "paper"
        case "Y": # draw desired
            return opponent_hand_sign
        case "Z": # win desired
            if opponent_hand_sign == "rock":
                return "paper"
            elif opponent_hand_sign == "paper":
                return "scissors"
            elif opponent_hand_sign == "scissors":
                return "rock"

def score_increase(janken_play):
    match janken_play:
        case "rock":
            return score_change["rock"]
        case "paper":
            return score_change["paper"]
        case "scissors":
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
        opponent_hand_sign = get_opponent_hand_sign(i[0])
        my_hand_sign = get_my_hand_sign(i[-1])
        opponent_score += score_increase(opponent_hand_sign)
        my_score += score_increase(my_hand_sign)
        
        if opponent_hand_sign == my_hand_sign:
            opponent_score += score_change["draw"]
            my_score += score_change["draw"]
        elif opponent_hand_sign == "rock" and my_hand_sign == "paper":
            my_score += score_change["win"]
        elif opponent_hand_sign == "rock" and my_hand_sign == "sissors":
            opponent_score += score_change["win"]
        elif opponent_hand_sign == "paper" and my_hand_sign == "rock":
            opponent_score += score_change["win"]
        elif opponent_hand_sign == "paper" and my_hand_sign == "scissors":
            my_score += score_change["win"]
        elif opponent_hand_sign == "scissors" and my_hand_sign == "paper":
            opponent_score += score_change["win"]
        elif opponent_hand_sign == "scissors" and my_hand_sign == "rock":
            my_score += score_change["win"]

print(outcome(my_score,opponent_score))