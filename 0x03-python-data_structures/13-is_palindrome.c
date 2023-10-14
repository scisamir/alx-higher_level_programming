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
	listint_t *second_list = NULL, * temp = NULL;
	listint_t *slow = NULL, *fast = NULL;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);

	temp = *head, slow = *head, fast = *head;

	/* Separate list into two */
	while (1)
	{
		fast = fast->next->next;
		if (fast == NULL)
		{
			second_list = slow->next;
			break;
		}
		if (fast->next == NULL)
		{
			second_list = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	slow->next = NULL;

	/* Reverse second list */
	reverse_list(&second_list);

	/* Compare first and second lists */
	while (second_list != NULL)
	{
		if (temp->n != second_list->n)
			return (0);
		second_list = second_list->next;
	}
	return (1);
}
