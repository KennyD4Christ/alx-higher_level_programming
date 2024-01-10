#include <Python.h>
#include <stdio.h>

/**
 *  * print_python_list - Prints basic information about a Python list
 *   * @p: Pointer to a Python object (list)
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

if (!PyList_Check(p))
{
fprintf(stderr, "Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 *  * print_python_bytes - Prints basic information about a Python bytes object
 *   * @p: Pointer to a Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

if (!PyBytes_Check(p))
{
fprintf(stderr, "Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %zd\n", size);
printf("  trying string: %s\n", str);

printf("  first %zd bytes: ", (size < 10) ? size : 10);
for (i = 0; i < 10 && i < size; i++)
{
printf("%02x", (unsigned char)str[i]);
if (i < 9 && i + 1 < size)
{
printf(" ");
}
}
printf("\n");
}
