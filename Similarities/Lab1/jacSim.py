import time
def MyJackSimWithSets(A, B): 
    #Α,Β είναι frozen sets από την επιλογη του χρήστη
    intersectionSet = set()#set που κρατάω τις τιμες τους από την τομή των sets
    intersection_count = 0
    
    start_time = time.time()

    for i in A: 
        for j in B:
            if i == j:# Αν βρεθεί match τότε είναι στις τιμές της τομής
                intersectionSet.add(i)
                intersection_count += 1
                break  
    print("Πλήθος iterrations", intersection_count)
    unionAB= A.union(B) #Ενωση των δύο sets
    #Υπολογισμός του Jacard Sim
    if len(unionAB) > 0:
        jacSim = len(intersectionSet) / len(unionAB)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")  
        return jacSim
    else:
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")  
        return 0 
  

def MyJackSimWithOrderedList(A,B):
    pos1 = 0
    pos2 = 0
    intersection_count = 0
    intersectionSet = set()#set που κρατάω τις τιμες τους από την τομή των sets

    start_time = time.time()

    setA = sorted(A) # Ταξινόμηση του A
    setB = sorted(B) # Ταξινόμηση του B

    while pos1 < len(A) and pos2 < len(B):
        if setA[pos1] == setB[pos2]:
            intersection_count += 1
            intersectionSet.add(setA[pos1])
            pos1 += 1
            pos2 += 1

        elif setA[pos1] < setB[pos2]:
            pos1 += 1
        else:
            pos2 += 1
    print("Πλήθος iterrations", intersection_count)

    unionAB = A.union(B) #Ενωση των δύο sets
    # Υπολογισμός του Jacard Sim
    if len(unionAB) > 0:
        jacSim = len(intersectionSet) / len(unionAB)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")  
        return jacSim
    else:
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")  
        return 0
    



#testing

# A = frozenset(random.sample(range(1, 3001), 2000)) 
# B = frozenset(random.sample(range(1, 3001), 2000)) 

# D = frozenset(random.sample(range(1, 3001), 2000)) 
# E = frozenset(random.sample(range(1, 3001), 2000)) 

# intersection1 = MyJackSimWithOrderedList(A, B)
# print(f"Jaccard Similarity Ordered: {intersection1}")

# intersection2 = MyJackSimWithSets(D, E)
# print(f"Jaccard Similarity Unordered: {intersection2}")