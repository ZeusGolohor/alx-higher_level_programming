#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *head = list;

	if (!list)
		return (0);
	while (list->next != NULL)
	{
		if (list->next == head)
			return (1);
		list = list->next;
	}
	return (0);
}
