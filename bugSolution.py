def function_with_closed_file(filename):
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ... 
        return f.read() # or any other processing of the file
    finally:
        f.close() # Ensures file closure even if exceptions occur