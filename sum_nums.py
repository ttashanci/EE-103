num = int(input("Enter a number: "))
running_sum = 0
for i in range(1, num + 1):
    running_sum += i
sum_gauss = num * (num + 1) // 2
if running_sum == sum_gauss:
    print("My running sum code works correctly!")
else:
    print("My running sum code failed badly!")