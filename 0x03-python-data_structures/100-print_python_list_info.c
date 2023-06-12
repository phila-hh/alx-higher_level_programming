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
	long int s, a, i;
	PyObject *obj;

	s = PyList_Size(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python list =  %ld\n", s);
	printf("[*] Allocated = %ld\n", a);

	i = 0;
	for (i < s)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
