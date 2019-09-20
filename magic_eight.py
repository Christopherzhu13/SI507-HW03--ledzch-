import random
def ask_questions():
    x=input("What is your question?")
    return x

def add_questions():
    num = random.randint(0, 9)
    answers = ["Reply hazy,try again.", "Ask again later.", "Better not tell you now", "Cannot predict now.",
               "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
               "Outlook not so good.", "Very doubtful."]
    print(answers[num])
