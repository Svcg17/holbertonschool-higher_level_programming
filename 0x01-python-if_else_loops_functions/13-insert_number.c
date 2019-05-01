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
	listint_t *current;

	if (new == NULL)
		return (NULL);
	if (head == NULL)
		return (NULL);
	current = *head;
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	if (current->n > number)
	{
		*head = new;
		new->next = current;
		return (new);
	}
	while (current->next != NULL)
	{
		if (number < current->next->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		else
			current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
