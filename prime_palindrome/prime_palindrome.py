'''
Created on Feb 4, 2015
https://www.codeeval.com/open_challenges/3/

Write a program which determines the largest 
prime palindrome less than 1000.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the largest prime palindrome 
less than 1000.

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
        
def is_palindrome(value):
    # Test forwards and backwards
    if str(value) == str(value)[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    largest_prime_palindrome = 0
    for num in range(0,1000):
        if is_prime(num) and is_palindrome(num):
            largest_prime_palindrome = num
            
    print largest_prime_palindrome
            