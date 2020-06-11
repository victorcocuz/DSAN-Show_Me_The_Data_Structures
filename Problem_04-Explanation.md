# Problem 4 - Explanation

## Strategy
Use a recursive function to:
* Check if there are users in the group, or if the user itself is a group within another group
* Call itself on sub-groups

## Time and space Complexity:
The time complexity is depending on the number of users in each group and the number of groups, so **O(mn)**

Space complexity is also **O(1)**, as there is nothing stored