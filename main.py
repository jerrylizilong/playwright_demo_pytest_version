# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(1,10):
        output = ''
        for j in range(1,i+1):
            output += '%s X %s = %s   ' %(j,i, j*i)
        print(output)
        print('\n')

def calculate():
    print('请输入第一个数组：')
    first = input()

    print('请输入第二个数字：')
    second = input()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
