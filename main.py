filename = input("Enter the filename (include the file extension e.g .txt): ")
try:
    file = open(filename, 'r').readlines()
except IOError:
    print ("File", filename, "not found. Program terminates")
    exit()

# reading the file and saving the information to variables
numberOfStates = int(file[0])
initialState = int(file[1])
# we ignore the number of final states which would be file[2] because it's irrelevant
finalStates = file[3]
numberOfTransitions = int(file[4])
# the 3 following variable are not from the file
transitions = [] # is a list containing all transitions in string form
listOfFinalStates = [] # is a list containing all final states in string form
alphabet = [] # is a list containing all accepted letters

# filling the transitions list from the file
for i in range(0, numberOfTransitions):
    transitions.insert(i, file[i + 5])

# extracting the digits ignoring the spaces
finalStatesListIndex= 0
for i in finalStates.split():
    if i.isdigit():
        listOfFinalStates.insert(finalStatesListIndex, i)
        finalStatesListIndex += 1

# saving every letter from every transition
transitionLetters = ""
for i in range(0, len(transitions)):
    transitionCharacter = transitions[i]
    transitionLetters += transitionCharacter[1]

# putting all the unique letters in the variable "alphabet"
for i in range(0, len(transitionLetters)):
    if transitionLetters[i] not in alphabet:
        alphabet += transitionLetters[i]

transitionTable = [[0 for x in range(len(alphabet))] for y in range(numberOfStates)] # 2-dimensional table filled with 0

# filling the transition table
for i in range(0, numberOfTransitions):
    char1 = transitions[i][0]
    char2 = transitions[i][1]
    char3 = transitions[i][2]
    row = int(char1) - 1 # -1 because table indexing starts from 0
    col = ord(char2) - 97 # -97 to convert to ASCII
    value = int(char3)
    transitionTable[row][col] = value

while True:
    inputString = input("Enter a word: ")
    currentState = initialState
    wordNotInAlphabet = False # flag for letters out of the alphabet set

    for i in range(0, len(inputString)):
        character = inputString[i]
        if character not in alphabet:
            wordNotInAlphabet = True
            currentState = 0
            break
        row = currentState - 1
        col = ord(character) - 97
        currentState = transitionTable[row][col]

    # checking if the last state is in one of the final states and if the letters are in the alphabet set
    if currentState in map(int, listOfFinalStates) and not wordNotInAlphabet:
        print ("Word is accepted by the automaton")
    else:
        print ("Word is NOT accepted by the automaton")

    answer = input("Do you want to continue? Yes:y, No:n ")
    if answer in ['y','n']:
        if answer == 'y':
            continue
        elif answer == 'n':
            break
    else:
        print ("Unexpected input type \nProgram terminates")
        break