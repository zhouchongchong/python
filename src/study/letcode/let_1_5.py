# _*_ coding: utf-8 _*_ 
'''
  @Author: Trent.zhouchong 
  @Date: 2018-08-14 16:40:50 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2018-08-14 16:40:50 
 '''

class Solution:
    def twoSum(self,nums,target):
        for leng in range(len(nums)):
            for sed in range(1,len(nums) - leng -1):
                if target == (nums[leng] + nums[leng+sed]):
                    return [leng,leng+sed]
                else:
                    raise Exception
            







if __name__ == '__main__':
    print('let_1_5')
    nums = [3,4,4,0,5,6]
    target = 6
    for i in range(1,6):
        print(i)
    sol = Solution()
    print(sol.twoSum(nums,target))        