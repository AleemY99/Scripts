# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
check_list = [11, 13, 14, 16, 17 , 18 , 19, 20]

def find_solution(step):
	for num in range(step, 10**10, step):
		if all(num % n == 0 for n in check_list):
			return num
	return None

if __name__ == '__main__':
	solution = find_solution(20)
	if solution is None:
		print("Did not find an answer in the specified range.")
	else:
		print("The answer is ", solution)
		