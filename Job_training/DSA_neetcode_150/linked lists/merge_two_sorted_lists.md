# Merge Two Sorted Lists

## Active recall

- Pattern: merge two sorted linked lists.
- Algorithm: use a dummy head and a `tail` pointer, or recursively choose the smaller head.
- Repeatedly attach the smaller current node from `list1` or `list2`.
- After one list ends, attach or return the remaining nodes from the other list.
- Time: O(n + m). Space: O(1) iterative, O(n + m) recursion stack for recursive version.
- Common mistake: losing the head; with dummy-head iteration return `dummy.next`.

You’re given two sorted singly linked lists. Merge them into one sorted list and return the head.

```cpp 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        if(!list1) return list2;
        if(!list2) return list1;

        if(list1->val <= list2->val)
        {
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        }
        else
        {
            list2->next = mergeTwoLists(list1, list2->next);
            return list2;
        }
    }
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy;
        ListNode* current = &dummy;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                current->next = list1;
                list1 = list1->next;
            }
            else {
                current->next = list2;
                list2 = list2->next;
            }

            current = current->next;
        }

        if (list1 != nullptr) {
            current->next = list1;
        }
        else {
            current->next = list2;
        }

        return dummy.next;
    }
};
```
