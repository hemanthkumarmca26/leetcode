class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers cannot be palindromes (e.g., -121 reads as 121-)
        # Numbers ending in 0 (except 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_num = 0
        original = x
        
        # Reverse the integer mathematically without converting to a string
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
            
        # Check if the reversed number matches the original input
        return original == reversed_num
View less
