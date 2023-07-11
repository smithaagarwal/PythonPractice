"""""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


class Solution:
    #to determine common prefix,compared letter  by letter of all words, hence its slow
    def longest_common_prefix(self, strs: List[str]) -> str:

        str_len = len(strs[0])
        prefix  = ""
        for i in range(str_len):
            start = strs[0][0:i+1]
            print("start:", start)
            for word in strs:
                print(word)
                if not word.startswith(start):
                    break
            else:
                prefix = start
            if prefix != start:
                break
        print(prefix)
        return prefix

    #used sort function to sort all words in list and then compare just the first and last word to see how much of the prefix match
    def longest_common_prefix_with_sorting_logic(self, strs: List[str]) -> str:
        strs.sort()
        num_of_words = len(strs)
        for i in range(len(strs[0])):
            if strs[0][i] != strs[num_of_words-1][i]:
                break
        else:
            return strs[0]
        if i == 0:
            return ""
        return strs[0][0:i]


s = Solution()
strs = ["flower","flow","flight"]
prefix = s.longest_common_prefix_with_sorting_logic(strs)
print("common prefix",prefix)

