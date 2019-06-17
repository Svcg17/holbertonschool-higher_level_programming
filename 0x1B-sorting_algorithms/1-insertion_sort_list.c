#include "sort.h"

/**
 * insertion_sort_list - sorts a doubly linked list of integers in ascending
 * order using the Insertion sort algorithm.
 *
 * @list: pointer to the head of the doubly linked list to be used.
 */
void insertion_sort_list(listint_t **list)
{
	listint_t *cur = NULL;
	listint_t *p, *prevnode = NULL;

	if (list == NULL)
		return;
	cur = *list;
	while (cur != NULL)
	{
		prevnode = cur->prev;
		while(prevnode != NULL)
		{
			if (prevnode->n > cur->n)
			{
				if (cur->next != NULL)
					cur->next->prev = prevnode;
				prevnode->next = cur->next;
				p = prevnode->prev;
				prevnode->prev = cur;
				cur->next = prevnode;
				cur->prev = p;
				if (p != NULL)
					p->next = cur;
				else
					*list = cur;
			}
			else
				break;
			print_list(*list);
			prevnode = prevnode->prev;
			prevnode = prevnode->prev;
		}
		cur = cur->next;
	}
}
