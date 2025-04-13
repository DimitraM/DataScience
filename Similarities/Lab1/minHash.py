import random
import readingDocs
def createRandomHash(p=2**33-355 , m=2**32-1):
    """
    Δημιουργεί ένα τυχαίο hash για n στοιχεία.
    
    :param p: Πρώτος αριθμός για το hash.
    :param m: Δεύτερος αριθμός για το hash.
    """
    a=random.randint(1, p-1)
    b=random.randint(0, p-1)
    return lambda x: ((a*x + b) % p) % m

def MyMinHash(document_sets, K, hash_functions):
    # Δημιουργία λίστας
    docsList = {}
    
    for docID, wordSet in document_sets.items():
        for wordID in wordSet:
            if wordID not in docsList:
                docsList[wordID] = []
            docsList[wordID].append(docID)

    # Δημιουργία του sig matrix
    numDocuments = len(document_sets)
    SIG = [[float('inf')] * numDocuments for _ in range(K)]

    # Υπολογισμός των hash values
    for wordID, docIDs in docsList.items():
        for docID in docIDs:
            for k in range(K):
                hash_value = hash_functions[k](docID)
                SIG[k][docID - 1] = min(SIG[k][docID - 1], hash_value)

    return SIG


# def MySigSim(docID1 , docID2, numPermutations) :
    