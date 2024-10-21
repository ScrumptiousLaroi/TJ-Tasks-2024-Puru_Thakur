def compress(chars):
   #write your code here
   counter = 0 #to check for discontinuity in chars
   s = []
   if chars[0] == chars[-1]:
       s.append(chars[0])
   else:
       s.append(chars[0])
       for i in range(len(chars)):
           if chars[i] != chars[i - 1]:
               counter += i + 1
               if counter < 10:
                    s.append(counter)
           
       
   return len(s)
       
       


if __name__ == "__main__":
    chars = ["a","a","b","b","c","c","c"]
    newSize = compress(chars)
    print("New length:", newSize)
    print(chars[:newSize])