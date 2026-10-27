from array_list import ArrayList

print('hello')
lst = ArrayList()
lst.add("a")
lst.add("b")
lst.add("c")

print(lst.size())            # 3
print(lst.getIndex("b"))     # 1
print(lst.remove(1))         # "b"
print(lst.size())            # 2
print(lst.get(1))            # "c"   (the c moved up)
print(lst.getIndex("b"))     # -1
print(lst.set(0, "z"))
print(lst.get(0))            # "z"
print(lst.get(2))            # IndexError