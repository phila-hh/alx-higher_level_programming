#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	while (f != NULL && f->next != NULL)
	{
		f = f->next->next;
		s = s->next;

		if (f == s)
			return (1);
	}

	return (0);
}
