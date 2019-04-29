#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - function that checks if there is a loop inside list
 * @list: pointer to first node in list
 * Return: 1 if there is, 0 if there isnt
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (list != NULL && fast != NULL && fast->next != NULL &&
			fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}

