#include "lists.h"

/**
 * insert_node - A function used to insert a newnode into a list.
 * @head: a pointer to a pointer to the head node.
 * @number: the data to be inserted into the newnode.
 * Return: listint_t *.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *newnode;

	if (*head == NULL)
	{
		newnode = create_newnode(number, NULL);
		if (newnode == NULL)
			return (NULL);
		*head = newnode;
		return (*head);
	}
	if (number <= temp->n)
	{
		newnode = create_newnode(number, temp);
		if (newnode == NULL)
			return (NULL);
		*head = newnode;
	}
	else
	{
		while (temp->next != NULL)
		{
			if (number <= temp->next->n)
			{
				newnode = create_newnode(number, temp->next);
				if (newnode == NULL)
					return (NULL);
				temp->next = newnode;
				break;
			}
			temp = temp->next;
		}
		if (temp->next == NULL)
		{
			newnode = create_newnode(number, NULL);
			if (newnode == NULL)
				return (NULL);
			temp->next = newnode;
		}
	}
	return (*head);
}

/**
 * create_newnode - A function used to create newnodes.
 * @n: data to be inserted into the newnode.
 * @next: next node to be inserted into the list.
 * Return: listint_t *.
 */
listint_t *create_newnode(int n, listint_t *next)
{
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = n;
	newnode->next = next;
	return (newnode);
}

