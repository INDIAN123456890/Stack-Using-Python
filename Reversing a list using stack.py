def reverse(arr1,arr2,top):

    while top >= 0:
        val = arr1[top]
        arr2.append(val)
        top -= 1

    print(f'Reversed array is: {arr2}')

if __name__ == '__main__':

    stack = []
    top = None

    n = int(input("Enter the size of the array: "))

    for i in range(n):
        stack.append(int(input("Enter the value for array: ")))

    arr2 = []
    top = len(stack)-1
    print(top)
    reverse(stack,arr2,top)