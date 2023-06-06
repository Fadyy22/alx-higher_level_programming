#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to the head of the linked list
 * @number: number to be inserted in the new node
 *
 * Return: address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	if (head == NULL)
	listint_t *temp = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	while (temp->next != NULL)
	{
		if ((new_node->n) >= (temp->n) && (new_node->n) < (temp->next->n))
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	temp->next = new_node;
	return (new_node);
}
