#!/usr/bin/python3

def no_c(my_string):
    # Use list comprehension to create a new string without 'c' and 'C'
    new_string = ''.join(char for char in my_string if char not in 'cC')
    return new_string


# Example usage
if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
