#!python3

############################################################
#   TWINE
#-----------------------------------------------------------
#   A module of helpful string operations.
############################################################

contains = str.__contains__


def remove(s: str, sub: str) -> str:
    return str.replace(s, sub, "")


replace = str.replace

#-------------------

contains_prefix = str.startswith

remove_prefix = str.removeprefix


def replace_prefix(s: str, old_prefix: str, new_prefix: str) -> str:
    return new_prefix + remove_prefix(s, old_prefix)


#-------------------

contains_suffix = str.endswith

remove_suffix = str.removesuffix


def replace_suffix(s: str, old_suffix: str, new_suffix: str) -> str:
    return remove_suffix(s, old_suffix) + new_suffix


#-------------------
