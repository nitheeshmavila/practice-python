import random
def quiz():
  capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston','Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

  for quiz_number in range(35):
    quizfile=open('Quiz_File_%d.txt' %(quiz_number+1),'w')
    quizfile.write('Name:\nDate:\nPeriod:\nState Capitals Quiz ,Form %d \n__________________________\n'%(quiz_number+1) )
 #  quizfile.close()
    answerfile=open('Answer_File_%d.txt' %(quiz_number+1),'w')
    answerfile.write('Answer key for quiz %d \n _____________________________________\n'%(quiz_number))
    states=capitals.keys()#states list
    random.shuffle(states)
    for i in range(50):
      quizfile.write('\n%d.Which is the capital of %s ?\n'% (i+1,states[i]) )
      answer=capitals[states[i]] 
      answerfile.write('%d.%s\n'%(i+1,answer))
      capital=capitals.values()
      capital.remove(answer)
      answer_options=[]
      capital=random.sample(capital,3)
      answer_options=capital+[answer]
      random.shuffle(answer_options)     
      quizfile.write(' A. %s \n B. %s \n C. %s \n D. %s \n'%(answer_options[0],answer_options[1],answer_options[2],answer_options[3]))
quiz()

