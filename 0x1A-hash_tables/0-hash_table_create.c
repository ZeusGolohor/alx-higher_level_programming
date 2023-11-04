#include "hash_tables.h"

/**
  * hash_table_create - Used to create a hash table.
  * @size: The size of the hash table.
  * Return: hash_table_t *.
  */
hash_table_t *hash_table_create(unsigned long int size)
{
	unsigned long int i;
	hash_table_t *table;

	if (size == 0)
		return (NULL);
	table = malloc(sizeof(hash_table_t));
	if (table == NULL)
		return (NULL);
	table->size = size;
	table->array = calloc(sizeof(hash_node_t *), size);
	if (table->array == NULL)
		return (NULL);
	for (i = 0; i < size; i++)
		table->array[i] = NULL;
	return (table);
}
