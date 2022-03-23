#Choose Your Next Read
first_name =input("What is your name?  ")

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
            print("")#this is where book data comes in. -You  need to figure out selenium and see if it can scrape data from the library/the storygraph/goodreads. 
            #use yes or no questions to narrow down the genre and mood 
            #can you pull book data from the storygraph? << and then ask did you like this book?
            #can you pull book data from the library? << and ask have you read this book?
            #use the storygraph and goodreads to rank the top 5 books recommended.
        
        else:
            print(first_name, "You're killing me smalls! You don't see anything you want to read AND you don't want my help picking out your next read. Are you even a reader?")
            print("Your life is going to be pretty boring without a good book to read.")

    
game_start = input("Do you want me to help pick your next book?") 
