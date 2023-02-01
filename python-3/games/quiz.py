quizzes = [
    {
        'question': 'What is Biology?',
        'answer': 'A',
        'options': [
            'A. To study life',
            'B. To study plant',
            'C. To study animal',
            'D. None of the above'
        ]
    },
    {
        'question': 'What is 2 + 2?',
        'answer': 'B',
        'options': [
            'A. 2',
            'B. 4',
            'C. 10',
            'D. None of the above'
        ]
    },
    {
        'question': 'Who is the President of the Philippines?',
        'answer': 'A',
        'options': [
            'A. Ferdinand Marcos Jr',
            'B. Leni Robredo',
            'C. Isko Moreno',
            'D. None of the above'
        ]
    }
]

def start_quiz():
    score = 0

    for quiz in quizzes:
        print('---------------------------------------')
        print(quiz.get('question'))
        print('---------------------------------------')

        for option in quiz.get('options'):
            print(option)

        print('---------------------------------------')
        answer = input('Enter your answer: ').upper()
        score += 1 if (answer == quiz.get('answer')) else 0
    
    print('\nTotal Score: {score} out of {items}'.format(score=score, items=len(quizzes)))
    print('Score to Percent: {:.2f}%'.format(score / len(quizzes) * 100))

def new_game():
    response = input('\nAnother round of Quiz [yes]?: ').lower()

    return response == 'yes'

start_quiz()

while new_game():
    start_quiz()

print('********************')
print('{:^20}'.format('Quiz Game Done!'))
print('********************')
