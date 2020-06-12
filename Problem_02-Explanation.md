# Problem 2 - Explanation

## Strategy
A recursive function that:
* Checks for the file name within a folder
* Appends all the file it finds to a list
* Calls itself on the subfolders it finds until no more subfolders are found (basecase)
* Prints the list of found items

## Time and space Complexity:
The time complexity is depending on the number of files in each folder and number of folders, so **O(mn)**

Space complexity is also **O(mn)**, due to recursion stack.