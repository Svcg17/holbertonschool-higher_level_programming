#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: pointer to a pointer to a list to be reversed.
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *t, *t2;

	if (*head == NULL)
		return (NULL);
	t = *head;
	while (t->next != NULL)
	{
		t2 = t->next;
		t->next = t2->next;
		t2->next = *head;
		*head = t2;
	}
	return (*head);
}
/**
 * is_palindrome - function that checks if list is a palindrome
 * @head: pointer to a pointer to the first node of the list
 * Return: 1 if it's palindrome, 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head;
	listint_t *f = *head;
	listint_t *current = *head;
	listint_t *mid = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (f != NULL && f->next != NULL && f->next->next)
	{
		s = s->next;
		f = f->next->next;
	}
	mid = reverse_listint(&s);
	while (current != NULL && mid != NULL)
	{
		if (current->n != mid->n)
			return (0);
		current = current->next;
		mid = mid->next;
	}
	return (1);
}



