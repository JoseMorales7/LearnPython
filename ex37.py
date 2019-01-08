from sys import argv  ## this gets a number from the terminal

script, arg = argv    ##this stores that number from the terminal and then typecasts it to a int
n = int(arg)              

for i in range( 1, n ):         ## this tells whether or not a number is a perfect square root. it does this  
    if n//i == i and n%i == 0:  ## by floor dividing n by i and if that is equal to i and n mod i is 0 then its a perfect square root 
        print(n//i)             ##If it is a perfect square root then it prints the square root then exits the program.
        exit(0)                 
        
print(False)  ## this just prints false it not a square root