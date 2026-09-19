# Reverse Linked List

## Active recall

- Pattern: pointer relinking.
- Algorithm: keep `prev`, `curr`, and `next`.
- Save `next = curr->next` before changing `curr->next`.
- Point `curr->next` to `prev`, then advance `prev = curr`, `curr = next`.
- Time: O(n). Space: O(1).
- Common mistake: overwriting `curr->next` before saving the rest of the list.

```cpp 
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *current = NULL;
        ListNode *prev = NULL;

        while(head != NULL)
        {
            current = head->next;
            head->next = prev;
            prev = head;
            head = current;
        }

    return prev;
    }
};
```
