# check whether the list is palindrome or not

# method 1
list1 = [1,2,3,2,1]
list2 = list1.copy()
list1.reverse()

if (list1 == list2):
    print("Given list is palindrome.")
else:
    print("not a palindrome")

# method 2
l1 = [1,3,4]
if(l1.reverse() == l1):
    print("Given list is palindrome.")
else:
    print("not a palindrome")

# method 3
# for loop
    