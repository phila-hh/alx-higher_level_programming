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
	Py_ssize_t i, list_size;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object_cast;

	list_object_cast = (PyListObject *)p;
	list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) list_size);
	printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);

	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
	}
}
