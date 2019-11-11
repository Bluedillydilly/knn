"""

"""
from numpy import linalg, array, argmin

def knn(training, labels, k, predictSet):
    """
        Parameters: 
            training - data samples that have been classified to labels
            labels -  the labels of the training data
            k - number of neighbos to *knock knock* check
            predictSet - set of points we want to classify
    """
    predicted = []
    for p in predictSet:
        distances = []
        for i in range(len(training)):
            distances.append((i,linalg.norm(p-training[i])))
        distances.sort(key=lambda pair: pair[1])
        distances = [labels[d[0]] for d in distances[:k]]
        predicted.append(max(distances, key=distances.count))
    return (predictSet, predicted)

if __name__ == "__main__":
    training = [[1,1], [1,2], [1,3], [50,1], [50,90], [50,10]]
    labels = [1,1,1,0,0,0]
    predict = [[0,0], [25,25], [50,50]]
    for k in range(5):
        print("Number of neighbors to check (K): ", k)
        print(knn(training, labels, k, predict))
