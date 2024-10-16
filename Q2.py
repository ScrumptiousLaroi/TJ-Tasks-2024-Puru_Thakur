
def climb_stairs(n):
  #write your code here
    if n == 1:
      return 1
    elif n == 2:
       return 2
    else:
        return climb_stairs(n-1) + climb_stairs(n-2) # Fibonacci series logic

  


if __name__ == "__main__":
    n = 2
    print(climb_stairs(n))
