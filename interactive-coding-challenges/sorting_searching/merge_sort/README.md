## Problem: Implement merge sort.

* [Constraints](#Constraints)
* [Test Cases](#Test-Cases)
* [Algorithm](#Algorithm)
* [Code](#Code)
* [Unit Test](#Unit-Test)
* [Solution Notebook](#Solution-Notebook)

## Constraints

* Is a naive solution sufficient?
    * Yes
* Are duplicates allowed?
    * Yes
* Can we assume the input is valid?
    * No
* Can we assume this fits memory?
    * Yes

## Test Cases

* None -> Exception
* Empty input -> []
* One element -> [element]
* Two or more elements
* Left and right subarrays of different lengths


## Algorithm

Wikipedia's animation:
![alt text](http://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

* Recursively split array into left and right halves
* Merge split arrays
    * Using two pointers, one for each half starting at index 0
        * Add the smaller element to the result array
        * Increment pointer where smaller element exists
    * Copy remaining elements to the result array
    * Return result array

Complexity:
* Time: O(n log(n))
* Space: O(n)

Misc:

* Not in-place
* Most implementations are stable

Merge sort can be a good choice for data sets that are too large to fit in memory, as large chunks of data can be read and written to disk.

Unlike many other sorting algorithms, merge sort is not done in-place.

See: [Quicksort vs merge sort](http://stackoverflow.com/questions/70402/why-is-quicksort-better-than-mergesort)

