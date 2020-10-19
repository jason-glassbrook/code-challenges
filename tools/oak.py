#!python3

############################################################
#   OAK (Of A Kind)
#-----------------------------------------------------------
#   A module of tools for type-checking.
############################################################

import sys as _sys
from collections import abc as _abc

from . import twine as _twine
from . import decor as _decor

#-----------------------------------------------------------

_DLI_FUN_TYPE = _abc.Callable[..., bool]
_DLI_REPLACE_TYPE = _abc.Iterable[tuple[str, str, str, bool]]
_DLI_REPLACE_DEFAULT = (
    # (position: str, old_sub: str, new_sub: str, stop_after: bool)
    ("<", "is_", "isnt_", True),
    ("<", "", "not_", True),    # ⬅ Fallback option.
)

_DLI_METHODS = {
    "<": {
        "contains": _twine.contains_prefix,
        "replace": _twine.replace_prefix,
    },
    "*": {
        "contains": _twine.contains,
        "replace": _twine.replace,
    },
    ">": {
        "contains": _twine.contains_suffix,
        "replace": _twine.replace_suffix,
    },
}


@_decor.double_decor
def def_logical_inverse(
    fun: _DLI_FUN_TYPE,
    replace: _DLI_REPLACE_TYPE = _DLI_REPLACE_DEFAULT,
):
    """
    Decorator that defines the "notted" (logical inverse) of the decorated function.

    Optionally accepts `replace`, which is an iterable with items of the form:
    `(position: str, old_sub: str, new_sub: str, stop_after: bool)`.

    The replacements in `replace` are attempted in order, one at a time.

    The `position` parameter specifies where to replace `old_sub` with `new_sub`
    -- it can be `"<"` (prefix), `"*"` (anywhere), or `">"` (suffix).

    The `stop_after` parameter specifies whether the replacement process should
    stop after the given replacement has been _successfully_ performed.

    The default value for `replace` is:
    ```
    (
        ("<", "is_", "isnt_", True),
        ("<", "", "not_", True),
    )
    ```
    """

    # Define generic logical inverse function, `not_fun`.
    def not_fun(*args, **kwargs):
        return not fun(*args, **kwargs)

    # Get `fun`'s info.
    fun__module = _sys.modules[fun.__module__]
    fun__name: str = fun.__name__

    # Figure out the new name for `not_fun`.
    not_fun__name: str = ""
    for (position, old_slug, new_slug, stop_after) in replace:
        methods = _DLI_METHODS[position]
        if methods["contains"](fun__name, old_slug):
            not_fun__name = methods["replace"](fun__name, old_slug, new_slug)
            if stop_after:
                break

    # Define attributes of `not_fun`.
    not_fun.__name__: str = not_fun__name
    not_fun.__doc__: str = f"The logical inverse of `{fun__module}.{fun__name}`."

    # Add `not_fun` to `fun`'s module.
    setattr(fun__module, not_fun__name, not_fun)

    # And we're done!
    return fun
