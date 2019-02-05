import random
import time
import sys
list = ["yes, most definately!","The chances are high!","Not likely!","May the odds be ever in your favour.","you got no shot, kid.","Try it out ans see!","15% of working","99.9% success rate","Congratulations, yes!","Ask a probably question","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Dont count on it"]

def userinput():
    question = 'Enter your question:'
    print(question)
    userQ = input("")

    print("\nThinking..\n")
    time.sleep(3)
    print(random.choice(list))

    result()

def result():
    print("would you like to ask another question?(yes or no)")
    user_reply = input('> ')
    while(input):
        if user_reply == "yes":
            userinput()
        
        else:
            print("Thanks for playing!")
            sys.exit(0)

print("Welcome to the magic 8 ball!")
userinput()

      

