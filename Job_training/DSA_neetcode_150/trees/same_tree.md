# Same Tree

## Prompt

Return whether two binary trees have identical structure and equal values at corresponding nodes.

## Approach

Use DFS on node pairs. Two null nodes match; exactly one null node does not; otherwise values and both child pairs must match.

## Key invariant

Each call answers whether the two subtrees rooted at its arguments are identical.

## Complexity

- Time: O(n).
- Space: O(h) recursion stack.

## Common mistakes

- Dereferencing before handling nulls.
- Comparing values but not structure.
- Using `p == q` as a general equality test; it only compares addresses.

```cpp
bool isSameTree(TreeNode* p, TreeNode* q)
{
    if (p == nullptr && q == nullptr) return true;
    if (p == nullptr || q == nullptr) return false;
    return p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}
```
