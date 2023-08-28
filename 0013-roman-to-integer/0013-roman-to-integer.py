class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals={
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                result -= roman_numerals[s[i]]
            else:
                result += roman_numerals[s[i]]

        return result