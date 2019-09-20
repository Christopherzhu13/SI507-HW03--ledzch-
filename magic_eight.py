import random
def ask_questions():
    x=input("What is your question?")
    return x

def pick_answer():
    a=random.randint(0,9)
    answer=["It is certain.","As I see it, yes","It is decidedly so.","Without a doubt."
            ,"yes - definitely.","You may rely on it.","Most likely","Outlook good.","Yes","Signs point to yes."
           ]
    print(answer[a])

def add_questions():
    num = random.randint(0, 9)
    answers = ["Reply hazy,try again.", "Ask again later.", "Better not tell you now", "Cannot predict now.",
               "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
               "Outlook not so good.", "Very doubtful."]
    print(answers[num])
while (True):
    x=ask_questions()
    if x=="quit":
        break
    if x[-1]!='?':
        print("I’m sorry, I can only answer questions.")
        continue
    b=random.randint(1,2)
    if b==1:
        pick_answer()
    else:
        add_questions()
