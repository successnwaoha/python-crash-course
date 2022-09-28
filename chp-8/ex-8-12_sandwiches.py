def sandwiches(*items):
    """Prints an unknown number of arguments"""
    print(f"Adding {items} to your sandwich")
    for i in items:
        print(i)
sandwiches('mushroom', 'pepper', 'extra cheese')
sandwiches('mushroom', 'pepper')
sandwiches('mushroom')