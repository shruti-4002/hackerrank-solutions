# Reverse a doubly linked list

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Reverse a doubly linked list](https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem)

## Problem Description

This challenge is part of a tutorial track by [MyCodeSchool](http://www.youtube.com/mycodeschool)

Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the *next* and *prev* pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

**Note:** The head node might be NULL to indicate that the list is empty.

**Function Description**

Complete the *reverse* function in the editor below.

reverse has the following parameter(s):

* *DoublyLinkedListNode head*: a reference to the head of a DoublyLinkedList

Returns **
- *DoublyLinkedListNode*: a reference to the head of the reversed list

Input Format**

The first line contains an integer , the number of test cases.

Each test case is of the following format:

* The first line contains an integer , the number of elements in the linked list.

* The next  lines contain an integer each denoting an element of the linked list.

**Constraints**

*

*

*

**Output Format**

Return a reference to the head of your reversed list.  The provided code will print the reverse array as a one line of space-separated integers for each test case.

**Sample Input**

```
1
4
1
2
3
4

```

**Sample Output**

```
4 3 2 1

```

**Explanation**

The initial doubly linked list is:

The reversed doubly linked list is:

## Examples



## Constraints



## Solution

```cpp
// HackerRank Problem: Reverse a doubly linked list
// Link: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
// Difficulty: Easy
// Language: cpp



/*
 * Complete the 'reverse' function below.
 *
 * The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
 * The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
 */

/*
 * For your reference:
 *
 * DoublyLinkedListNode {
 *     int data;
 *     DoublyLinkedListNode* next;
 *     DoublyLinkedListNode* prev;
 * };
 *
 */

DoublyLinkedListNode* reverse(DoublyLinkedListNode* llist) {
DoublyLinkedListNode* first=nullptr;
DoublyLinkedListNode*last=nullptr;
DoublyLinkedListNode*current=llist;


while(current!=nullptr){
    last=current->next;
    current->next=first;
    current->prev=last;
    first=current;
    current=last;
    
}





return first;






}

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
