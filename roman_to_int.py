class Solution:
    def romanToInt(self, s: str) -> int:
        roman_letters = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        integer_num = 0
        prev_val = 1000
        for x in s:
            #print(x)
            if prev_val < roman_letters[x]:
                integer_num -= prev_val
                integer_num = integer_num + (roman_letters[x] - prev_val)
            else:
                integer_num = integer_num + roman_letters[x]
            prev_val = roman_letters[x]
        #print("ans", integer_num)
        return integer_num


roman = "MMIM"
a = Solution()
ans = a.romanToInt(roman)
print("ans",ans)

