# Choose Your Next Book

Hi and welcome to this unique text based choose your own adventure game. [adventure2.py]
This game is supposed to help narrow down a list of books that you are interested in reading. The total number of recommended books in the list is 16. Going through the prompts will narrow it to 1-3 titles.  And it works just like any other choose your own adventure, some answers will lead you to the next path/level and some will end. If the path ends, you will be asked if you want to play again. If you say yes, it will restart at the beginning of the game at level one. 
At the initial running of the game, you will be asked your name (which you will see pop up in the game at different times. )
It will also import the csv the game is using to make recommendations and importing pandas to display the csv file. 

THINGS YOU SHOULD KNOW ABOUT THE GAME:
It is not case sensitve but you do have to spell the words correctly. Meaning at each input you are given a word to type in as a response to a question. The appropriate words are in brackets.   
For example:
Do you want to read nonfiction/fiction? [nonfiction/fiction]
 You can type in fiction or Fiction to get the next response. 
 But if you type in faction, you will be kicked out of the game. 

 If you get to the end of a path, you will be prompted with the qustion "Do you want to play a bookish game? [yes/no]
 If you say yes, the game restarts. If you say no, you break the loop and are kicked out of the game. 


 ## SYSTEM REQUIREMENTS FOR GAME:
 -A virtual environment 
 -python 3.9.6 (at least)
 -pandas
 -to start the game in your virtual environment type in [python adventure2.py] in the command line


 ### WHAT FEATURES CAN BE FOUND (AND WHERE)
Cat 1. Implement a "master loop" console application where the user can repeatedly enter commands/perform actions, including choosing to exit the application.  (once the game begins it loops as long as you answer yes. entering no breaks the loop. misspelling words will also kick you out of the loop. )

Bonus Cat. 1. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. (The entire game is a series of functions that are called based on the input entered. )

Cat 2. Utlize External Data- read dat from an external file and use that data in your application. (The titles are from a csv file and the game narrows the list down to 1-3 titles. )

Cat. 3 Data display -display data on a tabular form. Depending on what you choose at level three you can see the entire table of title choices.  As you narrow the list down, individual rows are displayed offering more information about the book title. 



Thank you for taking the time to play Choose Your Next Book!