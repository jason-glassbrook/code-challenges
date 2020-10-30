#!python3

############################################################
#   DECOR
#-----------------------------------------------------------
#   A module of helpful decorators.
############################################################

import functools as _fun
import collections.abc as _abc

#-----------------------------------------------------------

# We want to export `wraps` for convenience.
wraps = _fun.wraps


def double_decor(decorator: _abc.Callable) -> _abc.Callable:
    """
    Decorator for decorators that can be used with or without additional arguments.

    For example...

    ```
    @double_decor
    def decorator(fun: Callable, *args, **kwargs): ...
    ```

    ...will define `decorator` so that it can be used as...

    ```
    # SINGLE
    @decorator
    def fun_A(...): ...
    ```

    ...or...

    ```
    # DOUBLE
    @decorator(*args, **kwargs)
    def fun_B(...): ...
    ```
    """

    @wraps(decorator)
    def decor_router(*args, **kwargs):

        if len(args) == 1 and len(kwargs) == 0 and callable(decorator):
            # `decorator` was used in "single" form:
            # @decorator
            # def {fun = args[0]}(...): ...

            fun = args[0]
            return decorator(fun)

        else:
            # `decorator` was used in "double" form:
            # @decorator(*args, **kwargs)
            # def fun(...): ...

            def doubled_decorator(fun):
                return decorator(fun, *args, **kwargs)

            return doubled_decorator

    return decor_router
