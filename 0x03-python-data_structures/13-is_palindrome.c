#include "lists.h"

/**
  * is_palindrome - To check if a linked list is palindrome.
  * @head: the head to the linked list.
  * Return: Bool
  */

int is_palindrome(listint_t **head)
{
    int len = 0;
    int check = 0;

    len = list_len(*head);
    check = ple_check(*head, len);
    return (check);
}

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

/**
  * ple_check - to check if a list is a palindrome.
  * @head: head to the linked list.
  * @list_len: length of the list.
  * Return: Bool.
  */

int ple_check(listint_t *head, int list_len)
{
    int *array_a, *array_b, i, x;

    array_a = malloc(sizeof(int) * (list_len + 1));
    array_b = malloc(sizeof(int) * (list_len + 1));
    if (array_a == NULL || array_b == NULL)
        return (0);

    i = 0;
    while (head != NULL)
    {
        x = head->n;
        array_a[i] = x;
        array_b[(list_len - i)] = x;
        i++;
        head = head->next;
    }
    i = 0;
    while (i <= list_len)
    {
        if (array_a[i] != array_b[i])
        {
            free(array_a);
            free(array_b);
            return (0);
        }
        i++;
    }
    free(array_a);
    free(array_b);
    return (1);
}
