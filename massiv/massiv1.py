def find_separation_binary(arr):
  left, right = 0, len(arr) - 1
  while left < right:
    mid = (left + right) // 2
    if arr[mid] == 0 and arr[mid + 1] == 1:
      return mid
    elif arr[mid] == 0:
      left = mid + 1
    else:
      right = mid
  return -1

