# Validate Binary Search Tree

## Prompt

Return whether a binary tree is a valid BST: every value in a left subtree is strictly smaller and every value in a right subtree is strictly greater.

## Approach

DFS while propagating the complete allowed interval. The left child receives `(low, node->val)` and the right child receives `(node->val, high)`.

## Key invariant

Every visited node must lie strictly inside the range imposed by all of its ancestors, not just its parent.

## Complexity

- Time: O(n).
- Space: O(h) recursion stack.

## Common mistakes

- Comparing only a node with its immediate children.
- Allowing duplicates accidentally.
- Using `int` sentinels and failing on `INT_MIN` or `INT_MAX`.

```cpp
bool valid(TreeNode* node, long long low, long long high)
{
    if (node == nullptr) return true;
    if (node->val <= low || node->val >= high) return false;
    return valid(node->left, low, node->val) && valid(node->right, node->val, high);
}

bool isValidBST(TreeNode* root)
{
    return valid(root, LLONG_MIN, LLONG_MAX);
}
```
