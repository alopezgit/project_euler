## Code for problem https://projecteuler.net/problem=51
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

import itertools
def replacement_prime(number):

	for L in range(0, len(str(number))+1):
		for subset in itertools.combinations(range(len(str(number))), L):
			if len(subset)>0:
				
				n_primes = 0
				list_primes = []
				for n in range(10):
					number_copy = list(str(number))
					for i in subset:
						number_copy[i] = str(n)
					number_copy = int(''.join(number_copy))
					if len(str(number_copy)) == len(str(number)) and utils.check_prime(number_copy):
						n_primes += 1
						list_primes.append(number_copy)
						if n_primes == 8:
							print list_primes
							return True



check_number = 56003

while True:
	if utils.check_prime(check_number):
		if replacement_prime(check_number):
			print check_number
			break
	check_number += 1
	if check_number % 100:
		print check_number

	