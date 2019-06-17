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
 * selection_sort - sorts an array of integers in ascending order
 * using the Selection sort algorithm
 *
 * @array: array of integers to be sorted
 * @size: size of the array of integers to be sorted
 *
 */
void selection_sort(int *array, size_t size)
{
	size_t i, new, min_val;

	for (i = 0; i < size - 1; i++)
	{
		min_val = i;
		for(new = i + 1; new < size; new++)
		{
			if (array[new] < array[min_val])
				min_val = new;
		}

		if (array[new] > array[min_val])
		{
			swap_ints(&array[min_val], &array[i]);
			print_array(array, size);
		}
	}
}
