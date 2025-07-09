# Trees

Trees are a data structure that have a hierarchy structure. Here is an example.

Root (1)                                        1
    Parent (1,3)                              / | \
        Child (2,3,4 6,7)                    2  3  4
            Leaf (2,4,6,7)                     / \   
                Sibling (2,3,4 6,7)           6   7

## Binary Tree

Is a type of tree with a few rules. Each node can only have either zero or two nodes, and each child can only have one parent

     O
   /   \
  O     O
 / \   / \
O   O O   O

This is a Perfect Binary tree. Meaning that it is completely filled. By organizing data in this way the last row of data holds about half of the data. This type of data allows of Big O solutions with log(n) solution

## Binary Search Tree

I binary search tree is a subset of Binary tree. It's strengths is that is has good performance overall. As long as it is balanced. 

Rules:
1.) The value to the right of the node is always increasing
2.) A node can only have 2 children. 

## Binary Heap

Commonly used when ordering is important. They are structured such that the top node is always greater than any of the child nodes. these are really great at doing comparative iterations. Typically used in priority queues.

    101
   /   \
  72    32
 / \    / \
2  45  5   1

## Trie

Is a specialized tree most often used in searching. Typically with characters or strings. 

          Start
   /    /    \       \
  A     D      N     Z
 / \    |     / \    |
r   s   o    e   o   e
|       |    |   |   |
e       t    w   t   n
             |
             s