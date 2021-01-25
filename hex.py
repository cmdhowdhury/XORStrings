import sys
mode = sys.argv[1]
key = sys.argv[2]
inp = sys.argv[3]
debug = False

if key == "key1":
    key = "A"
elif key == "key2":
    key = "FISH"

if inp == "message1":
    inp = "hello"
elif inp == "message2":
    inp = ")$--."
elif inp == "message3":
    inp = "this is a test"
elif inp == "message4":
    inp = "f=;!5i:;f(s<#:'"  


if(debug):
    print("mode: "+mode)
    print("key: "+key)
    print("inp: "+inp)

if mode == "numOut":
    #inp2 = list(inp)
    for i in list(inp):
        print(hex(ord(i))[2:], end=" ")
else:
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
    

