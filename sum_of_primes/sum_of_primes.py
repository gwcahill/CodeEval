'''
Created on Jan 29, 2015
SUM OF PRIMES
CHALLENGE DESCRIPTION:

Write a program which determines the sum of the first 1000 prime numbers.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the sum of the first 1000 prime numbers.

@author: Grant Cahill
'''

def is_prime(eval_num):
    """Determines if number passed in is a prime value.

    Args:
        eval_num: integer to evaluate

    Returns:
        Boolean value indicating whether or not the value
        is prime.
    """
    if(eval_num<2):
        return False
    else:
        # Loop through possible factors
        for num in range(2,eval_num):
            # If mod operator is 0, then we have a factor and it is not prime
            if eval_num % num == 0:
                return False
        else:
            return True


if __name__ == "__main__":
    # List holding all of the prime values
    prime_list = list()
    
    # variable incrementing through possible primes
    num = 0
    
    # gather first 1000 primes
    while len(prime_list) < 1000:
        num += 1
        if(is_prime(num)):
            prime_list.append(int(num))
    
    # Add up all the primes found        
    tally = 0
    for item in prime_list:
        tally += item
        
    print tally
        