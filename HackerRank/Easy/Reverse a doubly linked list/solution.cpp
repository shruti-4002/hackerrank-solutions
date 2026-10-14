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
