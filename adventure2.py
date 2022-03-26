#Choose Your Next Read
first_name =input("What is your name?  ")

import pandas as pd
df = pd.read_csv("cynb_selections.csv")

df.rename(columns={'Title ': 'title'}, inplace=True)
df.rename(columns={'Author ': 'author'}, inplace=True)
df.rename(columns={'Audience': 'audience'}, inplace=True)
df.rename(columns={'Genre ': 'genre'}, inplace=True)
df.rename(columns={'Pub Year ': 'pub_year'}, inplace=True)
df.rename(columns={'Keywords ': 'keywords'}, inplace=True)

def playagain():
    answer = input("Do you want to play a bookish game [yes/no]")
    if answer.lower().strip() == "yes":
        print("Let's see what new books can be discovered. ")
        levelone ()
    
    elif answer == "no":
        print("Well, it was fun talking to you, I hope you come back again. Goodbye.")

def levelone():
    print("Hey!", first_name, "My name is Book Guru, it's nice to meet you. I am here to make picking your next read a lot easier." )
    print("I know that a lot of readers have a list that they pick their next book from. But sometimes it's nice to have someone else pick or explore other recommendations. ")
    choice = input("Do you want to pick from a list or explore some recommendations? [list/explore] \n")

    if choice.lower().strip() == "list":
        print("While it's superfantastic that you are organized and have the discipline to stay focused on that. I am not sure that I can help you.")
        print("It was nice chatting with you though. ")
        playagain()

    elif choice.lower().strip() == "explore":
        print("Alright! Now we get to find out where our recommendations will come from!")
        leveltwo()

def leveltwo():
    print("There are so many places that you can find recommendations. It's all about preference, really.")
    print("I think that we should narrow down the option, and since I've gotten to know you pretty well,", first_name, "I know that you are a browser.")
    print("I know it's not just the cover that gets your attention, it's the size, the feel and the smell of the book. I have two places in mind.")
    choice = input("Do you want to go to the bookstore or the library? [bookstore/library]  \n")

    if choice.lower().strip() == "bookstore":
        print(first_name, "You're broke! You can't afford to buy books right now. And there's no shame in that.")
        print("Your financial guardian did ask me to remind you of that.")
        playagain()

    elif choice.lower().strip() =="library":
        print("Great choice", first_name, "! I was also supposed to remind you to grab the stack of library books that you need to return. ")
        levelthree()

def levelthree():
    print("I am glad that you picked the Northeast Regional Library. I know some people are not happy about the new building, but it does have the best selction of books. ")
    print("Now you can browse while I look to see if they have copies of the books that I want to recommend.")        
    print("Okay, I am back. I have my recommendations, but you look like you were having fun browsing. ")
    choice = input("Do you want to continue browsing or do you want to see my recommendations? [browse/recommendations]")

    if choice.lower().strip() == "browse":
        print("It was nice talking with you.  I am glad that I could inspire you to come to the library. Maybe we can do this again some time. ")
        playagain()

    elif choice.lower().strip == "recommendations":
        print(df)
        print(" I found 16 books that I think you will like. Now all we need to do is narrow down the choices. ")
        levelfour()

def levelfour():

#game start below
    levelone()
