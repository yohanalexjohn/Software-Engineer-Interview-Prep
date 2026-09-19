# Has Cycle

Use Rabbit and Hare Algorithm

## Active recall

- Pattern: linked-list cycle detection.
- Use slow and fast pointers.
- Slow moves one node; fast moves two nodes.
- If they meet, there is a cycle.
- If fast reaches `nullptr`, there is no cycle.
- Time: O(n). Space: O(1).

```cpp 
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode * slow = head;
        ListNode * fast = head;

        while(fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast)
            {
                return true;
            }
        }

        return false;
    }
};
```
