# Problem 6 - Explanation

## Strategy
Create a linked list with a method that prepends elements from the provided lists.

### Create a union method
Declare a set and adds to the set each element from both lists.

Return a linked list created from the union set.

### Create an intersection method
Declare two sets:
* First set is temporary and adds each element from the first list
* Second set is for the intersection. Check if elements from the first list are in the temporary list. If so, add them to the intersaction

Return a link list created from the intersection set.

## Time and space Complexity:
The time complexity is depending on the number of items in the list **O(n)**

Space complexity is also **O(n)**, depending on the number of items in the list