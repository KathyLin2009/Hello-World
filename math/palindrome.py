"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
def check_palindrome(num):
    copy = num
    temp = 0
    while num >0:
        temp = temp *10 + num%10
        num = num//10
    
    return temp == copy


import unittest
class TestSum(unittest.TestCase):

    def test_true(self):
        self.assertTrue(check_palindrome(1))
        self.assertTrue(check_palindrome(0))
        self.assertTrue(check_palindrome(2))
        self.assertTrue(check_palindrome(11))
        self.assertTrue(check_palindrome(101))
        self.assertTrue(check_palindrome(1001))
    
    
    def test_false(self):
        self.assertFalse(check_palindrome(10))
        self.assertFalse(check_palindrome(12))
        self.assertFalse(check_palindrome(100))
        self.assertFalse(check_palindrome(1000))

if __name__ == '__main__':
    #unittest.main()
    number = input("Please input a number: ")
    number = int(number)
    print(check_palindrome(number))