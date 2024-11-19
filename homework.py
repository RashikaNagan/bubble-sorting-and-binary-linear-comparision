numbersbs = [2,6,5,3,8,21,35,64,75]
numbersls = [2,6,5,3,8,21,35,64,75]


def binarysearching(n):
    searches = 0
    numbersbs.sort()
    startingibs = 0
    endingibs = len(numbersbs)-1
    middleibs = (startingibs + endingibs) // 2
    while startingibs<= endingibs:
        middleibs = (startingibs+ endingibs) // 2
        if n == numbersbs[middleibs]:
                    return searches, middleibs
        elif n>= numbersbs[middleibs]:
                    startingibs = middleibs + 1
                    searches = searches + 1
        elif n<= numbersbs[middleibs]:
                    endingibs = middleibs - 1  
                    searches = searches + 1 
    return ("not found")
print(binarysearching(75))

def linearsearching(n):
    searchesls = 0
    for i in numbersls:
        searchesls = searchesls + 1
        if i == n:
            return("item found", searchesls)
            break 
    
    return("item not found", searchesls)    
print(linearsearching(75))

