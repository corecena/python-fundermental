# /* algorithm for binary search   get the length of the list , 
# get the middle element after sorting, get the search element
# if search element is less than middle then search the lower part else search the upper part 
#  return the address of the required elemeent or return  -1 */
searchList = list(range(0,10))
searchItem = 6
setflag =False

length_of_list = len(searchList)
middle_point = int(length_of_list)/2
print("value at the middle is ", searchList[middle_point])
for i in searchList:
    if i==searchItem:
        setflag =True
        
if(setflag):
    print(f"the required element found at ",searchList[i])
else:
    print(f"the search item is not in the list")

      
print(searchList)
