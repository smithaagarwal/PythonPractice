from math import *
class Solution:
    def isPalindrome(self, x: int) -> bool:

        rev = 0
        n = x
        while (n > 0):
            rev = rev*10 + (n % 10)
            #print("rv ", rev)
            n = n//10
            #print ("n",n)
        if(x == rev):
            return True
        else:
            return False
        """n = x
        start = 0
        end = 0
        while (n>9) and (start == end):
            length = len(str(n))

            print("length",length)
            start = n//10 ** (length-1)
            end = n % 10
            print("start",start)
            print("end", end)

            n = n // 10
            print("n", n)
            n = n % 10 ** (length-2)
            print("n", n)
            print("length",length,len(str(n)))
            if n!=0:
                if(length-2) != len(str(n)) and n !=0:
                    return False


        if start == end and n >= 0:
            return True
        else:
            return False
            """


s = Solution()
print(s.isPalindrome(100))

print(s.isPalindrome(1000021))

print(s.isPalindrome(1001001))