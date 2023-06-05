#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in linked list
 *
 * @list: header of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp != NULL)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
