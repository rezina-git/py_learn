#1 is even?
#2 is even ? True
#3 is even?

def check_if_even(nums):
    for i in nums:
        breakpoint()
        if i%2 == 0:
            return("List contains even",i)
    return ("list doesnot contains even",i)

a =[1,2,3,4,5,6,7,8,9,10]
print(check_if_even(a))
