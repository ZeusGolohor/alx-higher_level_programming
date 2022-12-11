#include "lists.h"

/**
  * list_len - Gets the length of a linked int.
  * @head: head to linked list.
  * Return: length of linked list.
  */

int list_len(const listint_t *head)
{
    int i;

    i = -1;
    while (head != NULL)
    {
        i++;
        head = head->next;
    }
    return (i);
}
