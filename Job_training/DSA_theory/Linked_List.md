# Linked Lists

## Advantages

- Do not need to specify memory when creating the list
- Grows in size when each new node is added to the end of the list

## Theory basic

- Series of nodes
- Each node has a pointer to the next node
- Last nodes next is **null**

1. Insertion O(1)
2. Deletion O(n)
3. Searching O(n)

## Singly Linked List

```c
struct ListNode {
    int data;
    struct ListNode *next;
};

// Function to create a new node
struct ListNode* newNode(int data) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->data = data;
    node->next = NULL;
    return node;
}
```

### Insertion

```c
// Function to insert a new node at the end of the list
void insertNode(struct ListNode** head, int data) 
{
// Create a new node
   struct ListNode* new_node = newNode(data);
// If list is empty
   if (*head == NULL) {
       *head = new_node;
   }
   else {
        // Don't change the original heads pointing 
        struct ListNode* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = new_node;
   }
}
```

### Searching

Traverse the list checking the value we are looking for

```c
// Function to search for a node with a specific value
bool search_for_node(struct ListNode *node, int data) {
    while (node != NULL) {
        if (node->data == data) {
            return true;
        }
        node = node->next;
    }
    return false;
}
```

### Deletion

The list is empty cannot delete
The node to remove is the only node in the linked list
Removing the tail node
Removing the head node
Removing the node in between the linked list
The item to remove doesn't exist

```c
// Function to delete a node with a specific value
bool deleteNode(struct ListNode** head, int data) {
    if (*head == NULL) {
        // The list is empty
        return false;
    }

    struct ListNode* temp = *head;
    struct ListNode* prev = NULL;

    // If the node to be deleted is the head node
    if (temp != NULL && temp->data == data) {
        *head = temp->next; // Changed head
        free(temp);         // Free the old head
        return true;
    }

    // Search for the node to be deleted, keep track of the previous node
    while (temp != NULL && temp->data != data) {
        prev = temp;
        temp = temp->next;
    }

    // If the node to be deleted was not found
    if (temp == NULL) {
        return false;
    }

    // If the node to be deleted is the last node
    if (temp->next == NULL) {
        prev->next = NULL;
        free(temp);
        return true;
    }

    // Node found in between
    prev->next = temp->next;
    free(temp);
    return true;
}
```

### Traverse a Linked list

```c
// Function to reverse traverse the list and print the values.
void ReverseTraversal(struct ListNode* head, struct ListNode* tail) {
    // Ensure that head and tail belong to the same list.
    if (tail != NULL) {
        struct ListNode* curr = tail;
        while (curr != head) {
            struct ListNode* prev = head;
            while (prev->Next != curr) {
                prev = prev->Next;
            }
            printf("%d\n", curr->Value);
            curr = prev;
        }
        printf("%d\n", curr->Value);
    }
}
```

## Double Linked List

### Insert Node

```c
// Function to create a new node
struct ListNode* newNode(int data) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->data = data;
    node->next = NULL;
    return node;
}
```

```c
// Function to insert a new node at the end of the list
// Double pointer as we need to modify the actual value 
// of the head and not just a copy
void insertNode(struct ListNode** head, int data) {
    struct ListNode* new_node = newNode(data);
    if (*head == NULL) {
        *head = new_node;
    } 
    else {
        struct ListNode* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = new_node;
    }
}
```

### Search

```c
// Function to search for a node with a specific value
bool search_for_node(struct ListNode *node, int data) {
    while (node != NULL) {
        if (node->data == data) {
            return true;
        }
        node = node->next;
    }
    return false;
}
```

### Deletion double linked list

```c
// Function to delete a node with a specific value
bool deleteNode(struct ListNode** head, int data) {
    if (*head == NULL) {
        // The list is empty
        return false;
    }

    struct ListNode* temp = *head;

    // If the node to be deleted is the head node
    if (temp != NULL && temp->data == data) {
        *head = temp->next; // Change head
        if (*head != NULL) {
            (*head)->prev = NULL;
        }
        free(temp); // Free the old head
        return true;
    }

    // Search for the node to be deleted
    while (temp != NULL && temp->data != data) {
        temp = temp->next;
    }

    // If the node to be deleted was not found
    if (temp == NULL) {
        return false;
    }

    // If the node to be deleted is the last node
    if (temp->next == NULL) {
        temp->prev->next = NULL;
        free(temp);
        return true;
    }

    // Node found in between
    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    free(temp);
    return true;
}
```

## Traversal reverse linked

```c
// Function to perform reverse traversal and print values.
void reverseTraversal(struct ListNode* head, struct ListNode* tail) {
    // Ensure that head and tail belong to the same list.
    if (tail != NULL) {
        struct ListNode* curr = tail;
        while (curr != NULL) {
            printf("%d\n", curr->value);
            curr = curr->prev;
        }
    }
}
```
