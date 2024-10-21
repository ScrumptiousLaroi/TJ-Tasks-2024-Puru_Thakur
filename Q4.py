def compress(chars):
   #write your code here
   counter = 0 #to check for discontinuity in chars
   last_char = 0 #for last character type
   s = []
   if chars[0] == chars[-1]:
       s.append(chars[0])
   else:
       s.append(chars[0])
       k = 0
       for i in range(1, len(chars)):  
        if chars[i] != chars[i - 1]:   
            counter = i - counter  #when ever there is a discontinuity, we subtract counter from current index to get number of times that char was in list
            if counter == 1:
                s.append(chars[i+1])
                last_char = 0
            else:
                s.append(counter)
                s.append(chars[i+1])
                last_char = 0 #since char got appended in this loop its clearly not the last char case so last_char is dismissed
        else:
           last_char += 1
           if i != len(chars) - 1: #this is checking for the last element
              pass
           else:
              last_char += 1 #since i is indexed from 0 but we need the count
              last_char = list(str(last_char)) #this makes sure if count is > 10 it gets converted to individual lists
              s.extend(last_char)  #using extend so that to avoid nested brackets
           
   chars[:] = s
   return len(s)
       
       


if __name__ == "__main__":
    chars = ["a","a","b","b","c","c","c"]
    newSize = compress(chars)
    print("New length:", newSize)
    print(chars[:newSize])