#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the address of the singly linked list to be checked
 *
 * Return: 1 if it is a palindrome, 0 if it is not a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *first;
	listint_t *prev, *curr, *next;

	if (*head == NULL)
		return (1);

	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	prev = NULL;
	curr = slow->next;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	first = *head;
	while (first != NULL && prev != NULL)
	{
		if (first->n != prev->n)
			return (0);
		first = first->next;
		prev = prev->next;
	}

	return (1);
}
