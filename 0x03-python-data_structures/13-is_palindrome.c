#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a doubler pointer to the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr = NULL;
	int *arr = NULL;
	int i = 0, len = 0;

	if (head == NULL || *head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);

	ptr = *head;

	/* Get the length of the list */
	while (ptr != NULL)
	{
		len++;
		ptr = ptr->next;
	}
	ptr = *head;

	/* Copy list to array */
	arr = malloc(sizeof(int) * len);
	while (ptr != NULL)
	{
		arr[i++] = ptr->n;
		ptr = ptr->next;
	}

	/* Determine if list is a palindrome */
	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}
