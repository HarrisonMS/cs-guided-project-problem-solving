"""
Given an integer value `n`, write a function that will return a list of the string representation of numbers from 1 to `n`.

However, there are a few additional rules to follow:

- For multiples of three, it should output "Lambda" instead of the number.
- For multiples of five, it should output "School" instead of the number.
- For numbers which are multiples of three and five, it should output "LambdaSchool" instead of the number.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Lambda",
    "4",
    "School",
    "Lambda",
    "7",
    "8",
    "Lambda",
    "School",
    "11",
    "Lambda",
    "13",
    "14",
    "LambdaSchool"
]
"""
# def lambda_school(n):
#     # Your code here
#     new_list = []
#     for i in range(1, n+1):
#         if i % 15 == 0:
#             new_list.append('LambdaSchool')
#         elif i % 3 == 0:
#             new_list.append('Lambda')
#         elif i % 5 == 0:
#             new_list.append('School')
#         else:
#             new_list.append(str(i))
#     return new_list

def lambda_school(n):
    list1 = list(range(1,n+1))
    for index, x in enumerate(list1):
        if x%3 == 0 and x%5 == 0:           list1[index]="LambdaSchool"
        elif x%3 == 0:
            list1[index] = "Lambda"
        elif x%5 ==0:
            list1[index] = "School"
    return list1
print(lambda_school(15))
