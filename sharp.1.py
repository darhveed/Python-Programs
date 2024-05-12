# A pop quiz using python
questions = ("How many days are in a leap year?:",
             "How many numbers makes 5 dozens?:",
             "When did Nigeria become a republic?:"
             "When did Nigeria gain Independence?:"
             "When is Democracy day?:")
options =   (("A. 365","B. 360","C. 366","D. 363"),
             ("A. 12", "B. 52", "C. 58", "D. 60"),
             ("A. 1st Oct 1960", "B. 1st Oct 1963","C. 1st Oct 1965","D. 27th May 1960")
             ("A. 1st Oct 1960", "B. 1st Oct 1963","C. 1st Oct 1965","D. 27th May 1960")
             ("A. 27th May", "B. 29th May", "C. 12th June", "D. 1st Oct"))
# Actually the code will run if you use this dictionary form...
# But it won't bring out the other options.

# questions2 = {
#     "How many days are in a leap year?:": {
#         "options": ("A. 365","B. 360","C. 366","D. 363"),
#         "answer": "c",
#         "response": ""
   
#     }
   
# }   

answers =   ("C","D","B","A","C")
guesses = []
score = 0 
question_num = 0 
for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)
   

    guess = input("Enter(A ,B ,C , D): ").upper().strip()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")   
    else :
        print("INCORRECT!")
        print(f'{answers[question_num]} is the correct answer.')
        print('You can do better.')
    
    question_num += 1
print('---------------')
print('RESULTS')
print('---------------')
print("answers:", end =  " ")
for answer in answers:
    print(answer, end = " ")
print()
print("guesses:", end =  " ")
for guess in guesses:
    print(guess, end = " ")
print()

score= int(score/len(questions) * 100)
print(f"Your score is: {score}%")