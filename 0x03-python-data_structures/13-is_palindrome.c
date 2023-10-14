#include "lists.h"

/**
 * reverse_list - reverses a singly linked list
 * @head: a double pointer to the list to be reversed
 *
 * Return: Nothing
 */

void reverse_list(listint_t **head)
{
	listint_t *temp = NULL, *ptr = NULL, *ptr2 = NULL;

	temp = *head;
	ptr = temp->next;
	ptr2 = ptr->next;
	temp->next = NULL;

	while (ptr != NULL)
	{
		ptr->next = temp;
		temp = ptr;
		ptr = ptr2;

		if (ptr2)
			ptr2 = ptr2->next;
	}

	*head = temp;
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a doubler pointer to the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *list_copy = NULL, *ptr = NULL;
	listint_t *comp = NULL, *comp2 = NULL;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);

	ptr = *head;

	while (ptr != NULL)
	{
		add_nodeint_end(&list_copy, ptr->n);
		ptr = ptr->next;
	}

	reverse_list(&list_copy);

	comp = *head;
	comp2 = list_copy;

	while (comp != NULL)
	{
		if (comp->n != comp2->n)
		{
			free_listint(list_copy);
			return (0);
		}

		comp = comp->next;
		comp2 = comp2->next;
	}

	free_listint(list_copy);
	return (1);
}
