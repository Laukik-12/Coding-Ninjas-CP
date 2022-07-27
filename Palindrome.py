def checkPalindrome(num):
    temp = num
    sum = 0
    while(temp>0):
        sum = sum*10 + temp%10
        temp = temp//10
    if(sum == num):
        return True
    else:
        return False
    pass
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
