#FUNCTION TO CHECK INPUT AND CONVERT TRING TO LIST
def listNumber(seq):
    listNum = []
    seqSplit = seq.split() #make list based on space seoaratir
    for i in range(0, len(seqSplit)): #step through the list
        try:
            listNum.append(float(seqSplit[i])) #convert to float
        except ValueError:
            print("Wrong number format at position", i + 1, ", it is reason, why it doesn't used in calculation.") #value skip in case of wrong format
    return listNum

#FUNCTION FOR ASCENDING SORTING OF LIST VALUE
def sortASC(inputList):
    for i in range(len(inputList)): #browsing list indexes
        minIndex = i
        for j in range( i + 1, len(inputList)): #browsing list indexes except i position
            if inputList[minIndex] > inputList[j]: #finding the lowest value
                minIndex = j 
        inputList[i], inputList[minIndex] = inputList[minIndex], inputList[i]
    return inputList

#UNION FUNCTION
def unionFunction(list1,list2):
    m, n = len(list1), len(list2)
    i, j = 0, 0  
    out = []
    prev = None #variable using for presious value (checking duplicate values)
    while i < m and j < n: #loop exists, when i,j is lower than size of list1 and list2
        if list1[i] < list2[j]:
            if list1[i] != prev:
                out.append(list1[i])
                prev = list1[i]
            i += 1 #increase of variable for reading value in list1
        elif list2[j] < list1[i]:
            if list2[j] != prev:
                out.append(list2[j])
                prev = list2[j]
            j += 1 #increase of variable for reading value in list2
        elif list2[j] == list1[i]: #append value, if list1 and list2 have the same value
            if list2[j] != prev:
                out.append(list2[j])
                prev = list2[j]
            i += 1 
            j += 1
    
    while i < m: #append remaining values of larger list1
        if list1[i] != prev:
            out.append(list1[i])
            prev = list1[i]
        i += 1
    while j < n: #append remaining values of larger list2
        if list2[j] != prev:
            out.append(list2[j])
            prev = list2[j]
        j += 1
    return out

#INPUT AND SORT LIST
firstSeq = input("Input first sequence of numbers separated by spaces: ")
listFirst = sortASC(listNumber(firstSeq))
secondSeq = input("\nInput second sequence of numbers separated by spaces: ")
listSecond = sortASC(listNumber(secondSeq))

#UNION
res1 = unionFunction(listFirst, listSecond)

#OUTPUT
if (len(res1) == 0):
    print("\nI am sorry, but you inputed two empty sequences.")
else:
    print("\nUnion is:", *res1, sep = ' ') #remove brackets from list and make space as separator
     
