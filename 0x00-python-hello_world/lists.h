#ifndef LISTS_H
#define LISTS_H

/* Definition for singly-linked list */
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

/* Function prototypes for linked list operations */
listint_t *add_nodeint(listint_t *head, int n);
void print_listint(const listint_t *head);
void free_listint(listint_t *head);

/* Function prototype */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
