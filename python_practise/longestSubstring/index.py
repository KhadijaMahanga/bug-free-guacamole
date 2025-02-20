class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenght_long_string = 0
        
        sub = ""
        for c in s:
            if c in sub:
                sub = sub[sub.index(c) + 1:]
            else:
                sub += c
        
            if len(sub) > lenght_long_string:
                    lenght_long_string = len(sub)

        return lenght_long_string



# best solution
# class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     char_set = set()
    #     left = max_len = 0

    #     for right in range(len(s)):
    #         while s[right] in char_set:
    #             char_set.remove(s[left])
    #             left += 1

    #         char_set.add(s[right])
    #         max_len = max(max_len, right - left + 1)

    #     return max_len        