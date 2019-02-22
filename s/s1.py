import os
os.mkdir("作业")
f=open("D:/six3/s/作业/tet.txt",'w+')
for i in range(10):
    f.write("hello world\n")

f.seek(0)
s=f.read(100)
print(s)
f=open("D:/six3/s/作业/tet2.txt",'w+')
for i in s:
    f.write(i)
f.close()