#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int list[100];
	int reverse_list[100];
	int counter = 0;
	int i;

	if (*head == NULL)
		return (1);

	temp = *head;
	while (temp != NULL)
	{
		counter++;
		temp = temp->next;
	}
	temp = *head;

	for (i = 0; i < counter; i++)
	{
		list[i] = temp->n;
		reverse_list[counter - (i + 1)] = temp->n;
		temp = temp->next;
	}
	for (i = 0; i < counter; i++)
	{
		if (list[i] != reverse_list[i])
			return (0);
	}
	return (1);
}
