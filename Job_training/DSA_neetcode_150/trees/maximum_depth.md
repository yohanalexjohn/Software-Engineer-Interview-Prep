# Maximum Depth of Binary Tree

## Prompt

Given a binary-tree root, return the number of nodes on the longest path from the root to a leaf.

## Approach

Use post-order DFS. An empty subtree has depth `0`; a non-empty subtree has depth `1 + max(leftDepth, rightDepth)`.

## Key invariant

Each recursive call returns the correct maximum depth of the subtree rooted at its argument.

## Complexity

- Time: O(n).
- Space: O(h) recursion stack; O(n) for a completely skewed tree.

## Common mistakes

- Returning `1` for `nullptr`.
- Counting edges when the prompt expects nodes.
- Saying O(log n) space without knowing the tree is balanced.

```cpp
int maxDepth(TreeNode* root)
{
    if (root == nullptr) return 0;
    return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
}
```
