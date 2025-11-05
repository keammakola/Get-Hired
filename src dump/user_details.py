def basic_info():
    """
    Get user's basic information.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Example
    -------
    >>> basic_info()
    Enter your First name & Surname: John Doe
    John
    Doe
    """
    name, surname = input("Enter your First name & Surname: ").split()
    print(name)
    print(surname)


if __name__ == "__main__":
    basic_info()
