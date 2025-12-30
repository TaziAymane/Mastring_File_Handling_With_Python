# Exircice 1
# notes = [12,23,24,23,45,45]
# # afficher la list 
# print(notes)
# # ajouter 
# notes.append(16)
# print(notes)
# # supprimer
# notes.pop(2)
# print(notes)
# notes.remove(12)
# print(notes)
# #  boucle 
# for i in notes :
#     print(i)    
# Exrcice2

# numbers = [12,23,24,23,45,45]
# numbers.sort()
# print(numbers[0])
# print(numbers[-1])
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

#Exrcice 2 
# L = [1,1,2,2,3,4,3,4,3,]
# print(L)
# L.reverse()
# print(L)

# Methode 1
# L2 = [1,1,2,2,3,4,3,4]
# list_result = list(set(L2))
# print(list_result)

# Methode 2
# result = []
# for i in L2 :
#     if i not in result :
#        result.append(i)
# print(result)
# Exercice 3
listPairs = []
for i in range (21) :
    if (i%2 == 0):
        listPairs.append(i)

print(listPairs)
