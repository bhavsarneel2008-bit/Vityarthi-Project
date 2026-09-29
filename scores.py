def save_score(score):
    file = open("scores.txt", "a")
    file.write(score + "\n")
    file.close()

def show_scores():                            
    print("\n===== SCORE HISTORY =====")
    file = open("scores.txt", "r")
    data = file.read()
    if data == "":
        print("No scores saved yet.")
    else:
        print(data)
    file.close()

