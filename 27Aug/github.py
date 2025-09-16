

print("Check given string is palindrome or not")
def palindrome(s):
    n = len(s)
    for i in range(n//2):
        if(s[i]!=s[n-i-1]):
            return False

    return True


word = "madam"
if(palindrome(word)): print("palindrome")
else: print("Not palindrome")


print("Check given number is prime or not")
def isPrime(num,divisor=2):
    if(num == 1): return False

    if(num%divisor==0): return False

    if(divisor*divisor > num): return True

    return isPrime(num,divisor+1)
print(isPrime(8))



# check strong number
print("Check Strong Number")

# Function to calculate factorial of a digit
def factorial(digit):
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    return fact

# Function to check if number is Strong
def strong(num):     # e.g. 145 → 1! + 4! + 5!
    temp = num  # store original number
    sumFactorial = 0

    while num > 0:
        digit = num % 10
        sumFactorial += factorial(digit)
        num = num // 10

    return sumFactorial == temp

print(strong(145))  # True (145 is a strong number)
# print(strong(123))  # False
