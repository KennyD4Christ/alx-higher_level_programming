#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        # Create a new list using slicing to avoid modifying the original list
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
    else:
        # If idx is -ve or out of range, return a copy of the original list
        return my_list


# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
