#FUNKCE PRO PŘEVOD TEXTOVÉHO ŘETĚZCE DO STRUKTURY LIST
def listNumber(seq):
    listNum = []
    seqSplit = seq.split() #tvorba seznamu na základě mezer
    for i in range(0, len(seqSplit)): #procházení jednotlivých prvků seznamu
        try:
            listNum.append(float(seqSplit[i])) #zápis do proměnné listNumber prvků typu int
        except:
            print("Špatný formát čísla na pozici", i + 1, "a proto bylo vynecháno.")
    return listNum

#FUNKCE PRO VYTVOŘENÍ SJEDNOCENÍ
def union(list1,list2):
    sum = sorted(list1 + list2) #uspořádaný seznam všech prvků dvou seznamů
    delRedundant = list(dict.fromkeys(sum)) #odstranění rededantních hodnot
    return delRedundant  

#SAMOTNÉ VOLÁNÍ FUNKCÍ
firstSeq = input("Zadej 1. posloupnost čísel oddělených mezerami: ")
listFirst = listNumber(firstSeq)

secondSeq = input("\nZadej 2. posloupnost čísel oddělených mezerami: ")
listSecond = listNumber(secondSeq)

#VÝSTUP
outputWithBrackets = union(listFirst, listSecond)
if (len(outputWithBrackets) == 0):
    print("\nBohužel jsi zadal dvě prázdné množiny")
else:
    print("\nSjednocením je:", *outputWithBrackets, sep = ' ') #odstranění krajcních závorek a definice mezery jako separátoru
        
