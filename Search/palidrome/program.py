def isPalindrome(string):
    # Write your code here.
	
	i =0
	while (i < len(string)//2):
		if string[i]!=string[-i-1]:
			return False
		else: i += 1
	return True

string = "abcdefghhgfedcba"
print(isPalindrome(string))

string = "abcdefgghgfedcba"
print(isPalindrome(string))