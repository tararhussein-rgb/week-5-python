# countdown.py

# Ask the user which number to start from
start_num = int(input("Enter a number to start the countdown: "))

# Use a while loop to count down from start_num to 1
current = start_num
while current > 0:
    print(current)
    current -= 1

# After the loop ends, print "Blast off!" exactly once
print("Blast off!")