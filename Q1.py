def generate_pascal_triangle(n):
    #write your code here
    triangle = [] # Initialize an empty list to store all the rows of triangle
    for i in range(n):
        row = [1] # Initialize the first element of the row
        if triangle:
            last_row = triangle[-1]
            for _ in range(len(last_row) - 1): # we are excluding the last element we need to access adjacent elements
                row.append(last_row[_] + last_row[_ + 1])
            row.append(1) # to put last element as 1
        triangle.append(row)
    
    return triangle

            

if __name__ == "__main__":
    n = 5
    triangle = generate_pascal_triangle(n)
    for _ in triangle:
        print(_)
