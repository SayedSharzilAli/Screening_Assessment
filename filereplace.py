def funfilereplace(f,x,y):
    
    f = open(f, "r+")
    l = f.readlines()
    c = 0
    for i in l:
        if x in i:
             Replacement = i.replace(x, y)
             l = Replacement
             c += 1
 
    f.truncate(0)
    f.writelines(l)
    f.close()

a = input("enter file name:")
b = input("enter text to be replaced:")
c = input("enter text that will replace:")
funfilereplace(a,b,c)
print("Text successfully replaced")
