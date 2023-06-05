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
	listint_t *one_step = list;
	listint_t *two_steps = list;

	while (two_steps != NULL && two_steps->next != NULL)
	{
		one_step = one_step->next;
		two_steps = two_steps->next->next;

		if (one_step == two_steps)
			return (1);
	}
	return (0);
}
