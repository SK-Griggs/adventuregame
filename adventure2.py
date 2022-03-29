#Choose Your Next Read
first_name =input("What is your name?  ")

#16 randomly selected titles to use for the game. 
import pandas as pd
df = pd.read_csv("cynb_selectionsA.csv")

df.rename(columns={'Title ': 'title'}, inplace=True)
df.rename(columns={'Author ': 'author'}, inplace=True)
df.rename(columns={'Audience': 'audience'}, inplace=True)
df.rename(columns={'Genre ': 'genre'}, inplace=True)
df.rename(columns={'Pub Year ': 'pub_year'}, inplace=True)
df.rename(columns={'Keywords ': 'keywords'}, inplace=True)


#function for the game
def playagain():
    answer = input("Do you want to play a bookish game [yes/no] \n")
    if answer.lower().strip() == "yes":
        print("Let's see what new books can be discovered. ")
        levelone()
    
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
    choice = input("Do you want to continue browsing or do you want to see my recommendations? [browse/recs] \n")

    if choice.lower().strip() == "browse":
        print("It was nice talking with you.  I am glad that I could inspire you to come to the library. Maybe we can do this again some time. ")
        playagain()


    elif choice.lower().strip() =="recs":
        print("I found 16 books that I think you are going to like.  ")
        print(df)
        levelfour()


def levelfour():
    print("Now we have to narrow down the list. Unless you want to take all sixtem books home with you. ")
    choice = input("Do you want to take all sixteen books home or do you want to narrow down the list? [all/narrow] \n")

    if choice.lower().strip() == "all":
        print("Well, I am glad that you are trusting me enough to think that every book I pick out is going to be a winner. This was kind of fun, maybe we can do this again, sometime")
        print("Maybe when you finish those books, you can come back and tell me how they were. Help me improve my recommendation process.")
        playagain()

    elif choice.lower().strip() == "narrow":
        print("Okay, now we have to figure out how to narrow down the list. ")
        levelfive()   


def levelfive():
    print("You have really been into fantasy. But I know that sometimes you get tired of it. Or maybe you simply get distracted by other books. ")
    print("But sometimes it's just about mixing things up. I completely understand, that's why I have a mix. ") 
    choice = input("Do you want something with or without romance in it? [with/without] \n")

    if choice.lower().strip() == "with":
        print("I have two titles tjhat you can choose from. Let's see if we can narrow it down even further.")
        levelsix()

    elif choice.lower().strip() == "without":
        print("That knocks out two titles. I think that you will probably want to stick with fantasy ")
        levelseven()
    


def levelsix():
    print("So you want something with romance in it. I know sometimes you are just in the mood for love. ")
    print("The question is how much love are you in the mood for?")
    choice = input("Do you want a book that is a straight up romance, enemies to lovers, or do you want a fantasy with a side of romance? [straight/side] \n")

    if choice.lower().strip() == "straight":
        print(" I have picked out The Worst Best Man for you. It's an enemies to lovers romance with a wedding planner and a marketing expert are forced to collaborate and impress a hotel client. ")
        print("Too bad they have bad history between them. This is a contemporary and it's supposed to be funny. ")
        print(df.loc[[12]])
        playagain()

    elif choice.lower().strip() == "side":
        print("I have picked out A Wolf After My Own Heart. It is the sequel to Bears Behaving Badly, a book that you enjoyed. ")
        print("You know it's going to be funny and it's going to have some sexytimes in it. ")
        print(df.loc[[1]])
        playagain()

def levelseven():
    print("So you are not in the mood for romance, or at least books where romance plays a big part.")
    print("We can also narrow the list down by the audience. ") 
    choice = input("Do you want to continue going through the list by genre or do you want to look at the audience for the book? [genre/audience] \n")

    if choice.lower().strip() == "genre":
        print("I guess the next thing you should think about is if you want to stick with fantasy or branch out.")
        leveleight()

    elif choice.lower().strip() =="audience":
        print("I know that you think that you want to pick based on the audience. But if I was to ask you what you thought about young adult, I'm pretty sure that you'd say you weren't really interested in it.")
        print("Or you would say that you're losing interent in it. But your shelves and lists say differently. I know, I peeked. Maybe you just need a break, and that's okay. ")
        playagain()

def leveleight():
    print(first_name, "You've had some time. Do you want to stick with fantasy or do you want to try something else?")
    choice = input("Do you want to read more fantasy or do you want to try something different? [fantasy/different] \n")

    if choice.lower().strip() == "fantasy":
        print("I have five titles that you can pick from. At this point, it might be easier to pick based on the audience. ")
        levelnine()

    elif choice.lower().strip() =="different":
        print("If you take away the romance and fantasy, that takes out 7 titles. ")
        levelten()

def levelnine():
    print(first_name, "So, you definitely want to stick with fantasy. And you are not interested in anything with romance as a focus.")
    choice = input("I have 5 fantasy titles that you can pick from, do you want to read an adult fantasy or a younger audience? [adult/younger] \n")

    if choice.lower().strip() == "adult":
        print("I only have one adult fantasy in my recommendations. It's the Blood Trials.  ")
        print(df.loc[[4]])
        print("The Blood Trials is about Ikenna who has secret blood magic and has been secretly learning martial skills. When she learns about her grandfather's death, she risks her life to particiapte in the trials. ")
        print ("She knows that his death wasn't natural and once she finds the killer she wants revenge.")
        playagain()

        
    elif choice.lower().strip() =="younger":
        print("There are still three titles to choose from. We need to narrow it down some more. ")
        leveleleven()
       
def levelten():
    print(first_name, "You don't want fantasy or romance. That leaves four other genres to pick from. ")
    choice = input("Do you want to read nonfiction or fiction? [nonfiction/fiction] \n")

    if choice.lower().strip() == "nonfiction":
        print("There is only one nonfiction title that I have to recommend. If I am not mistaken, you read the first book and already have plans to read this one. ")

        

    elif choice.lower().strip() =="fiction":
        print("If you take away the romance and fantasy, that takes out 7 titles. ")
        #leveltwelve()
      

def leveleleven():
    print(first_name, "I guess now you have to decide if you want to read middle grade or young adult?")
    choice = input("Do you want to read something young adult or middle grade? [young/middle] \n")

    if choice.lower().strip() == "middle":
        print("There is only one middle grade in my recommendations. It's Pilar Ramirez and the Escape From Zafa.  ")
        print(df.loc[[7]])
        print("Pilar Ramirez is about 12 year old Pilar who is dealing with a lot of change that she is not happy about. She is sucked into a blank page that leads her to the unknown world of Zafa. ")
        print("WHile here, Pilar finds her Abuela's cousin who has been missing for fifty years. She has to face the Domincan Boogeyman to free her cousin and to find her way home.  ")
        playagain()

    elif choice.lower().strip() =="young":
        print("I have three young adult fantasies that you may be interested in.  ")
        print("My first recommendation is one that I hear you have wanted to read for a while. It's Not Even Bones. ")
        print(df.loc[[2]])
        print("Not Even Bones is about Nita who dissects the bodies of the supernaturals that her mother kills. She aslso has nothing to do with selling their body parts on the black market. ")
        print("Until her mom brings home a live speciman. Nita (who is not exactly human)wants out. When she rescues the boy she finds herself being sold in his place. To escape, she may have to become the worst kind of monster. ")
        print("Next, there is  She Who Rides the Storm.")
        print(df.loc[[3]])
        print("She Who Rides the Storm is about four teenagers, a high stakes heist and a cursed sword of a shapeshifter. ")
        playagain()





        
        
        
    
                 


#game start below
levelone()
