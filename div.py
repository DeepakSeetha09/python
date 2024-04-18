def div_ab(a,b):
    if b == 0:
        return None
    q = a // b
    r = a % b
    if r == 0:
        return q
    res=[str(q),"."]
    rem_map={}
    while r !=0:
        if r in rem_map:
            res.append(')')
            return "".join(res)
        rem_map[r]=len(res)
        r=r*10
        q=r//b
        res.append(str(q))
        r=r%b
    return res
a = int(input("enter a"))
b = int(input("enter b"))
ans = div_ab(a,b)
print("ans : ",ans)
 
