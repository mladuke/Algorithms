# Input : string => Non empty string of lower case letters
# Input : key => Non negative integer to shift input string by
# Output : lower case string, wrapped around if necessary
# Ex : Input => "xyz",2 : Output => "zab"
def caesarCipherEncryptor(string, key):
    # Write your code here.
	newString=""
	aAscii= ord('a')
	for letter in string:
		newString += chr((ord(letter)-aAscii+key)%26 +aAscii)
	return newString	