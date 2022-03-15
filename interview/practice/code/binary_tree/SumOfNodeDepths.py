"""
Requirement: Given a binary tree, return the sum of the depths of the nodes in the tree.
For example the tree below should return a depth of 19 made up of the depths as follows:
7-1, 9-1, 11-2, 13-2, 15-2, 17-2, 19-3, 21-3, 23-3, 1+1+2+2+2+2+3+3+3 = 19

                  5
             //      \\
            7          9
        //     \\     //  \\
       11       13   15   17
    //   \\    //
   19     21   23

Implementation: We traverse the tree and as we do, we pass down the depth of the next level
as the parent nodes know the depth of their children. We then return the sum of all the nodes.
Complexity: O(n) T O(h) S as we visit each node and the maximum number of calls on the stack
will be the height of the tree at most.
"""