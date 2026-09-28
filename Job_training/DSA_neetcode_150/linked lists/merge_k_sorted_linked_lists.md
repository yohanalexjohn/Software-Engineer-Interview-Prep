# Merge K Sorted Lists

## Recognition and invariant

Each list head is the smallest remaining value in that list. Keep those `k`
candidates in a min-heap, append the smallest one, then insert only its next
node. `tail` always points to the final node in the merged prefix.

```cpp
ListNode* mergeKLists(vector<ListNode*>& lists)
{
    auto compare = [](ListNode* a, ListNode* b)
    {
        // priority_queue puts the element considered "largest" on top.
        // Returning true for a->val > b->val gives smaller values priority.
        return a->val > b->val;
    };

    priority_queue<
        ListNode*,
        vector<ListNode*>,
        decltype(compare)
    > minHeap(compare);

    // Add first node of each list
    for (ListNode* head : lists)
    {
        if (head != nullptr)
        {
            minHeap.push(head);
        }
    }

    ListNode dummy{0, nullptr}; // removes the special case for the first node
    ListNode* tail = &dummy;

    while (!minHeap.empty())
    {
        ListNode* smallest = minHeap.top();
        minHeap.pop();

        tail->next = smallest;
        tail = tail->next;

        if (smallest->next != nullptr)
        {
            minHeap.push(smallest->next);
        }
    }

    return dummy.next;
}
```

- Time: O(N log k), where N is the total number of nodes.
- Extra space: O(k) for the heap; output reuses the existing nodes.
- Common mistakes: reversing the comparator, pushing null heads, forgetting to
  push `smallest->next`, or losing the result head without dummy/tail.
