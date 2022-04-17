course_name = "python \"programming"
# print(len(course_name))
# print(course_name[0:3])
# print(course_name[:])
# first = "wanzu"
# last = "sinani"
# full = f" {first}  {last}   "
# print(full.strip()) 
# print(full.replace("a","isis"))
# print("pro" in course_name)
# print("swift" not in course_name)
# x=input("enter X:")
# y= int(x) +34 
# print(f" x : {x} , y : {y}")
# print(course_name[1:-1])
# if len(course_name)>10:
#     print("what a lengthy name")
# elif len(course_name)>14:
#     print("nothing to do")
# else: print("leaarn javascript first")
count =0
for x in range(1,10):
    if(x%2==0):
        count+=1
        print(x)
print(f" we are {count} in this range ")
items =[
    ("product1",9),
    ("product2",9),
    ("product3", 2)
]
#using the map and filter function , and lambda expression  lambda arguments: expression
prices =list(map(lambda item:item[1],items))
print(prices)
#using the list expression 
prices = [item[1] for item in items]
filtered = list(filter(lambda item:item[1]>2 , items))
print(filtered)
filtered = [item for item in items if item[1]>2]
items.sort( key = lambda item: item[1])
print(items[0])
