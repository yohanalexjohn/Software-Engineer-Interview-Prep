# Push and Pop Front with `Node**`

## Prompt

Implement C linked-list `push_front` and `pop_front` functions that can replace the caller's head pointer.

## Approach

Pass `Node** head` because C passes the `Node*` argument by value. Writing `*head = newHead` updates the caller's pointer. Push links a new node before the old head; pop saves the old head, advances `*head`, then frees the old node.

Pointer chain: if `Node* head` stores the first node's address, then
`Node** headRef = &head` stores the address of that pointer. `headRef` points to
the caller's variable, `*headRef` is the first-node pointer, and
`(*headRef)->next` is the second-node pointer. Call a mutating function with
`push_front(&head, value)`.

## Key invariant

After each successful operation, `*head` is the first live node (or null), and every remaining node is reachable exactly once from it.

## Complexity

- Time: O(1) for both operations.
- Space: O(1), excluding the one node allocated by push.

## Common mistakes

- Accepting `Node* head` and changing only the function's local copy.
- Writing `*head->next`; use `(*head)->next` because `->` binds first.
- Freeing the old head before saving its `next` pointer.
- Not checking `head`, `*head`, `out`, or allocation failure.

```c
typedef struct Node {
    int value;
    struct Node* next;
} Node;

bool push_front(Node** head, int value)
{
    if (head == NULL) return false;
    Node* node = malloc(sizeof *node);
    if (node == NULL) return false;
    node->value = value;
    node->next = *head;
    *head = node; // mutate the caller's Node* head through Node**
    return true;
}

bool pop_front(Node** head, int* out)
{
    if (head == NULL || *head == NULL || out == NULL) return false;
    Node* oldHead = *head;
    *out = oldHead->value;
    *head = oldHead->next; // replace the caller's head before freeing oldHead
    free(oldHead);
    return true;
}
```

The deeper pointer explanation remains in [[../../DSA_theory/linked_list]].
