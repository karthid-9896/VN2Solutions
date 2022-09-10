'''
1. Implement palindrome using iterator(for loop) and generator mechanism.'''
print("---------------------program 1--------------------------")

x="malayalam"
g=""    
   
    
def Generator(x):
    for i in x[::-1]:
        yield i
               
for i in Generator(x): 
    g+=i
    
if g==x:
    print("yes ,it is Palindrome")
else:
    print("No ,it is not Palindrome")



print("---------------------program 2--------------------------")
'''
2.Sum of 2 digits into output'''

n1=1234
n2=9999
output=0


if len(str(n1))==len(str(n2)):
    for i in range(len(str(n1))):
        x=str(n1)
        y=str(n2)
        
        output+=(int(x[i])+int(y[i]))
print(output)


'''
3. st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba'''

print("---------------------program 3--------------------------")
st = "ab@#cd!ef"
def reverseString(text):
    index = -1
    for i in range(len(text) - 1, int(len(text) / 2), -1):

        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text



mmm = reverseString(list(st))

print("Output : ", "".join(mmm))


print("---------------------program 4--------------------------")
'''
4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format
'''
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]

d={}
s={}
count=0

for i in some_list:

    if i not in d:
        count=1
        
        d[i]=count
    else:
        d[i]+=1
        
print(d)
print("only with duplicate counts:")
for i,j in d.items():
    if d[i]>1:
        s[i]=j
print(s)

print("---------------------Program 5--------------------------")
'''
5. # t1 = (1, 2, 3, "a", "c") 
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")'''
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
Output=[]
x=[]
y=[]
r=[]
for i in list(t2):
    if type(i)==int:
        x.append(i)
    else:
        y.append(i)
    
z=x+y

for i in range(len(t1)):
    k=list(t1)
    m=k[i]+z[i]
    r.append(m)
output=tuple(r)
print(output)










print("---------------------Program 6--------------------------")
'''
6  #Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196'''

inp = "216.08.094.196"
out=[]
x=inp.split(".")

for i in x:
    
    if i[0]=='0':
        i=i[1:]
        out.append(i)
    else:
        out.append(i)

res=".".join(out)
print(res)


print("---------------------program 7--------------------------")

'''
7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]'''

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
out=[]

for i in l:
    
    if type(i)==list:

        for j in i:
            
            if type(j)==list:
                for k in j:
                    out.append(k)
            else:
                out.append(j)
    
    else:
        out.append(i)
print(out)

print("---------------------program 8--------------------------")

file = open('493.txt', 'r')

txt = file.readlines()
no_lines = len(txt)

print("No.of.lines: ", no_lines)

# no of words in each line
count = 0
for i in txt:
    for j in i:
        if j != " ":
            count += 1
    print("characters :",count)
    count = 0
v="aeiou"
cnts=0
# no of vowels
for i in txt:
    if i in v:
        count+=1
    else:
        cnts+=1
print("vowels :",count)
print("Consonants:",cnts)