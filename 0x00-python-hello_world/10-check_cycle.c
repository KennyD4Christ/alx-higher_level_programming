#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *  * add_nodeint - Adds a new node at the beginning of a linked list.
 *   * @head: Pointer to the head of the list.
 *    * @n: Value to set in the new node.
 *     *
 *      * Return: Address of the new node or NULL on failure.
 */

listint_t *add_nodeint(listint_t *head, int n)
{
listint_t *new_node = malloc(sizeof(listint_t));
if (!new_node)
return (NULL);
new_node->n = n;
new_node->next = head;
return (new_node);
}

/**
 *  * print_listint - Prints the elements of a linked list.
 *   * @head: Pointer to the head of the list.
 */

void print_listint(const listint_t *head)
{
while (head != NULL)
{
printf("%d", head->n);
if (head->next != NULL)
{
printf(" -> ");
}
head = head->next;
}
printf("\n");
}

/**
 *  * free_listint - Frees the memory allocated for a linked list.
 *   * @head: Pointer to the head of the list.
 */

void free_listint(listint_t *head)
{
listint_t *current, *next;
current = head;
while (current != NULL)
{
next = current->next;
free(current);
current = next;
}
}

/**
 *  * check_cycle - Check if a singly linked list has a cycle.
 *   * @list: A pointer to the head of the linked list.
 *    * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
listint_t *tortoise, *hare;
if (list == NULL)
return (0);
tortoise = list;
hare = list->next;
while (tortoise != hare)
{
if (hare == NULL || hare->next == NULL)
return (0);
tortoise = tortoise->next;
hare = hare->next->next;
}
return (1);
}
