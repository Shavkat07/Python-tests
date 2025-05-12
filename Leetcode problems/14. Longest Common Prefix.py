"""
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


class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		common_prefix = strs[0]
		if not common_prefix:
			return ""
		for i in strs[1::]:
			for let_idx in range(len(common_prefix)):
				if let_idx >= len(i):
					common_prefix = common_prefix[:let_idx]
					break
				elif i[let_idx] == common_prefix[let_idx]:
					continue
				else:
					common_prefix = common_prefix[:let_idx]
					if not common_prefix:
						return ""
					break


		return common_prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flofw","flight", "flasdfg"]))
print(sol.longestCommonPrefix(['av', 'a']))
