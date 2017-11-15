def coin_check(n,i):

	if n==1 or n==2 or n==4:
		return i
	
	elif n==3:
		return i*-1
	
	else:
		if coin_check(n-1,i*-1)==i or coin_check(n-2,i*-1)==i or coin_check(n-4,i*-1)==i:
			return i
		else:
			return i*-1


n=int(input())
if coin_check(n,1)>0:
	print("Alice")
else:
	print("Bob")

		
		