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
 * partition - gets pivot
 * places pivot in place in the array.
 * @array: array of integers to be sorted.
 * @low: minimun number in array
 * @high: maximum number in array
 * @size: size of the array of integers
 * Return: index value of pivot
 */
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
/**
 * recursion - recursively calls itself to call partition function
 * takes care of passing to partition for sorting the left and
 * right part of the rest of the numbers
 * @array: array of integers to be sorted.
 * @low: minimum index value of array.
 * @high: maximum index value of array.
 * @size: size of the array.
 */
void recursion(int *array, int low, int high, size_t size)
{
	int pi;

	if (low < high)
	{
		/*store pivot index in pi*/
		pi = partition(array, low, high, size);
		/*recursively call function from 0 to pivot*/
		recursion(array, low, pi - 1, size);
		/*recursively call function from pivot to max idx*/
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
	/*call recursion func low = 0, high = size - 1*/
	recursion(array, 0, size - 1, size);
}
