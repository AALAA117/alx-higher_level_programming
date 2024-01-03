#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check the code
 * @list:..
 * Return: integer
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;
	int count = 0;

	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
	{
		return (-1);
	}
	ptr = list;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	if (count == 1)
	{
		free(ptr);
		return (1);
	}
	else
	{
		free(ptr);
		return (0);
	}
}
