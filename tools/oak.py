#!python3

############################################################
#   OAK (Of A Kind)
#-----------------------------------------------------------
#   A module of tools for type-checking.
############################################################

import sys as _sys
from collections import abc as _abc

from . import decor as _decor

#-----------------------------------------------------------

_DLI_F_TYPE = _abc.Callable[..., bool]
_DLI_RP_TYPE = _abc.Iterable[tuple[str, str]]
_DLI_RP_DEFAULT = (
    ("is_", "isnt_"),
    ("", "not_"),    # ⬅ Fallback option.
)


@_decor.double_decor
def def_logical_inverse(
    fun: _DLI_F_TYPE,
    replace_prefix: _DLI_RP_TYPE = _DLI_RP_DEFAULT,
):
    """
    Decorator that defines the "notted" (logical inverse) of the decorated function.
    """

    # Define generic logical inverse function, `not_fun`.
    def not_fun(*args, **kwargs):
        return not fun(*args, **kwargs)

    # Get `fun`'s info.
    fun__module = _sys.modules[fun.__module__]
    fun__name: str = fun.__name__

    # Figure out the new name for `not_fun`.
    not_fun__name: str = ""
    for (old_prefix, new_prefix) in replace_prefix:
        if fun__name.startswith(old_prefix):
            not_fun__name = new_prefix + fun__name.removeprefix(old_prefix)
            break

    # Define attributes of `not_fun`.
    not_fun.__name__: str = not_fun__name
    not_fun.__doc__: str = f"The logical inverse of `{fun__module}.{fun__name}`."

    # Add `not_fun` to `fun`'s module.
    setattr(fun__module, not_fun__name, not_fun)

    # And we're done!
    return fun
