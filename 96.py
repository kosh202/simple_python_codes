def sum2(nums):
  soma = []
  if len(nums) >= 2:
    soma.append(nums[0] + nums[1])
    return soma
  else:
    if len(nums) == 1:
      soma.append(nums)
      return soma
    if len(nums) <= 0:
      nums.append(0)
      soma.append(nums)
      return soma

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))
print(sum2([0, 0, 0]))
print(sum2([]))
print(sum2([1]))