import textwrap

def wrap(string, max_width):
    
    return textwrap.fill(string, max_width)

if __name__ == '__main__':


# >>> import textwrap
# >>> string = "This is a very very very very very long string."
# >>> print textwrap.wrap(string,8)