# Add Two Lists

## Prompt

Two non-empty linked lists store non-negative integers in reverse digit order.
Add the numbers and return the sum as a linked list in the same order.

## Approach

- Walk both lists together and treat a missing digit as `0`.
- Compute `sum = digit1 + digit2 + carry`.
- Append `sum % 10`; carry `sum / 10` into the next column.
- Continue while either list remains or `carry != 0`.

## Key invariant

Before each iteration, `tail` is the final node of the already-computed low-order
digits, and `carry` is exactly what must enter the next digit column.

## Complexity

- Time: O(max(m, n)).
- Space: O(max(m, n)) for the returned list; O(1) auxiliary state.

## Common mistakes

- Stopping when the shorter list ends.
- Forgetting a final carry, such as `5 + 5 -> 0 -> 1`.
- Advancing a null list pointer.
- Using a `TreeNode` definition for a linked-list problem.

## C++

```cpp
struct ListNode
{
    int val;
    ListNode* next;
};

ListNode* addTwoNumbers(
    ListNode* l1,
    ListNode* l2)
{
    ListNode* dummy = new ListNode{0, nullptr};
    ListNode* tail = dummy;

    int carry = 0;

    while (l1 != nullptr ||
           l2 != nullptr ||
           carry != 0)
    {
        int val1 = (l1 != nullptr) ? l1->val : 0;
        int val2 = (l2 != nullptr) ? l2->val : 0;

        int sum = val1 + val2 + carry;

        int digit = sum % 10;
        carry = sum / 10;

        ListNode* node =
            new ListNode{digit, nullptr};

        tail->next = node;
        tail = tail->next;

        if (l1 != nullptr)
        {
            l1 = l1->next;
        }

        if (l2 != nullptr)
        {
            l2 = l2->next;
        }
    }

    ListNode* result = dummy->next;
    delete dummy;

    return result;
}
```
