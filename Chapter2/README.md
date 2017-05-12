# 2.2 Analysis of Algorithms

**Algorithm Analysis**: Predicting the resources thatthe algorithmrequires. Typically computation time is prime concern but also can consider memory, communication bandwidth, or computer hardware.

Typically focus on worst-case running time of algoirithms because it provides an upper bound of running **any** input.

## Exercises
**2.2-1** 
Express the function n^3 / 1000 - 100n^2 - 100n + 3 in terms of Θ notation.

**Answer:**


Θ(n<sup>3</sup>)


**2.2-2**
Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element in A[1]. Then find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first n - 1
elements of A. Write pseudocode for this algorithm, which is known as selection sort. What loop invariant does this algorithm maintain? Why does it need to run
for only the first n - 1 elements, rather than for all n elements? Give the best-case and worst-case running times of selection sort in Θ notation.

**Answer:**

```
// Selection Sort(A)
for i = 0 to A.length - 1
	indexLowestValue = i
	// Find smallest value to insert at position 0
	for j = i + 1 to A.length
		if A[j] < A[indexLowestValue]:
			indexLowestValue = j
	// Insert smallest value into position i
	temp = A[i]
	A[i] = A[indexLowestValue]
	A[indexLowestValue] = temp

```

**Loop invariant:** The elements to the left of i are sorted.

It only needs to run for n - 1 elements because the last element can be assumed sorted.

Worst-case: Θ(n<sup>2</sup>)

Best-case: Θ(n<sup>2</sup>)

**2.2-3**
Consider linear search again (see Exercise 2.1-3). How many elements of the input sequence need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? What are the average-case and worst-case running times of linear
search in Θ notation? Justify your answers.

**Answer:**

Average n / 2 -->  Θ(n)
> If each element has equal likelihood of being the searched element, then the elemenet has an equal chance of being in the first half / second half of the array. Therefore On average it will require n / 2 checks.

Worst case n -->  Θ(n)
> The element is not in the array or is the last element in the array. This requires every element to be checked.


**2.2-4**
How can we modify almost any algorithm to have a good best-case running time?

The information known about the data can aid in picking an algorithm that is better suited to solving the problem.

# 2.3 Designing algorithms

**Incremental** Approach: F/e: insertion sort

**Divide and Conquer** Approach to Algorithms

Recursive algorithms typically follow a divide-and-conquer approach.

**Divide** the problem into subproblems of the same problem

**Conquer** the subproblems by solving them recursively.

**Combine** the solutions to the subproblems into the solution for the original problem.

Example: *Merge sort*. Divides sequence into subsequences of n/2 elements each. Then Sorts the subsequences. The combines and sorts to produce the sorted answer.

## Mergesort

**Divide**: The divide step just computes the middle of the subarray, which takes constant time. Thus, D(n) = Θ(n).
**Conquer**: We recursively solve two subproblems, each of size n=2, which contributes 2T(n=2) to the running time.**Combine**: We have already noted that the MERGE procedure on an n-element subarray takes time Θ(n), and so C(n) = Θ(n).

Worse-case: 
T(n) = Θ(n*lg(n))
