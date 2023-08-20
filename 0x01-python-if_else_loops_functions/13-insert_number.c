#include "lists.h"

/**
 * insert_at_pos - inserts a new node at a specific position in a singly linked
 * list
 * @head: a pointer to a pointer to the singly linked list
 * @num: the number to be inserted
 * @pos: the position the 'num' is to be inserted
 *
 * Return: the address of the inserted node, or NULL if it failed
 */

listint_t *insert_at_pos(listint_t **head, int num, int pos)
{
	listint_t *ptr = *head, *temp;
	listint_t *new = malloc(sizeof(listint_t));
	int insert_point = 1;

	new->n = num;
	new->next = NULL;

	if (pos == 0)
	{
		new->next = *head;
		*head = new;

		return (new);
	}

	while (ptr != NULL)
	{
		if (insert_point == pos)
		{
			temp = ptr->next;
			ptr->next = new;
			new->next = temp;

			return (new);
		}

		ptr = ptr->next;
		insert_point++;
	}

	return (NULL);
}


/**
 * insert_node - a function in C that inserts a number into a sorted singly
 * linked list
 * @head: a pointer to a pointer to the head of the singly linked list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	int pos = 0;

	if (ptr == NULL)
		return (insert_at_pos(head, number, 0));

	while (ptr != NULL)
	{
		if (ptr->n > number)
			return (insert_at_pos(head, number, pos));
		pos++;
		ptr = ptr->next;
	}

	return (NULL);
}
