import time
import execjs
# time.time()
# a=time.time()
# b=execjs.eval('new Date')
# execjs.eval("Date.now()")
# print(execjs.eval("Date.now()"))
# a=execjs.eval("new Date()")
# # u'2018-09-08T09:11:35.248Z'
#
# js = """
# function add(x, y){
#     return x + y;
# }
# """
# ctx = execjs.compile(js)
# d=ctx.call("add", 3, 4)
# print(d)
# print(time.time())
# print(a,b)
# def bubbleSort(nums):
#     for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
#         for j in range(len(nums)-i-1):  # ｊ为列表下标
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums
#
# nums = [5,2,45,6,8,2,1]
#
# print(bubbleSort(nums))
# b=time.time() - a
# print(b)
# print(time.asctime(time.localtime(b)))
# c=time.localtime(b)
# print(c)
# a='https://www.qichacha.com/firm_80af5085726bb6b9c7770f1e4d0580f4.html'
# print(len(a))
import re
ar="certRecord"
br=re.sub('(R\w+)','ajax',ar)
print(br)

