#include "lists.h"

int ple_check(listint_t *head, int list_len)
{
    int array_a[list_len];
    int array_b[list_len];
    int i;
    int x;

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
            return (0);
        i++;
    }
    return (1);
}

