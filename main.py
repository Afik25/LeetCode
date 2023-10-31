from test import nums, target
from easy.P1_twoSum import twoSum


if __name__ == '__main__':
    result = twoSum(nums, target)
    print('*****'*10)
    print(f'Initial array : {nums}')
    print(f'Result : {result}')