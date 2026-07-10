arr=[1,2,3,4,0]
smallest=arr[0]
for i in range(len(arr)):
  if arr[i]<smallest:
    smallest=arr[i]
print("smallest:",smallest)
