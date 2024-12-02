def main():
    list1 = []
    list2 = []
    
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            list1.append(words[0])
            list2.append(words[1])
            
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    distances = find_distances(list1_sorted, list2_sorted)
    print("Similarity score: " + str(similarity_score(list1_sorted, list2_sorted)) + ", Sum of distances: " + str(sum_distances(distances))) 

def find_distances(list1, list2):
    distances = []
    for i in range(len(list1)):
        distances.append(abs(int(list1[i]) - int(list2[i])))
    return distances

def sum_distances(distances):
    return sum(distances)

def similarity_score(list1, list2):
    total_score = 0
    for i in range(len(list1)):
        similiraty_score = int(list1[i]) * list2.count(list1[i])
        total_score += similiraty_score
    return total_score

main()