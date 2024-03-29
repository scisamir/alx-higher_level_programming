#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: a pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (fast == NULL)
		return (0);

	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}

	return (0);
}
