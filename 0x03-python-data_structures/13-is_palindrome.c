#include "lists.h"

/**
  * is_palindrome - To check if a linked list is palindrome.
  * @head - the head to the linked list.
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
