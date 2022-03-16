"""
7 is not base case
7 = fib(5), fib(6)...up to the base case
Visualise this as a tree
Because the levels are equivalent of n, and at each level, the nodes increase by double
We know that the time complexity is O(2**n)
The space complexity is O(n) because we only even have stacks equivalent to n at max
The fibonacci is a good example of a dynamic problem because we see a pattern of duplicate
trees solving the fibonacci.
Memoization is one of the overarching that helps resolve problems using dynamic programming
with memoization, we store the values we have calculated
With memoization, include the memo in the visualisation, showing that in the first instance, the
first branch will calculate the fib, but subsequent calls to fib will use the memoized value

"""


def fib_recursive(n):
    if n <= 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memoization(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]


"""
Travel down a 2D grid from top left corner to the bottom right corner. 
You can only travel down or right. 
In how many ways can you travel to the goal on a grid with dimensions of m * n
Rectangle not necessarily a square
visualise some simple example
grid_traversal(2,3) => 3
grid_traversal(1,1) => 1 - Do nothing as you are already at the bottom right
grid_traversal(0,1) => 0 - invalid as the grid is zero
if any of the dimensions is zero then there's no path to traverse
grid_traversal(3,3) => 3
Every step towards the bottom right shrinks our problem and grid towards the base case of (1,1)
Every times, structure the problem as a tree to visualise
grid_traversal(2,3) => 3
knowing the result of a simple examples, we can visualise our logic
We know that going down the tree, we have made known decisions of either traversing right or down
and we know the resulting count of ways to the base case
We know we can only either go a step down or a step right which means -1
So every node branches down and right
Time complexity O(2 ** (n+m))
Space is the height of the tree which is O(n+m)
So the issue is the n+m exponent
Pick out the duplicate work
With a brute force solution and recursion, memoization becomes easier
By memoizing, we have reduced our time complexity to O(m * n) and space complexity of O(m+n)
"""


def traverse_grid(m, n, memo=None):
    # Are the arguments in the memo
    if memo is None:
        memo = {}
    key = str(m) + "-" + str(n)
    if key in memo:
        return memo[key]
    if 0 in (m, n):
        return 0
    if m == 1 and n == 1:
        return 1
    memo[key] = traverse_grid(m - 1, n, memo) + traverse_grid(m, n - 1, memo)
    return memo[key]


"""
Write a function that takes in a target sum and an array of numbers as arguments. 
The function should return a boolean indicating whether or not it is possible 
to generate the target sum using numbers from the array. 
You may use an element of the array as many times as needed. 
You may assume that all input numbers are nonnegative.

Taking a simple example, we know that if we subtract 7 away from our target, 
the result will be zero and 4 will result in three of which we can take away 3 
available to us in the array, resulting in  0. 
All the cases which result in a zero are base cases with a positive result 
while any with a remainder means that we could not arrive at the base case of zero 
and thus are a false result. 
The question however, is just looking for a single true. 
So we can return a true soon as we know it’s feasible.

m - target sum
n - length of the array we are given
What is the depth of the tree, this would be m as you have to subtract 1 in the 
 worst case scenario all the way down the tree to the value of m. This is the height of the tree.
 What is the branching factor or breadth of the tree at each level? Every target value could potentially 
 be made up of n factors - all of the factors in the array.
 Time complexity is thus O(n ** m)
 Space complexity will be O(m) the height of the tree
 With the memoized version, the complexity is cut down by our values stored in the memo
 So we never have to go beyond the target sum up to the number of nodes in our array.
 O(m*n)
Space complexity will remain O(m), the height of the tree
"""


def can_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum in numbers:
        return True
    if target_sum == 0:
        return True

    if target_sum < 0:
        return False
    for n in numbers:
        remainder = target_sum - n
        if can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


