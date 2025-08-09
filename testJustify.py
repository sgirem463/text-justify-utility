# This program does text justify formatting,
# Usage: python3 textJustify.py <text file name> [width per line, default is 80]
#
# Extra spaces will be distributed as evenly as possible, empty slots on the left will be assigned more spaces
# if even distribution is not possible. The last line of text will be left-justified, no extra space is
#  inserted between words
#
import sys

# input arguments processing
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: python3 textJustify.py <text file name> [width per line, default is 80]")
    exit(1)
if len(sys.argv) == 3:
    if sys.argv[2].isdigit():
        maxWidth = int(sys.argv[2])
    else:
        print("Error: with per line must be an integer.")
        exit(1)
else:
    maxWidth = 80

# open the file and check exception
filename = sys.argv[1]
try:
    f = open(filename)
except FileNotFoundError:
    print("Error: The text file does not exist.")
except Exception as e: # Catching any other unexpected errors
    print(f"An unexpected error occurred: {e}")
else:
    A = [] # for the answer
    with f:
        for paragraph in f:
            words = paragraph.split() 

            # handle blank lines
            if len(words) == 0:
                A.append('\n')
                continue

            n = len(words)
            line = [] # use a list for easier processing, used for each output line
            chars = 0 # number of characters
            for i in range(n):
                w = words[i]

                # accumulated char count + 1 space after each word + length of the next word > maxWidth
                if chars + len(line) + len(w) > maxWidth:
                    spaces = maxWidth - chars
                    if len(line) == 1:
                        # special case, one word per line
                        A.append(line[-1] + ' ' * (maxWidth - len(line[0])))
                    else:
                        # calculate space distribution
                        d = spaces // (len(line)-1)
                        r = spaces % (len(line)-1) # one addition space for first few words 
    
                        # put words and spaces to a sring
                        ll = ''
                        for j in range(len(line) - 1):
                            ll += line[j]
                            ll += ' ' * d
                            if r > 0:
                                ll += ' ' # additional space
                                r -= 1
                        ll += line[-1]
                        A.append(ll)
    
                    # start a new line
                    line = [w]
                    chars = len(w)
                elif i == n-1: # the last word
                    line.append(w)
    
                else:
                    line.append(w)
                    chars += len(w)
    
            if line:
                A.append(' '.join(line))

    # output
    for l in A:
        print(l)

