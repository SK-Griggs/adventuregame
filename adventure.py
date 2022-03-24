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


game_start ="yes"


while game_start =="yes":
    print(first_name, "I hear you  have finished your book. And you are ready for something else. Do you know what you want to read?")
    answer_1 = input("yes or no?   ")

    if answer_1 == "yes":
        print("You sound pretty confident. But I know you pretty well", first_name, "let's go look at your bookshelf. Do you see something you want to read?")
    else:
        print("This sounds like the perfect time to get out of the house. Do you want to go to the library?")
        library = input("yes or no?  ")
        while library == "no":
            print(first_name, "You're broke. You can't go to the bookstore. Do you want to go to the library?")
            library = input("yes or no? ")
        print("You grab the stack of overdue and unread library books and head to the library. You drive to the Northeast branch, it seems to always have the best selection. Do you see something you want to read? ")
    answer_2 = input("yes or no?  ")

    if answer_2 =="yes":
        print(first_name, "I am not sure why you teased me like this. If you already knew what you were going to read then you could have said so. ") 
        print("I don't think you're going to like the book you pick out though. ")
    else:
        print("This is where I get to work my magic. *Rubs digital hands together* Can I pick your next read?")
    answer_3 = input("yes or no? ")
    
    if answer_3 == "yes":
        print(first_name, "I have 16 titles picked out for you. Do you want to see what they are?")
    else:
        print(first_name, "You're killing me smalls! You don't see anything you want to read AND you don't want my help picking out your next read. Are you even a reader?")
        print("Your life is going to be pretty boring without a good book to read.")
    answer_4 = input("yes or no? ")
    
    if answer_4 == "yes":      
       print(df) 
       print("These are some good titles. I need to ask a few more questions though. Do you want to read a fantasy?")     
    else: 
        print("I am excited that you trust me that much. Do you want to read a fantasy?") 
    answer_5 = input("yes or no? ")

    if answer_5 == "yes":
       print(df.genre)
       print("You've really been into fantasy. I have 5 fantasy titles. Do you know what audience you're in the mood for? ")
    else:
        print("You do read a lot of fantasy. Maybe that's not the place to start. Do you know what audience you're in the mood for? ")
    answer_6 = input("yes or no? ")

    if answer_6 =="yes":
        print("I have my own recommendations,but first... Do you want to read an adult book? ")
    else:
        print(first_name, "I thought this was going to be easy. I mean you are a self-professed fantasy reader. But you suddenly don't want to read fantasy. That's not so bad. ")
        print("But, now you can't tell me what audience you're in the mood for? You know that even though you gravitate towards young adult, those books are the most unsatisfying books")
        print("So, my recommendation is that that you just take a reading break and come back when you are in the mood to read something.")
    answer_7 = input("yes or no? ")

    if answer_7 =="yes":
        print(df.audience)
        print(first_name, "You are in luck! That narrows it down to The Blood Trials by N.E. Davenport. ")
        print("The Blood Trials is 2022 release, and it's about a girl who has been hiding her magic. When her grandfather dies she wants revenge and answers. She enters into  trials that will risk her secrets being uncovered. ")
        print(df.loc[[3]])
    else:
        print("Do you want to read a middle grade book?")
    answer_8 = input("yes or no?")
    
    if answer_8 =="yes":
        print(first_name, "Another good choice! I have one middle grade fantasy for you. It's Pilar Ramirez and the Escape From Zara by Julian Randall. ")
        print("Pilar Ramirez is about a young girl who is sucked into a magical world and discovers her missing cousin.")
        print(df.loc[[6]])    
    else:
        print("Do you want to read a young adult book?")
    answer_9 = input("yes or no? ")

    if answer_9 =="yes":
        print(first_name, "I've narrowed it down to three titles, and honestly I think you'll enjoy them all. ")
        print(df.loc[[1]]) 
        print("Not Even Bones is about a girl who is forced to face the monster inside of herself. ")
        print(df.loc[[2]]) 
        print("She Who Rides the Storm is about 4 teens, a heist and a cursed shapeshifting sword.")
        print(df.loc[[13]])
        print("Only a Monster is a 2022 release about a girl who discovers that she comes from a family of monsters and the boy she's been crushing on is a monster slayer. ")
        print("She is then forced to work with a rival monster house to take down Nick.") 
    else:
        print(first_name, "I don't think you know what you're in the mood for. Maybe you should just take a reading break and come back when you're refreshed. ")
    game_start = input("Do you want me to help pick your next book?") 