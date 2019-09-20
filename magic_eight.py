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
