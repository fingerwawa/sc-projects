"""
File: largest_digit.py
Name: Jael Lin
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the integer.
	:return: int, the biggest digit.
	"""
	n = abs(n)
	digit = len(str(n))
	return find_largest_digit_helper(n, digit)


def find_largest_digit_helper(n, digit):
	if digit == 1:
		return n
	else:
		n1 = n//(10**(digit-1))
		n2 = (n//(10**(digit-2)))-(n1*10)
		if n1 > n2:
			n = n - n1*(10**(digit-1)) - n2*(10**(digit-2)) + n1*(10**(digit-2))
		else:
			n = n - n1*(10**(digit-1))
		return find_largest_digit_helper(n, digit-1)


if __name__ == '__main__':
	main()
