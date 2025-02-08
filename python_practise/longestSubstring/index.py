class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenght_long_string = 0
        
        sub = ""
        i = 0
        while i < len(s):
            if s[i] in sub:
                if len(sub) > lenght_long_string:
                    lenght_long_string = len(sub)
                
                s = s[s.index(s[i]) + 1:]
                sub = ""
                i = 0
            else:
                sub += s[i]
                i+= 1
        if len(sub) > lenght_long_string:
                    lenght_long_string = len(sub)

        return lenght_long_string



# best solution
# class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len        