arr=[10,12,13,14]
largest=arr[0]
for i in range(len(arr)):
  if arr[i]>largest:
    largest=arr[i]
print("largest =",largest)
