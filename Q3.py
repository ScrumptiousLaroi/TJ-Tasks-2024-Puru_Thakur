def search_range(nums, target):
  #write your code here
  start = 0
  end = 0
  counter = 0
  for i in range(len(nums)):
      for j in range(i, len(nums)):
          if nums[j] == target:
              counter += 1
              if counter == 1 and start == 0:
                  start = j
              end = j
              break
          
  if start == 0 and end == 0:
      start = -1
      end = -1
  return [start, end]
  


    



if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(search_range(nums, target))