sortingnr = [3,7,2,8,12,64,76,4]

def sortingsearching():
    print(sortingnr)
    for a in range(0, len(sortingnr)-1):
        for i in range(0, len(sortingnr)-1-a): #i is the index numbers
            if sortingnr[i] >= sortingnr[i+1]:
                sortingnr[i],sortingnr[i+1] = sortingnr[i+1], sortingnr[i] #swapping
            print(sortingnr)
        print()
sortingsearching()
    