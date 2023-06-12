#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python object
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int size, aloc, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		return;
	}

	size = PyList_Size(p);
	aloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python list =  %ld\n", size);
	printf("[*] Allocated = %ld\n", aloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
