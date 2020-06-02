#!python3

# import math
import os


def triangle(n):
    return sum(i for i in range(1, n + 1))


def windows_iter(iterable, width, start=0, stop=None, step=1):
    if stop is None:
        stop = len(iterable)
    for window_start in range(start, stop - width + 1, step):
        window_stop = window_start + width
        yield (
            iterable[window_start : window_stop],
            window_start,
            window_stop,
        )
    return


# Complete the sherlockAndAnagrams function below.
#--- FAST? ---#


def sherlockAndAnagrams(string):
    pairs = dict()
    for width in range(1, len(string)):
        for (substring, *rest) in windows_iter(string, width):
            key = "".join(sorted(substring))
            if key in pairs:
                pairs[key] += 1
            else:
                pairs[key] = 0    # we've only found the key, not a repeat
    pairs_count = 0
    for n in pairs.values():
        pairs_count += triangle(n)
    return pairs_count


# #--- TOO SLOW ---#
#
# import re
#
#
# def counter_dict(iterable):
#     counter = dict()
#     for item in iterable:
#         if item in counter:
#             counter[item] += 1
#         else:
#             counter[item] = 1
#     return counter
#
#
# NOT_ALPHANUMERIC = re.compile(r"[^\w\d]")
#
#
# def counter_dict_to_key(counter):
#     everything = str(sorted(counter.items()))
#     alphanumeric = NOT_ALPHANUMERIC.sub("", everything)
#     return alphanumeric
#
#
# def counter_key(iterable):
#     return counter_dict_to_key(counter_dict(iterable))
#
#
# def is_anagram(a, b):
#     if len(a) == len(b) and counter_dict(a) == counter_dict(b):
#         return True
#     return False
#
#
# # Complete the sherlockAndAnagrams function below.
# def sherlockAndAnagrams(string, verbose=False):
#     count = 0
#     for width in range(1, len(string)):
#         start_a = 0
#         for window_a in windows_iter(string, width, start=start_a):
#             start_b = start_a + 1
#             for window_b in windows_iter(string, width, start=start_b):
#                 if verbose: print("{!r} ~ {!r}".format(window_a, window_b))
#                 if is_anagram(window_a, window_b):
#                     count += 1
#                     if verbose: print("-> is a unique anagram -> count = {!r}".format(count))
#                 start_b += 1
#             start_a += 1
#     return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
