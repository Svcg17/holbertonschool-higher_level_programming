#include "sort.h"
/**
 * swap_ints - swaps two integers
 * @a: integer to swap
 * @b: integer to swap
 */
void swap_ints(int *a, int *b)
{
	int temp = 0;

	temp = *a;
	*a = *b;
	*b = temp;
}

/**
 * bubble_sort - sorts an array of integers in ascending order using the
 * Bubble sorting algorithm.
 *
 * @array: array of integers to be sorted
 * @size: size of the array of integers
 */
void bubble_sort(int *array, size_t size)
{
	size_t i, j;

	if (size < 2)
		return;

	for (j = 0; j < size; j++)
	{
		for (i = 0; i < size; i++)
		{
			if (array[i] < array[i - 1])
			{
				swap_ints(&array[i - 1], &array[i]);
				print_array(array, size);
			}
		}
	}
}
