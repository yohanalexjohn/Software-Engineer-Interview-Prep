# Binary Tree Level Order Traversal

## Prompt

Return the node values of a binary tree one level at a time from left to right.

## Approach

Use BFS with a queue. At the start of each outer iteration, snapshot `levelSize = q.size()`, then process exactly that many nodes.

## Key invariant

At the start of an outer iteration, the queue contains exactly the current level; children appended during it belong to the next level.

## Complexity

- Time: O(n).
- Space: O(w), where `w` is the maximum tree width.

## Common mistakes

- Re-reading `q.size()` as the loop bound while also pushing children.
- Calling `front()` after `pop()`.
- Enqueueing a null root.

```cpp
vector<vector<int>> levelOrder(TreeNode* root)
{
    if (root == nullptr) return {};
    queue<TreeNode*> q;
    q.push(root);
    vector<vector<int>> levels;

    while (!q.empty()) {
        int levelSize = static_cast<int>(q.size());
        vector<int> level;
        for (int i = 0; i < levelSize; ++i) {
            TreeNode* node = q.front();
            q.pop();
            level.push_back(node->val);
            if (node->left != nullptr) q.push(node->left);
            if (node->right != nullptr) q.push(node->right);
        }
        levels.push_back(std::move(level));
    }
    return levels;
}
```
