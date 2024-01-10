#include <Python.h>

/**
 *  * print_python_list - Prints information about a Python list
 *   * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

if (!p || !PyList_Check(p))
{
fprintf(stderr, "Invalid List Object\n");
return;
}
size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, item->ob_type->tp_name);
}
}

/**
 *  * print_python_bytes - Prints information about a Python bytes object
 *   * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *bytes;

if (!p || !PyBytes_Check(p))
{
fprintf(stderr, "Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
bytes = ((PyBytesObject *)p)->ob_sval;

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", bytes);

printf("  first 10 bytes:");
for (i = 0; i < size && i < 10; i++)
{
printf(" %02x", (unsigned char)bytes[i]);
}
printf("\n");
}
