# Implement a function that groups identical items based on their order in the list

# Constraints

	* Can we use extra data structures?
		* Yes

# Test Cases

	* group_ordered([1, 2, 1, 3, 2]) -> [1, 1, 2, 2, 3]
	* group_ordered(['a', 'b', 'a']) -> ['a', 'a', 'b']
	* group_ordered([1,1,2,3,4,5,2,1])-> [1,1,1,2,2,3,4,5]
	* group_ordered([]) -> []
	* group_ordered([1]) -> [1]
	* group_ordered(None) -> None

# Algorithm: Modified Selection Sort

	* Save the relative position of the first-occurence of each item in a list
	* Iterate through list of unique items
		* Keep an outer index; scan rest of list, swapping matching items
		  with outer index and incrementing outer index each time

Complexity:

	* Time: O(n^2)
	* Space: O(n)


# Code: Modified Selection Sort


# Algorithm: Ordered Dict.

	* Use an ordered dict to track insertion order of each key
	* Flatten list of values.

Complexity:
	* Time: O(n)
	* Space: O(n)

# Code: Ordered Dict
