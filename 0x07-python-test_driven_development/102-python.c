#include <Python.h>

/**
 *  * print_python_string - Prints information about a Python string object
 *   * @p: Pointer to the Python object
 */
void print_python_string(PyObject *p)
{
if (!PyUnicode_Check(p))
{
fprintf(stderr, "[ERROR] Invalid String Object\n");
return;
}

printf("[.] string object info\n");

if (PyUnicode_IS_COMPACT_ASCII(p))
printf("  type: compact ascii\n");
else
printf("  type: compact unicode object\n");
Py_ssize_t length = PyUnicode_GET_LENGTH(p);
const char *value = PyUnicode_AsUTF8(p);

printf("  length: %ld\n", length);
printf("  value: %s\n", value);
}

/**
 *  * main - Entry point for the C program interacting with Python
 *   *
 *    * Description:
 *This function initializes the Python interpreter, creates Python string
 *objects, and demonstrates the usage of the print_python_string function.
 *Additional C code can be added as needed.
 *        *
 * Return: Always 0 (Success)
 */
int main(void)
{
Py_Initialize();

PyObject *str1 = PyUnicode_DecodeUTF8("Hello, World!", 13, "strict");
PyObject *str2 = PyUnicode_DecodeUTF8("你好，世界！", 20, "strict");

print_python_string(str1);
print_python_string(str2);

Py_XDECREF(str1);
Py_XDECREF(str2);
Py_Finalize();

return (0);
}
