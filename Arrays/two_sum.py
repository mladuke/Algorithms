array = [3,5,-4,8,11,1,-1,6]
targetSum = 10

# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     arrayOut = []
#     for num1 in array:
#         for num2 in array:
#             if (num1+num2==targetSum) and (num1 != num2):
#                 arrayOut.append(num1)
#                 arrayOut.append(num2)
#     finalList =sorted(list(set(arrayOut)))
#     return finalList

# def twoNumberSum(array, targetSum):
# 	# Write your code here.
#     arrayOut =[]
#     newDict = dict.fromkeys(array)
#     for num1 in newDict:
#         num2 = targetSum- num1
#         if (num2 in newDict) and (num1 != num2):
#             arrayOut.append(num1)
#             arrayOut.append(num2)
#             finalList =sorted(arrayOut)
#             return finalList
#     return arrayOut

def twoNumberSum(array, targetSum):
    # Write your code here.
    
    arrayOut =[]
    newDict = {}
    for num1 in array:
        num2 = targetSum- num1
        if (num2 in newDict):
                arrayOut.append(num1)
                arrayOut.append(num2)
                finalList =sorted(arrayOut)
                return finalList
        else:
            newDict[num1]=True
    return arrayOut

# def twoNumberSum(array, targetSum):
#     # Write your code here.
# 	array.sort()
#     left =0
#     right = len(array) -1
# 	while (left < right):
#         currSum = array[left] + array[right]
#         if currSum == targetSum:
#             return [array[left],array[right]]
#         elif currSum < targetSum:
#             left += 1
#         else:
#             right -= 1
#     return []



print(twoNumberSum(array, targetSum))