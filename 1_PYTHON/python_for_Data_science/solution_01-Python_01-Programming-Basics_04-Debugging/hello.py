# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
    """returns the full name"""
    name = f"{first_name.capitalize()}{last_name.capitalize()}"
    # $DELETE_BEGIN
    # Uncomment the line below and run your code to see the debugger in action
    # breakpoint()
    name = f"{first_name.capitalize()} {last_name.capitalize()}".strip()
    # $DELETE_END
    return name

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # => ['hello.py']
        print(f'Hello{full_name("", "")}!')
    elif len(sys.argv) == 2:
        # => ['hello.py', 'John' ]
        print(f'Hello {full_name(sys.argv[1], "")}!')
    else:
        # => ['hello.py', 'John', 'Lennon']
        print(f"Hello {full_name(sys.argv[1], sys.argv[2])}!")
