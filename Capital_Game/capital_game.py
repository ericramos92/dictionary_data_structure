import random
#This all the states and capitals
dic = {'Alabama':'Montgomery', 'Alaska': 'Juneau', 'Arizona': '	Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': '	Denver ', 'Connecticut': 'Hartford', 'Delaware': '	Dover', 'Florida': 'Tallahassee ', 'Massachusetts': 'Boston',
       'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Michigan': 'Lansing',
       'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
       'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': '	Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': '	Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
       'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
       }
#accumulators for correct and incorrect answers
correct = 0
incorrect = 0
#status for while loop
status = True
#will run code inside until the players says no
while status:
       #the start of the game
       print("Guess the capital of the state")
       state = random.choice(list(dic.keys()))
       print("The state is "+ state)
       capital = input("Enter capital:")
       if capital.lower() == dic[state].lower():
              correct += 1
              print("You got the right answer")
              print("Correct = " + str(correct) + " Incorrect: " + str(incorrect))
              print("----------------------------")

       else:
              incorrect += 1
              print("You got the wrong answer")
              print("Correct = " + str(correct) + " Incorrect: " + str(incorrect))
              print("----------------------------")
       #Ask user if he/she wants to play
       game_decision = input("Do you still want to play? Y-(yes) or N-(no) ").upper()
       if game_decision == 'N':
              status = False


