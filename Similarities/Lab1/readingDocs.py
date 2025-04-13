
import jacSim as jacSim
import minHash as minHash
import time
def MyReadDataRoutine():
    print("Παρακαλώ επιλέξτε το αρχείο δεδομένων που θέλετε να συγκρίνετε (1 ή 2): \n  1. DATA_1-docword.enron.txt \n  2. DATA_2-docword.nips.txt \n ")
    chosenDoc = int(input("Επιλογή: "))

    if chosenDoc == 1:
        filePath = "DATA_1-docword.enron.txt"
    elif chosenDoc == 2:
        filePath = "DATA_2-docword.nips.txt"

    print("Παρακαλώ ορίστε το εύρος των αρχείων που θα διαβαστούν (π.χ. 0-100): ")
    rangeInput = input("Εύρος: ")
    start = int(rangeInput.split('-')[0])
    end = int(rangeInput.split('-')[1])
    document_sets = {} # Αρχικοποίηση του λεξικού για την αποθήκευση των σύνολων λέξεων
    try:    
        with open(filePath, 'r') as file:
            lines = file.readlines()
            doc = int(lines[0].strip())
            word = int(lines[1].strip())

            for i in lines[3:]: 
                parts = i.strip().split(' ')
                docId = int(parts[0])
                wordId = int(parts[1])
                #Αν το docId βρίσκεται στo εύρος που όρισε ο χρήστης τότε προσθέτουμε το wordId στο σύνολο
                if start <= docId <= end:
                    if docId not in document_sets:
                        document_sets[docId] = frozenset()
                
                    #Μετατρέπω το frozenset σε set για να μπορώ να προσθέσω το wordId
                    current_set = set(document_sets[docId]) 
                    current_set.add(wordId)
                    document_sets[docId] = frozenset(current_set)# Το μετατρέπω πάλι σε frozen set
                
    except FileNotFoundError:
        print(f"Το αρχείο {filePath} δεν βρέθηκε.")
        return None
    
    return document_sets

if __name__ == "__main__":
    result = MyReadDataRoutine()
    # Pretty print the result
    if result:
        print("===========================================================")
        print("Λεξικό Εγγράφων (Document Sets):")
        for doc_id, words in result.items():
            words_list = sorted(words)  # Sort the words for better readability
            print(f"Έγγραφο ID {doc_id}: {len(words_list)} λέξεις - {words_list}")
        print("===========================================================")   
    print("Επιλέξτε δύο έγγραφα για σύγκριση (π.χ. 1,2): ")
    selected_docs = input("Επιλογή: ")
    doc1, doc2 = map(int, selected_docs.split(','))
    #Α,Β είναι frozen sets από την επιλογη του χρήστη
    A = result[doc1]
    B = result[doc2]
    print("===========================================================")
    print("Jaccard Sim Unordered List: ", jacSim.MyJackSimWithSets(A,B))
    print("===========================================================")
    print("Jaccard Sim Ordered List: ", jacSim.MyJackSimWithOrderedList(A,B))
########################################################################################
    #Θα εκτελέσω και την MinHash αν το επιθυμεί ο χρήστης
    print("Θέλετε να εκτελέσετε MinHash; (y/n): ")
    choice = input("Επιλογή: ")
    if choice.lower() == 'y':
        print("Παρακαλώ εισάγεται το πλήθος των μεταθέσεων που θέλετε να δημιουργήσετε για κάθε μητρώο: ")
        W = int(input("Πλήθος μεταθέσεων: "))
        # Δημιουργία τυχαίων hash functions
        start_time = time.time()
        hash_functions = [minHash.createRandomHash() for _ in range(W)]
        # Υπολογισμός MinHash
        signature_matrix = minHash.MyMinHash(result, W, hash_functions)        
        print("Signature Matrix:")
        for row in signature_matrix:
            print(row)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")
        print("===========================================================")
    else:
        print("Ευχαριστώ! Τέλος προγράμματος.")