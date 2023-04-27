# prices = [1 , 2, 3, 4, 5]
# print(prices[-4], prices[-5:-2], prices[-3:-4])

# nums1 = (6, 2, 0, 0)
# nums2 = (5, 2, 3, 4)

# print(nums1 > nums2)


# int_a = 3
# float_a = 3.0

# if int_a < float_a:
#     print("False")
# elif int_a > float_a:
#     print("t")

# class Math:
#     def __init__(self, num):
#         self.num = num

# class Number(Math):
#     def __init__(self, num):
#         self.value = num*2
#     def show(self):
#         print(self.value, self.num)

# obj = Number(10)
# obj.show()


try: 
    print(14/0)
    print("88"+1)
except(NameError, TypeError):
    print("Invalid INput")