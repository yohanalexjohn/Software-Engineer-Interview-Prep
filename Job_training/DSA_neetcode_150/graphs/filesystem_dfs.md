# Filesystem DFS — Optional / Low Priority

Use DFS when a directory contains files and subdirectories and every reachable
entry must be visited. Treat the filesystem as a tree unless symbolic links or
other links can create cycles.

Checklist:

- Decide whether to process a path before or after its children.
- Distinguish files from directories before recursing.
- Handle permission errors and disappearing entries without crashing the full
  traversal.
- If following symbolic links, track stable file identities or canonical paths
  to prevent cycles.
- Recursive DFS uses O(h) stack space; an explicit stack avoids call-stack
  overflow on very deep trees.

This is optional interview breadth. Keep RTOS/concurrency, memory, pointers,
buffers, and core DSA ahead of filesystem-specific practice.
