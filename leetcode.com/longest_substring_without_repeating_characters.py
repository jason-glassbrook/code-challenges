#!python3


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        w__left = 0
        w__chars = dict()
        answer = 0

        for (w__right, c) in enumerate(s):

            if c in w__chars and w__chars[c] >= w__left:

                w__left = w__chars[c] + 1

            w__chars[c] = w__right
            answer = max(answer, w__right - w__left + 1)

        return answer

    def lengthOfLongestSubstring__submission_1(self, s: str) -> int:

        s__len = len(s)
        w__left, w__right = 0, 0
        w__chars = set()
        answer = 0

        while w__left < s__len and w__right < s__len:

            if s[w__right] not in w__chars:

                w__chars.add(s[w__right])
                w__right += 1
                answer = max(answer, w__right - w__left)

            else:

                w__chars.remove(s[w__left])
                w__left += 1

        return answer
