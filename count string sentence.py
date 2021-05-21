OUT = 0
IN = 1

def countWords(string):
    state = OUT
    wc = 0
    for i in range(len(string)):
        if (string[i] == ' '):
            state = OUT
        elif state == OUT:
            state = IN
            wc += 1
            
    return wc
 

string = "My name is"
print("number of words  " + str(countWords(string)))
