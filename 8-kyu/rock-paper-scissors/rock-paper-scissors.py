def rps(p1, p2):
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if p1 == p2:
        return "Draw!"
    elif wins[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"