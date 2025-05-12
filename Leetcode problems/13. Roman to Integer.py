"""
Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
	roman_numerals = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000

	}
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		answer = 0
		a = False
		for i in range(len(s)):
			try:
				if self.roman_numerals.get(s[i]) < self.roman_numerals.get(s[i+1]):
					answer += self.roman_numerals.get(s[i+1]) - self.roman_numerals.get(s[i])
					a = True
				else:
					if a:
						a = False
						continue
					answer += self.roman_numerals.get(s[i])
			except IndexError:
				if a:
					break
				answer += self.roman_numerals.get(s[i])
		return int(answer)

sol = Solution()
print(sol.romanToInt(s="VII"))
