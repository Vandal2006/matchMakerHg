# Henry Gilson
# Matchmaker_HG
#functions
def validateInput(userResponse) :
    print("Validateing Response")
    try:
        while userResponse <1 or userResponse >5:
            print(ERROR_MESSAGE)
            userResponse = int(input(QUESTION[i]))
            continue
    except ValueError:
        while userResponse <1 or userResponse >5:
            print(ERROR_MESSAGE)
            userResponse = int(input(QUESTION[i]))
            continue
# Constants
QUESTION_WIEGHT = [
    2,
    1,
    4,
    5,
    8
]
ERROR_MESSAGE = ("please enter an interger between 1 and 5")
QUESTION = [
    'Is wargame the best game ever made:',
    'Canada sucks:',
    'Does abusing your children make them better people:',
    'Having children seems like a good idea:',
    'Raising a family of horses whuld be highly enjoyable:'
]
DESIRED_RESPONSE = [
    5,
    1,
    5,
    1,
    5 
]
MAX_SCORE = 5 * len(QUESTION)
COMPATIBILITY_RANGE = [
    'Wow let get married!',
    'We should just be friends.',
    'Sorry this just isnt going to work out'
]
INTRODUCTION = '''
Matchmaker 2022
GilsoSoft, Inc

This program will find out how compatiable we whuld be as a couple.
Please enter an integer between 1 and 5, 5 being highly agree, 1 being strongly disagree
At the end of this you will see how comaptiable we are.
'''
print(INTRODUCTION)
# main loop
response = []
comaptablity = []
for i in range(len(QUESTION)):
    try:
        userResponse = int(input(QUESTION[i]))
        validateInput(userResponse)
        response.append(userResponse)
        questionCompatability = 5 - abs(userResponse - DESIRED_RESPONSE[i])
        questionCompatability = questionCompatability * QUESTION_WIEGHT[i]
        comaptablity.append(questionCompatability)
        print('Question %d Compatiblity %d\n' % (i+1, questionCompatability))
    except ValueError:
        print(ERROR_MESSAGE)
        userResponse = int(input(QUESTION[i]))
        validateInput(userResponse)#Says userResponse is not defined
#compatibility stuff
totalCompatibility = 0
for c in comaptablity:
    totalCompatibility += c
#totalCompatibility *= 100 / MAX_SCORE
print('Total Compatability: %d\n\n' % (totalCompatibility))
if totalCompatibility>85:
    print(COMPATIBILITY_RANGE[0])
if totalCompatibility>26 and totalCompatibility<84:
    print(COMPATIBILITY_RANGE[1])
if totalCompatibility<25:
    print(COMPATIBILITY_RANGE[2])