num=int(input("Enter number of tasks: "))
tasks=[]
for i in range(num):
    l=[]
    l.append(input("Enter name"))
    l.append(input("Enter description"))
    l.append(input("Enter Due"))
    tasks.append(l)

f=open("mini-project\\tasks.csv","w")
# tasks=[]
# t=f.readlines()
# for s in t:
#     s=s[:-1]
#     l=s.split(",")
#     tasks.append(l)
# for i in tasks:
#     print(i)
# f.close()
print("Name\tDescription\tDue")
f.write("Name,Description,Due\n")
for a in tasks:
    for b in range(len(a)):
        print(a[b],end="\t")
        if (b==(len(a)-1)):
            f.write(a[b]+"\n")
        else:
            f.write(a[b]+",")
    print()