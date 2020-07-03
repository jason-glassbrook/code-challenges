#!python3

from collections import deque as Deck


class Solution:

    def isValid(self, s: str) -> bool:

        return self.isValid__v1(s)

    #===========================================================
    #   Braces Specification
    #-----------------------------------------------------------

    ROUND_ID = 0
    SQUARE_ID = 1
    CURLY_ID = 2

    OPENING_PART = 0
    CLOSING_PART = 1

    BRACES = {
        "(": (ROUND_ID, OPENING_PART),
        ")": (ROUND_ID, CLOSING_PART),
        "[": (SQUARE_ID, OPENING_PART),
        "]": (SQUARE_ID, CLOSING_PART),
        "{": (CURLY_ID, OPENING_PART),
        "}": (CURLY_ID, CLOSING_PART),
    }

    #===========================================================
    #   Solutions
    #-----------------------------------------------------------

    def isValid__v1(self, s: str) -> bool:

        stack = Deck()    # -- records unmatched opening braces.

        # Move through all characters in string `s`:

        for c in s:

            # Try matching `c` to a brace.
            curr_brace = self.BRACES[c] if c in self.BRACES else None

            if curr_brace:

                curr_brace__id, curr_brace__part = curr_brace

                # We can always use an opening brace:

                if curr_brace__part == self.OPENING_PART:

                    stack.append(curr_brace)
                    continue

                # ... Now `curr_brace__part == self.CLOSING_PART` ...

                if stack:
                    # We must have a matching closing brace.
                    prev_brace = stack.pop()
                    prev_brace__id, prev_brace__part = prev_brace

                    if curr_brace__id == prev_brace__id:
                        # Note: We don't need to check `prev_brace__part`. It will always equal to `self.OPENING_PART`.

                        # `curr_brace` and `prev_brace` annihilate like matter and antimatter.
                        continue

                    else:
                        # We found an unmatched opening/closing brace 😢
                        return False

                else:
                    # We found an unmatchable closing brace 😢
                    return False

            # else:
            #     # `c` isn't a brace, so move on.
            #     continue

        # One last check...

        if stack:
            # We have unmatched opening braces 😭
            return False

        # We made it!
        return True
