import random
def get_user_guess():

    while True:
        try:
            guess=int(input("Enter your guess(2-200)"))
            if 2 <=guess<=200:
                return guess
            else:
                print("")
        except ValueError:
            print("invalide input. please enter a number between(2-200)")        

responses = [
    "Yes, definitely!",
    "No, not now.",
    "Ask again later.",
    "It is certain.",
    "Very doubtful.",
    "Outlook is good.",
    "Better not tell you now.",
    "Concentrate and ask again."
]

def get_random_response():
    global responses
    return random.choice(responses) 