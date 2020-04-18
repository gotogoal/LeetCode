class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		for each in ransomNote:
			if each in magazine and ransomNote.count(each) <= magazine.count(each):
				continue
			else:
				return False
		return True


if __name__ == '__main__':
	solution = Solution()
	print(solution.canConstruct("a", "b"))
	print(solution.canConstruct("aa", "ab"))
	print(solution.canConstruct("aa", "aab"))
