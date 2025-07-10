## Recursion

Is a common concept used to refer a function within itself. These are really good for repeated tasks, such as traversing a tree.

# Concerns

When working with recursion it can potentially cause a stack overflow issue. This can be dangerous since infinite loops can occur. The downside is that it also can take up more memory. 

the big O of recursion could be exponential issue. 2^n

# Mitigation

Creating a base case. 

# best use case

When traversing a tree or converting something into a tree. 

1.) Divided into a number of sub-problems that are smaller instances of the same problem
2.) Each instance of the subproblem is identical in nature.
3.) The solutions of each subproblem can be combined to solve the problem at hand