#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 *  * print_python_list - Prints information about a Python List object
 *   * @p: Pointer to PyObject representing a Python List
 */
void print_python_list(PyObject *p)
{
if (!p || !PyList_Check(p))
{
fprintf(stderr, "Invalid List Object\n");
return;
}

Py_ssize_t size = PyObject_Size(p);
PyObject *element;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyVarObject *)p)->ob_size);

for (Py_ssize_t i = 0; i < size; i++)
{
element = PyTuple_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
}
}

/**
 *  * print_python_bytes - Prints information about a Python Bytes object
 *   * @p: Pointer to PyObject representing a Python Bytes
 */
void print_python_bytes(PyObject *p)
{
if (!p || !PyBytes_Check(p))
{
fprintf(stderr, "Invalid Bytes Object\n");
return;
}
Py_ssize_t size = PyObject_Size(p);
char *str = NULL;
if (PyBytes_AsStringAndSize(p, &str, &size) == -1)
{
fprintf(stderr, "Error getting Bytes data\n");
return;
}

printf("[.] bytes object info\n");
printf("size: %zd\n", size);
printf("trying string: %s\n", str ? str : "(no value)");

printf("first 6 bytes: ");
for (Py_ssize_t i = 0; i < size && i < 6; i++)
printf("%02hhx ", str[i] & 0xff);
printf("00\n");
}

/**
 *  * print_python_float - Prints information about a Python Float object
 *   * @p: Pointer to PyObject representing a Python Float
 */
void print_python_float(PyObject *p)
{
if (!p || !PyFloat_Check(p))
{
fprintf(stderr, "Invalid Float Object\n");
return;
}

printf("[.] float object info\n");
printf("value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
