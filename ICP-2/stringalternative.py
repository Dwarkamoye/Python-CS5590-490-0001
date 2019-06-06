#custom function takes input and processes
def string_alternative(string):
    """convert to list
    str = list([string])"""
    str1 = []
    for a,items in enumerate(string):
        if a % 2 == 0:
            str1.append(items)
    out_str = ''.join(str1[:])
    print(out_str)
    """for i, item in enumerate(str):
        for k, char in enumerate(item):
            if k % 2 == 0:
               str1.append(item[k:k+1])
    out_str = ''.join(str1[:])
    print(out_str)"""
if __name__ == '__main__':
    #passing values on user enter to custom function
    string_alternative(input("Enter the string: "))
