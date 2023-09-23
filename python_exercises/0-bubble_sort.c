#include "sort.h"

/**
 *bubble_sort - Funtion that sorts a given array of integers in an
 *	ascending order by the use of bubble sort algorithm. It then
 *	prints out the array after each swaps done
 *@array: The array with the data(integers) to sort
 *@size: The length or the array
 *
 * Return: void
 */
void bubble_sort(int *array, size_t size)
{
	unsigned long int i, j;
	int temp;

	if (size < 2 || array == NULL)
		return;

	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size - i - 1; j++)
		{
			if (array[j] > array[j + 1])
			{
				temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
				print_array(array, size);
			}
		}
	}
}
