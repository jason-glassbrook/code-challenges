#!python3

import re
from collections import deque as Deck


class Solution:

    OPENING_BRACE = "["
    CLOSING_BRACE = "]"
    PATTERN__COUNT = r"\d+"
    PATTERN__OPENING_BRACE = re.escape(OPENING_BRACE)
    PATTERN__CLOSING_BRACE = re.escape(CLOSING_BRACE)
    PATTERN = re.compile(
        r"(?P<count>{})(?P<opening>{})|(?P<closing>{})".format(
            PATTERN__COUNT,
            PATTERN__OPENING_BRACE,
            PATTERN__CLOSING_BRACE,
        )
    )

    def decodeString__match(self, encoded_string: str):
        """
        Match the most deeply nested part of the encoded string.
        """
        # @@ inspired by <https://stackoverflow.com/a/23561129/3281405>

        stack = Deck()

        for match in self.PATTERN.finditer(encoded_string):

            # -- we matched something! figure out what it is...

            groups = match.groupdict()
            brace = "opening" if groups["opening"] else "closing"
            index = match.start(brace)

            if encoded_string[index - 1] == r"\\":

                continue

            if brace == "opening":

                # -- we found the beginning of an encoded part
                # 1. process the current match into opening part
                # 2. push the opening part to the stack
                # 3. continue searching for matches

                count = int(groups["count"])
                count__start = match.start("count")
                embraced__start = index + len(self.OPENING_BRACE)

                stack.append((count, count__start, embraced__start))

                continue

            if brace == "closing":

                if stack:

                    # -- we found the ending of an encoded part
                    # 1. pop the last opening part from the stack
                    # 2. process the current match into the closing part
                    # 3. process the opening part and closing part into the decoded data
                    # 4. return the decoded part

                    (count, count__start, embraced__start) = stack.pop()

                    embraced__stop = index
                    embraced = encoded_string[embraced__start : embraced__stop]

                    decoded = (count, embraced)
                    decoded__start = count__start
                    decoded__stop = embraced__stop + len(self.CLOSING_BRACE)

                    return (decoded, decoded__start, decoded__stop)

                else:

                    print(f"Missing the opening brace for the closing brace at {index}.")

                    continue

        if len(stack) > 0:

            for (count, index) in stack:

                print(f"Missing the closing brace for the opening brace at {index}.")

        return None

    def decodeString(self, encoded_string: str) -> str:

        decoded_string = encoded_string
        maybe_more_to_decode = True

        while maybe_more_to_decode:

            match = self.decodeString__match(decoded_string)

            if match:

                ((count, embraced), start, stop) = match

                decoded_string = "".join((
                    decoded_string[: start],
                    embraced * count,
                    decoded_string[stop :],
                ))

            else:

                maybe_more_to_decode = False

        return decoded_string
