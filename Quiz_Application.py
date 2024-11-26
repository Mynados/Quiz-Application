import pickle
import os

# Make or take a quiz depending on answer.
user = str(input('Making a quiz or taking a quiz?(making/taking) \n'))
while user != 'making' and user != 'taking':
    print('Error')
    user = str(input('making or taking? \n'))

if user == 'making':
    n = int(input('How many questions would you like to add? \n'))
    Quiz = {}
    # Loops depending on the number inputted for n.
    for i in range(1,n+1):
        Q = str(input("Input your question. \n"))
        A = str(input("Input the answer to your question \n"))
        Quiz[Q] = A
    # Saves the dictionary to a pickle file for later use.
    with open("QuizApplication.pkl", "ab") as fp:
        pickle.dump(Quiz, fp)
        fp.flush()
    print("Saving the following quiz data:", Quiz)
if user == 'taking':
    try:

        with open("QuizApplication.pkl", "rb") as fp:
            Quiz = pickle.load(fp)
        for question, solution in Quiz.items():
            print(question)
            answer = str(input('Input your answer \n'))
            if answer.strip().lower() == solution.strip().lower(): # Makes the comparison case insensitive.
                print('Correct')
            else:
                print(f'Incorrect, the correct answer is {solution}')
        print(Quiz)
    except FileNotFoundError:
        print('No quiz found, please create a quiz first.')
        