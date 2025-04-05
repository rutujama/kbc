questions = [
    ['What is the capital of India?', 'Mumbai', 'New Delhi', 'Chennai', 'Kolkata', 2],
    ['Who wrote the Mahabharata?', 'Valmiki', 'Ved Vyasa', 'Kalidas', 'Tulsidas', 2],
    ['What is the national animal of India?', 'Tiger', 'Lion', 'Elephant', 'Peacock', 1],
    ['Which planet is known as the Red Planet?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 2],
    ['What is H2O commonly known as?', 'Oxygen', 'Hydrogen', 'Water', 'Salt', 3],
    ['Which is the largest ocean?', 'Atlantic', 'Indian', 'Arctic', 'Pacific', 4],
    ['Who is known as the Father of the Nation?', 'Subhash Chandra Bose', 'Jawaharlal Nehru', 'Mahatma Gandhi', 'Sardar Patel', 3],
    ['Which organ purifies blood in the human body?', 'Heart', 'Kidney', 'Lungs', 'Liver', 2],
    ['Who was the first President of India?', 'Dr. Rajendra Prasad', 'Jawaharlal Nehru', 'Mahatma Gandhi', 'Sardar Patel', 1],
    ['In which year did India gain independence?', '1947', '1950', '1942', '1935', 1],
    ['Which gas is most abundant in the Earth’s atmosphere?', 'Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen', 3],
    ['Who invented the Telephone?', 'Thomas Edison', 'Alexander Graham Bell', 'Isaac Newton', 'Albert Einstein', 2],
    ['Which is the largest desert in the world?', 'Sahara', 'Thar', 'Gobi', 'Kalahari', 1],
    ['Who discovered Gravity?', 'Galileo', 'Newton', 'Einstein', 'Darwin', 2],
    ['Which is the smallest continent?', 'Australia', 'Europe', 'Antarctica', 'South America', 1],
    ['What is the boiling point of water?', '90°C', '80°C', '100°C', '120°C', 3],
    ['Which festival is known as the festival of colors?', 'Diwali', 'Christmas', 'Holi', 'Eid', 3]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]

i=0
money=0

for i in range(0,len(questions)):
    question=questions[i]
    print(f'\nQuestion for Rs.{levels[i]}')
    print(f' {question[0]}') 
    print(f'a. {question[1]}          b. {question[2]}')
    print(f'c. {question[3]}          d. {question[4]}')
    reply = int(input('Enter your answer (1-4): '))
    
    if(reply == question[-1]):
        print(f'Correct answer, you have won Rs.{levels[i]}')
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 7500000
        elif(i == 16):
            money = 75000000
    else:
        print('Wrong Answer')
        break   

print(f'Your take home money is Rs.{money}')
