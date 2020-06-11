# Problem 1 - Explanation

## Strategy
The cache will be implemented so that:
* A dictionary will hold the key-value pairs
* A linked list will hold the count, using the same keys as in the dictionary
* The linked list will automatically rearrange its nodes with each new element added (set) or visited (get), to determine its LRU element
* This will make it very easy to remove the LRU element, simply by removing the head of the linked list every time the cache size reaches capacity

## Time and space Complexity:
The worst case scenario time complaxity is by iterating through the whole linked list compare frequency of used elements. In this case complexity will be **O(n)**. Everything else is constant time.

Space complexity is also **O(n)**, as it linearly increases with the cache input