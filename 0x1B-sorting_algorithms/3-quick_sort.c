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


int partition(int *array, int low, int high, size_t size)
{
	int pivot = array[high];
	int i = low - 1;
	int j;

	for (j = low; j <= high - 1; j++)
	{
		if (array[j] <= pivot)
		{
			i++;
			swap_ints(&array[j], &array[i]);
			if (array[i] != array[j])
				print_array(array, size);
		}
	}
	swap_ints(&array[i + 1], &array[high]);
	if (array[high] != array[i + 1])
	{
		print_array(array, size);
	}

	return (i + 1);
}

void recursion(int *array, int low, int high, size_t size)
{
	int pi;

	if(low < high)
	{
		pi = partition(array, low, high, size);
		recursion(array, low, pi - 1, size);
		recursion(array, pi + 1, high, size);
	}
}

/**
 * quick_sort - sorts an array of integers in ascending order using
 * the Quick sort algorithm
 * @array: array of integers to be sorted.
 * @size: size of the array of integers.
 */
void quick_sort(int *array, size_t size)
{
	if (array == NULL)
		return;
	recursion(array, 0, size - 1, size);
}
