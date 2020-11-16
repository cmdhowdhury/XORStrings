import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

if mode == numOut:
    #inp2 = list(inp)
    for i in list(inp):
        print(hex(ord(i))[2:], end=" ")
elif mode == human:
    for (a,b) in zip(list(inp), list(key)):
        print(''.join(chr(ord(a)^ord(b))), end='')

'''
TESTING CODE IN PYTHON

key = 'FISH'
inp = ' this is a test'
inp2 = list(inp)
print(inp2)
for (a,b) in zip(list(inp), list(key)):
    print(''.join(chr(ord(a)^ord(b))), end="")

#print(''.join(chr(ord('F')^ord(' '))), end='')
print(''.join(chr(ord('I')^ord('t'))), end='')
print(''.join(chr(ord('S')^ord('h'))), end='')
print(''.join(chr(ord('H')^ord('i'))), end='')
print(''.join(chr(ord('F')^ord('s'))), end='')
    
print("")
for j in list(key):
    for i in inp2:
        print(''.join(chr(ord(j)^ord(i))), end="")

testing code in python
inp = "this is a test"
inp2 = list(inp)
for i in inp2:
    print(hex(ord(i))[2:], end=" ")
'''    
    

