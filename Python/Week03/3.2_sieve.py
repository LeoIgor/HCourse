# -*- coding: utf-8 -*-

def sieve(n):
	p = 2
	
	nums = list(range(2,n+1))
	
	counter = 0
	
	while True:
		for i in range(p*2,n+1,p):
			if i in nums: nums.remove(i)
		counter += 1
		
		if counter < len(nums):
			p = nums[counter]
		else:
			return nums	

if __name__ == "__main__":
	print(sieve(120))
