#Create Task - AP CSP

#Two-dimensional python array
cols_count = 10 #0, 1, 2 --> 3 questions per category
rows_count = 2 #0, 1 --> 2 categories
questions = [[0 for x in range(cols_count)] for x in range(rows_count)] 
answers = [[0 for x in range(cols_count)] for x in range(rows_count)]

#Initialize Array of selected numbers
alreadySelectedNumbers = []

#Define math questions
questions[0][0] = "(34+50/5)"
questions[0][1] = "Find the area of a rectangle with a height of 3 and a length of 5"
questions[0][2] = "Find the square root of 289"
questions[0][3] = "Find the probability that a year will have 367 days."
questions[0][4] = "A 'reunion of broken parts' is the meaning of the root of what word"  
questions[0][5] = "Estimate the total number of species and doves (You may not Google the answer)."
questions[0][5] = "Who are the 'Einsteins' of math in the bird world?"
questions[0][6] = "An ellipse is represented by the equation [x^2/36] + [y^2/16] = 1. What is the length of the major axis of this ellipse?"
questions[0][7] = "For a right triangle, the sin(A) is 3/5. To what value is the tan(A) equal? Answer as a decimal."
questions[0][8] = "What is the imaginary unit 'i' when raised to the power 10?"
questions[0][9] = "For which values of x from the set of real numbers does the following inequality hold: 4x + 5 < x + 11 "

#Define math answers
answers[0][0] = "44"
answers[0][1] = "15"
answers[0][2] = "17"
answers[0][3] = "0"
answers[0][4] = "algebra" 
answers[0][5] = "300"
answers[0][5] = "pigeons"
answers[0][6] = "12"
answers[0][7] = "0.75"
answers[0][8] = "-1"
answers[0][9] = "x<2"


#Define science questions
questions[1][0] = "Who is considered to be the father of the modern periodic table?" 
questions[1][1] = "What is the most abundant element in the Earth's atmosphere?" 
questions[1][2] = "A block of metal which weighs 60 newtons in air and 40 newtons under water has a density, in kilograms per meter cubed, of: " 
questions[1][3] = "What was the first organism to be genetically engineered?" 
questions[1][4] = "What is the protein that acts as a biological catalyst?" 
questions[1][5] = "Quartz commonly occurs in what type of crystal habit?"
questions[1][6] = "Which extinct shark was throught to be the largest on Earth?" 
questions[1][7] = "An agate is a form of what mineral?"
questions[1][8] = "What is the name of the white clay which has been used for thousands of years in the fabrication of ceramic bodies?" 
questions[1][9] = "A ball leaves a girl's hand with an upward velocity of 6 meters persecond. What is the maximum height of the ball above the girl's hand? Answer in meters." #1.8m

#Define science answers (these correspond to the science answers)
answers[1][0] = "Dmitri Mendeleev" 
answers[1][1] = "nitrogen" 
answers[1][2] = "3000" 
answers[1][3] = "tobacco" 
answers[1][4] = "enzymes"
answers[1][5] = "hexagonal"
answers[1][6] = "megalodon" 
answers[1][7] = "quartz"
answers[1][8] = "kaolin" 
answers[1][9]= "1.8"

#Import randint function from library
from random import randint

print("Hello! I'm happy you decided to check out this trivia game. Let's see how smart you are!") #Starting menu

start = input("Enter 's' to start the game! ")
if start == "s": #if 's' is pressed, game will start     
    print()
    print("Instructions: This trivia game will test you on your math and science knowledge! Each game will consist of 5 questions, on any category of your choice. You can play with the computer or practice yourself.")
    print("There will be no penalties for wrong answers. Be sure to capitalize all appropriate names.")
    print()
                   
    play = "y"
    
    def randomNumberGenerator(gameCategory): #Function to provide random numbers of questions from a specified game category without repeats
        generatorRunning = 1 
        while generatorRunning == 1:
            randomQuestionNumber = randint(0, len(questions[gameCategory]) - 1) #Create a random number of question to select
            if randomQuestionNumber not in alreadySelectedNumbers:
                generatorRunning = 0
                alreadySelectedNumbers.append(randomQuestionNumber)
                return randomQuestionNumber
    
    def computer(gameCategory): #Define the game played against a computer
        playAgain = "y"
        while playAgain == "y":
            alreadySelectedNumbers = [] #Clear the list of already chosen numbers
            roundCount = 1
            playerScore = 0
            computerScore = 0
            
            while roundCount <= 5: #ALGORITHM
                chosenNumber = randomNumberGenerator(gameCategory)
                print("Your turn to go. It is round", roundCount)
                print("Your score is", playerScore)
                print("The computer's score is", computerScore)
                print()
                print("You may enter '999' to quit.")
                print(questions[gameCategory][chosenNumber])#Print the question randomly from chosen category
                answer = input("Answer: ")
                print()
                if answer == answers[gameCategory][chosenNumber]:#If user's answer matches with answers logged in from computer, add one point to the user's score
                    print("You were correct!")
                    playerScore += 1
                elif answer == "999":
                    print("Your final score is", playerScore)
                    print()
                    playAgain = "n"
                    break
                else:
                    print("You were incorrect.")
                computerAnswer = randint(0, 1) #Randomly see if the computer is correct.
                if computerAnswer == 1:
                    print("The computer was correct!")
                    computerScore+= 1
                else:
                    print("The computer was incorrect.")

                print("Your score is", playerScore, "The computer's score is ", computerScore)#Final score statement
                print()
                print()
                
                roundCount += 1 #Move on to the next round
            if playAgain != "y":
                pass
            else:
                if playerScore > computerScore: #Establish who won/lost
                    print("Congratulations you won!")
                elif playerScore == computerScore:
                    print("It was a tie.")
                elif playerScore < computerScore:
                    print("Sorry, you lost.")

            print()
            playAgain = input("Would you like to play again? (y)es or (n)o ") #allows user to swtich game option (to practice or verse computer)
            print()     

    def practice(gameCategory): #Define practice game, Abstraction 
        playAgain = "y"
        while playAgain == "y": 
            alreadySelectedNumbers = [] #Clear the list of already chosen numbers
            roundCount = 1
            playerScore = 0
            
            while roundCount <= 5: #One round is 5 questions 
                chosenNumber = randomNumberGenerator(gameCategory)
                print("This is round: ", roundCount)
                print("Your score is", playerScore)
                print("You may press '999' to quit")
                print(questions[gameCategory][chosenNumber])#Print the question randomly from chosen category
                answer = input("Answer: ")
                if answer == answers[gameCategory][chosenNumber]:
                    print("You are correct!")
                    playerScore += 1
                elif answer == "999":
                    print("Your final score is", playerScore)
                    print()
                    playAgain = "n"
                    break
                else:
                    print("Sorry, you are incorrect.")
                print("Your current score is ", playerScore)

                print()
                roundCount += 1 #add 1 to the round number after each question 

            playAgain=input("Would you like to practice again? (y)es or (n)o? ")
            print()
 
    while play == "y": #While still playing, keep playing
        playAgain = "y"
        gameCategory = int(input("Pick a category: (0) Math, (1) Science or (999)Quit ")) #add categories here - these are game types
        if gameCategory == 999:
            quit()
        operation = input("Would you like to play against the (c)omputer, or (p)ractice? ")
        print()
        if operation == "c":
            computer(gameCategory) #Pass category chosen to the function
        if operation == "p":
            practice(gameCategory)
       
                
        
            
        
          
        
