"""
Requirement: Given a binary tree, return an array representing the sums of all the branches
in the binary tree in order from left to right. In the example below,
you should return [32, 44, 48, 29, 31]
               5
           //    \\
         7         9
      //   \\    //  \\
     11     13   15   17
   //  \\   //
  19    21 23
Implementation: We traverse the tree starting from root, down the left nodes and right nodes.
As we do, we keep a running sum of the values of the nodes.
When we get to the leaf, we add the sum to the array that we will return.
Complexity: O(n) T because we visit each of the nodes to get to the leaf nodes and
add the sum to the array. O(n) S because each traversal to the leaf node will result
in log n as each call is limited to a branch at a single time.
However, if the tree is unbalanced and has one branch with n nodes,
then we have n branches on the stack thus O(n). Also consider that leaf nodes are always about ½
of the total nodes in the tree which is effectively O(n).
"""