# Mini Project 8: Voting System

votes = {"A": 0, "B": 0, "C": 0}

while True:
    vote = input("Vote (A / B / C or stop): ")
    if vote == "stop":
        break
    if vote in votes:
        votes[vote] += 1

winner = max(votes, key=votes.get)
print("Winner:", winner)