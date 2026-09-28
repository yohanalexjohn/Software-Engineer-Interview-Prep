# Lowest Common Ancestor of a Binary Tree

## Prompt

Given a binary tree and nodes `p` and `q`, return their lowest common ancestor. This is not necessarily a BST, so there is no value ordering to follow.

## Approach

Use recursive DFS. Return the current node when it is null, `p`, or `q`. Search both children. If both sides return non-null, the current node is the split point and therefore the LCA; otherwise pass the one non-null result upward.

## Key invariant

A non-null return means this subtree contains a target or already found their LCA. Two non-null child results mean the targets split below the current node.

## Complexity

- Time: O(n).
- Space: O(h) recursion stack.

## Common mistakes

- Using BST comparisons on an unordered binary tree.
- Searching only until the first target is found.
- Forgetting that one target may be an ancestor of the other.

```cpp
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)
{
    if (root == nullptr || root == p || root == q) return root;
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left != nullptr && right != nullptr) return root;
    return left != nullptr ? left : right;
}
```
