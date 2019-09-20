def ask_questions():
    x=input("What is your question?")
    return x
while (True):
    x=ask_questions()
    if x=="quit":
        break
    if x[-1]!='?':
        print("I’m sorry, I can only answer questions.")
        continue