"""
In this case, we take a target sum and an array of numbers as arguments. 
We should return an array containing any combinations of elements that add up to 
exactly the target sum. If there is no combination that adds up to the target sum, 
we return null. If there are multiple combinations, then we just return one of them.
The implementation in this case is similar to can sum. However, we need to return an array of 
possible combinations. The brute force implementation returns the result array after appending 
the result when we find a non-null result.
This has a time complexity of O(n**m *m) and space complexity of O(m) for space.
We then memoize it and the new solution has a
Time complexity of O(n * m**2)
and a space complexity of O(m**2) 
"""


def how_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for n in numbers:
        remainder = target - n
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            memo[target] = [*remainder_result, n]
            return memo[target]

    memo[target] = None
    return None


"""
In this case we need to find the best way to get to the target value
The sub problems are to find the best way to get to constituents of the target sum
m is the target sum
n is the size of numbers

The brute force solution 
time : O(n ** m * m) but we also have the possibility that the combination is made up of 
1s which add up to m, hence * m
space: O(m**2) we use at least m the height of the tree, however, we are storing a shortest combination
for each iteration hence m **2 are maintaining
When we add memoization, we have the following complexity:

time: O(m ** 2 * n) - This is coming from running best_sum for target value for each combination
of numbers and in addition updating the array with new combination in each iteration which is a linear
operation.
space: O(m ** 2) because the memo uses keys of the target but the value could be an array of length m
 in worst case scenario
"""


def best_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for n in numbers:
        remainder = target - n
        remainder_combination = best_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = [*remainder_combination, n]

            # if the combination is shorter, then update shortest
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target] = shortest_combination
    return shortest_combination


"""
Write a function that accepts a target string and an array of strings and returns a boolean
indicating whether or not the target word can be constructed from elements of the word bank array.
You may use elements of the word bank array as many times as you wish.
knowing that the array of words will not changing, we take the target string.
We know we need to shrink the target string as we go using the array of strings from we have.
So we check for any elements that match the prefix of the word we want to construct
or suffix and then recursively check for other prefixes and suffixes until we get to the empty
base case or arrive at an element that is not in the array. 
"""


def can_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}

    if target == '':
        return True

    if target in memo:
        return memo[target]

    for word in word_bank:
        word_length = len(word)
        if target[:word_length] == word:
            if can_construct(target[word_length:], word_bank, memo):
                memo[target] = True
                return True

        # if target[:word_length] == word:
        #     if can_construct(target[:word_length], word_bank):
        #         return True
    memo[target] = False
    return False


"""
Write a function that accepts a target string and an array of strings and 
determines how many ways the target string can be constructed from the elements 
in the array of strings. You may use the elements in the array as many times as needed.
If we arrive at the end of our iterations with a string that cannot form the target string, 
we should return 0. However, if we arrive at an empty string we should return 1 
to indicate that the target string could be constructed.
"""


def count_construct(target, word_bank, memo=None):

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == '':
        return 1

    total_count = 0
    for word in word_bank:
        word_length = len(word)
        if target[:word_length] == word:
            ways = count_construct(target[word_length:], word_bank, memo)
            total_count += ways

        memo[target] = total_count
    return total_count


"""
Create a function that will receive a target string and an array of strings, and return 
an array with all the different combinations from the array of the string that can form 
the target string. You may reuse the elements of the array as many times as possible.
If there are no ways to generate the target string, then we return an empty array [].
However, if we receive an empty string, we know we can always generate an empty string, 
so we return an array of an empty array [[]]
We optimise this solution with memoization even though this doesn't improve the time complexity 
given that we have to go through the whole array to find all possible combinations to make the 
target string.
"""


def all_constructs(target, words, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]

    def add_word (word, ways):
        for way in ways:
            way.append(word)
        return ways

    constructs = []
    for word in words:
        if target[:len(word)] == word:

            remainder = target[len(word):]
            suffix_ways = all_constructs(remainder, words, memo)
            target_ways = add_word(word, suffix_ways)
            # memo[target] = target_ways
            constructs.extend(target_ways)

    memo[target] = constructs
    return constructs
