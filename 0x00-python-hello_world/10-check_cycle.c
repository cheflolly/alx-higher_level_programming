#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		/* slow pointer will move one node per iteration, fast node
		   will move two nodes per iteration
		   */
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			list = slow;
			slow = fast;
			while (1)
			{
				fast = slow;
				while (fast->next != list && fast->next != slow)
				{
					fast = fast->next;
				}
				if (fast->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
