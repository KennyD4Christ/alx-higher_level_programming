#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            # Allow assignment of 'first_name' attribute
            object.__setattr__(self, name, value)
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
