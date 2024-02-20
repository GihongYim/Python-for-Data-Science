def callLimit(limit: int):
    """callLimit(limit)
takes as argument a call limit of another function and blocks
its execution above a limit.

    Args:
        limit (int): function call limit

    Returns:
        function: excute function function limit call,
        should sub function called number of limit
    """
    try:
        if not isinstance(limit, int):
            raise TypeError('limit is not an integer')
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)

    count = 0

    def callLimiter(function):
        """outer function call limit_function

        Args:
            function (function): limit_function(*args:any, **kwds: any)
        """
        def limit_function(*args: any, **kwds: any):
            """
            limit_function(*args: any, **kwds: any)
            """
            nonlocal count
            count += 1
            if count <= limit:
                function()
            else:
                print("Error: ", function, " call too many times")
        return limit_function
    return callLimiter
