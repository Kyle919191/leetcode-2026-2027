# Linked List Notes

## Dummy (Virtual Head) Node

Many readers ask me, when should we use a dummy (virtual head) node?

Here is my summary: when you need to create a new linked list, you can use a dummy node to make edge cases easier.

For example, when you merge two sorted lists into a new list, you need to create a new linked list. Or when you split a list into two new lists, you are also creating new linked lists. In these cases, using a dummy node makes the code simpler and easier to handle edge cases.
