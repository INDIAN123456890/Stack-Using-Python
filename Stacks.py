def push(arr,val,top,max):
    if top == None:
        arr.append(val)
        top = 0
        return arr,top
    else:
        if top == max - 1:
            print("Overflow")
            return arr, top

        top +=1
        arr.append(val)
        return arr,top

def pop(arr,top):
    if top == 0:
        arr = []
        top = None
        return arr,top
    else:
        if top == None:
            print("Underflow")
            return arr,top

        arr.remove(arr[top])
        top -= 1
        return arr,top

def peek(arr,top):

    if top == None:
        print("The stack is empty.")

    else:
        print(f'The top most value in the stack is: {arr[top]}')

if __name__ == '__main__':

    stack = []
    top = None
    max = int(input("Enter the max size of the stack: "))

    x = int(input("Enter 1 for push, 2 for pop, 3 for peek or 4 to exit: "))
    if x == 1 or x == 2 or x == 3:
        while x != 4:
            if x == 1:
                val = int(input("Enter the value: "))
                stack,top = push(stack,val,top,max)
                print(stack)
                x = int(input("Enter 1 for push, 2 for pop, 3 for peek or 4 to exit: "))

            elif x == 2:
                stack,top = pop(stack,top)
                print(stack)
                x = int(input("Enter 1 for push, 2 for pop, 3 for peek or 4 to exit: "))

            elif x == 3:
                peek(stack,top)
                x = int(input("Enter 1 for push, 2 for pop, 3 for peek or 4 to exit: "))

            else:
                print("You gave the wrong input.")
                break

        print("Thanks for using this.")

    elif x != 4:
        print("You gave the wrong input.")

    else:
        print("You clicked on 4 to exit")