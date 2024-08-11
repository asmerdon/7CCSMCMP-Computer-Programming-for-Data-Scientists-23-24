from binarysearchtree import BinarySearchTree
from linkedlist import LinkedList
import random
import time
import matplotlib.pyplot as plt


def randomTree(n): #creates a random tree with capacity n
    bst = BinarySearchTree(limit=n)
    for _ in range(n):
        bst.insert(random.randint(1,1000)) #populates with a random int between 1 and 1000
    return bst

X = [] 
for i in range(5,105,5): #create X with step of 5
    X.append(i)

def average(list): #function to get average of a list
    return sum(list)/len(list)

Y = [] #to store average means 

for val in X: #iterate through each step of 5
    avgList = []
    for i in range(0, 1000): #create 1000 random trees 
        tree = randomTree(val) 
        startTime = time.time() #get time before search
        tree.search(42)
        endTime = time.time() #get time after search
        elapsed = (endTime - startTime) * 1000 #calculate how long it took (converted to ms)
        avgList.append(elapsed) #add to list of search times 
    avgMean = average(avgList) #get average time taken
    print(f"Average time taken for tree size of {val}: {avgMean:.4f} ms.")
    Y.append(avgMean) #add to Y list

print(Y) #prints the list of means

#Plot X and Y
plt.plot(X, Y)
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

# Complexity analysis X vs Y:
# Assuming the tree is balanced, a BST has a logarithmic time complexity for searching for a value (O(log N)).
# This can be seen on the graph plotting X and Y, as the run time doesn't increase much despite the size of the BST increasing by 20x by the end.
# If the tree is not balanced however, the search time would be linear (O(N)).
# This is because it would have to search through each node to find the value, instead of being able to halve the search space at each node.
# Close figure to get figure 2.

# Calculate Y2 (linear prediction based off average times at 5 and 10)
t1 = Y[X.index(5)]  # average search time for n=5
t2 = Y[X.index(10)]  # average search time for n=10
c = (t2 - t1) / (10 - 5) # solving equations t = c ∗ n + b, difference in average search time / difference in tree size
b = t1 - 5 * c # intercept
Y2 = [c * n + b for n in X] # estimates search times for other tree sizes in X (t)

# I could not figure out how to calculate and plot Y3. A logarithmic relationship to the size of the tree (Y3) would plot a curve lower than the linear relationship (which would be a 45 degree line, as shown in Y2).

# Complexity analysis X vs Y, Y2, Y3:
# There could be a few reasons that Y does not follow the logarithmic Y3. Firstly, during the tests there may not be enough trees with 42 being created to give an accurate sample.
# This may impact how the graph is plotted, and how the logarithmic search times are calculated, with Y3 following a different curve to Y.
# When I run my code on this machine, there seems to be an issue where the first or second trees (5 or 10) end up taking longer to search than subsequent ones.
# To get closer to the line in Y3, we may want to increase the amount of testing we do to get better results.
# Changing the values of n may also give better predictions, as the time difference between n=5 and n=10 is so minimal when measuring the time that it can cause issues with the function (I get a much better looking plot for Y2 when I change n=10 to n=25).

#plot X and Y (and Y2 and Y3)
plt.plot(X, Y)
plt.plot(X, Y2)
#plt.plot(X, Y3)
plt.legend(['BST','Linear','Logarithmic'])
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

#linked list logic:
def randomLinkedList(n): #creates a random ll with capacity n
    ll = LinkedList(limit=n)
    for _ in range(n):
        ll.insert(random.randint(1,1000)) #populates with a random int between 1 and 1000
    return ll

Y4 = [] #to store average means 

for val in X: #iterate through each step of 5
    avgList = []
    for i in range(0, 1000): #create 1000 random linked lists 
        ll = randomLinkedList(val) 
        startTime = time.time() #get time before search
        ll.search(42)
        endTime = time.time() #get time after search
        elapsed = (endTime - startTime) * 1000 #calculate how long it took (converted to ms)
        avgList.append(elapsed) #add to list of search times 
    avgMean = average(avgList) #get average time taken
    print(f"Average time taken for tree size of {val}: {avgMean:.4f} ms.")
    Y4.append(avgMean) #add to Y list

print(Y4) #prints the list
#plot X and Y (and Y2 and Y4)
plt.plot(X, Y)
plt.plot(X, Y2)
#plt.plot(X, Y3)
plt.plot(X, Y4)
plt.legend(['BST','Linear','Linked List'])
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

# Complexity analysis X vs Y, Y2, Y3 and Y4:
# A linked list is has a linear time complexity for searching, unlike a BST, which has a logarithmic time complexity.
# The link list (Y4) follows the line of Y2, whilst the BST follows a logarithmic curve.
# This is because a linked list has to search node by node to find the value 42, whereas the BST can prune half of the search space at each node (if balanced).
# This makes it a much more efficient data structure for storing integers. 
