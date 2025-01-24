"""
<Module Name>: <Brief Description>

<Optional longer description of the module.>
This module provides functionalities for [specific task/goal].
It includes functions for [task1], [task2], and [task3].

Examples:
    Example of how to use this module:

        import module_name

        result = module_name.function_name(args)
        print(result)
"""

class ExampleClass:
    """
    Brief description of the class.

    This class is used for [specific purpose].
    It provides methods for [task1], [task2], and [task3].

    Attributes
    ----------
    attribute1 : type
        Description of the first attribute.
    attribute2 : type
        Description of the second attribute.

    Methods
    -------
    method_name(param1, param2):
        Description of what this method does.
    """

    def __init__(self, attribute1: int, attribute2: str):
        """
        Initialize the ExampleClass with given attributes.

        Args:
            attribute1 (int): Description of the first attribute.
            attribute2 (str): Description of the second attribute.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def example_method(self, param1: int, param2: str = "default") -> str:
        """
    Brief description of the function.

    Args:
        param1 (int): Description of the first parameter.
        param2 (str, optional): Description of the second parameter. Defaults to "default".

    Returns:
        bool: Description of the return value.

    Raises:
        ValueError: Description of the error condition.


        Example:
            >>> obj = ExampleClass(10, "example")
            >>> obj.example_method(5)
            'Processed 5 with attribute1=10'
        """
        return f"Processed {param1} with attribute1={self.attribute1}"


def example_function(param1: int, param2: str = "default") -> bool:
    """
    Example function that demonstrates Google-style docstrings.

    Args:
        param1 (int): The first parameter.
        param2 (str, optional): The second parameter. Defaults to "default".

    Returns:
        bool: True if the operation was successful.

    Raises:
        ValueError: If param1 is not a positive integer.

    Example:
        >>> example_function(5, "example")
        True
    """
    if param1 <= 0:
        raise ValueError("param1 must be a positive integer")
    return True
