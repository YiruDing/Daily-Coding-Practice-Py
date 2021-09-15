# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# Solution
def products(array):
    prefix_products = []
    for num in array:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    
    suffix_products = []
    for num in reversed(arrays):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))
   
result = []
for i in range(len(array)):
    if i == 0:
        result.append(suffix_products[i + 1])
    elif i == len(array) - 1:
        result.append(prefix_products[i - 1])
    else:
        result.append(prefix_products[i - 1] * suffix_products[i + 1])
return result

#    What is difference between reverse and reversed in Python?
# reverse() actually reverses the elements in the container. 
# reversed() doesn't actually reverse anything, it merely returns an object that can be used to iterate 
# over the container's elements in reverse order. If that's what you need, it's often faster than actually reversing the elements.

# A MUCH BETTER SOLUTION
# https://www.geeksforgeeks.org/a-product-array-puzzle/?fbclid=IwAR1hzUZTjurSIOBzehnnyEqLq6esMWzhuS_68iJ3K02helXYxWExjkpbiuA
