#20CE146
#Practical 5
'''You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
Sample Input: HackerRank.com presents "Pythonist 2".'''
def swap_case(str):
    ans = str.swapcase()
    return ans

if __name__ == '__main__':
    str = input()
    ans = swap_case(str)
    print(ans)