def fibonacci(n):
    """
    Generate a list containing the Fibonacci sequence up to the n-th element.
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1.
    Args:
        n (int): The number of elements in the Fibonacci sequence to generate.
    Returns:
        list: A list containing the first n elements of the Fibonacci sequence.
    Examples:
        >>> fibonacci(0)
        []
        >>> fibonacci(1)
        [0]
        >>> fibonacci(2)
        [0, 1]
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence