#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the address of the head of a singly linked list
 * @number: the new number to be inserted into the list
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new, *cur;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	prev = NULL;
	cur = *head;
	while (cur != NULL)
	{
		if (number < cur->n)
		{
			break;
		}
		prev = cur;
		cur = cur->next;
	}
	new->next = cur;

	if (prev != NULL)
	{
		prev->next = new;
	}
	else
	{
		*head = new;
	}

	return (new);
}
