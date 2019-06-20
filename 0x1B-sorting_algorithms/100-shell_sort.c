#include "sort.h"

/**
 * shell_sort - sorts an array of integers in ascending order using the
 * Shell sort algorithm, using Knuth sequence
 *
 * @array: array of integers to be sorted
 * @size: size of the array of ints
 */
void shell_sort(int *array, size_t size)
{
	int temp;
	size_t i, j, gap = 1;

	/*set gap value*/
	while (gap * 3 + 1 < size)
		gap = gap * 3 + 1;

	while (gap > 0)
	{
		for (i = gap; i < size; i++)
		{
			temp = array[i];
			j = i;
			/* checks to see if the leftmost gap value ismore than the current gap*/
			while (j > gap - 1 && array[j - gap] >= temp)
			{
				/*swap values*/
				array[j] = array[j - gap];
				j = j - gap;
			}
			array[j] = temp;
		}
		print_array(array, size);
		/*reduce gap*/
		gap = (gap - 1) / 3;
	}
}
