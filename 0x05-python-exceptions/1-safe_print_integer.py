def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError as e:
        return False
