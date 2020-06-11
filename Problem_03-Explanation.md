# Problem 2 - Explanation

## Strategy
### A method that encodes:
* Adds all characters in a string to a dictionary, where key is character and value is frequency
* Creates nodes for each character in the dictionary
* Adds all nodes into a priority queue
* Joins nodes two by two, based on ascending frequency, until only one node is creating 
* Uses a helper method to get a dictionary for all leters used, which traverses a given tree
* Encodes and returns a binary message by using the dictionary

## A method that decodes:
* Inputs a tree and the binary message
* Uses another helper method that traverses the tree and returns the letters based on the binary message

## Time and space Complexity:
The time complexity in worst case scenario is for the binary function **O(nlog(n))**

Space complexity is also **O(nlogn)**