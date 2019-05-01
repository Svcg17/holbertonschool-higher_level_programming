#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the first node of a list
 * @number: number to add
 * Return: listint_t list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *prev = NULL;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		new->n = number;
		return (new);
	}
	prev = *head;
	while (prev->next != NULL)
	{
		if (number < prev->next->n)
		{
			new->next = prev->next;
			prev->next = new;
			new->n = number;
			return (new);
		}
		else
			prev = prev->next;
	}
	return (NULL);
}
