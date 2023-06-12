#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 *
 * @p: PyObject
 *
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	long int size;
	long int i;
	PyListObject *my_list;
	PyObject *element;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	my_list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", my_list->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
