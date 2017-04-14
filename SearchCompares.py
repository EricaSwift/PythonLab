"""Do the Finger Exercise from page 33 of the textbook:
Add dome code to the implementation of N-R to keep track of the number of iterations 
used to find a square root.  Use that code as part of a program to compare the efficiency 
of N-R and bisection search."""


print 'Incremental Search\n'

x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:    
    ans += step    
    numGuesses += 1
print 'numGuesses =', numGuesses
if abs(ans**2 - x) >= epsilon:    
    print 'Failed on square root of', x
else:    
    print ans, 'is close to square root of', x
  
      
print 'Bisection\n'
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:    
    print 'low =', low, 'high =', high, 'ans =', ans    
    numGuesses += 1    
    if ans**2 < x:        
        low = ans    
    else:        
        high = ans    
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x

nrCount=0
print 'Newton-Raphson\n'
#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    nrCount+=1
print 'Square root of', k, 'is about', guess
print 'numGuesses =', nrCount