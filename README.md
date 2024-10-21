# TJ-Tasks-2024-Puru_Thakur
## Technojam Auditions tasks for DSA in python

### Q1 Pascal's Triangle 
1) I tried accessing the last row in each iteration but im excluding the last element (i.e. 1) and then I append last rows adjacent elements sum in each iteration (except the last element) after the loop I append last element (i.e.) and store it in triangles variable
2) I initially had problem accessing the last element of an array. Here, "triangle" is my global array which is storing every row which iterates and provides a row of pascal triangle, "row" is my temporary variable which resets after every iteration
3) Solution: <img width="908" alt="Screenshot 2024-10-16 at 8 08 06 PM" src="https://github.com/user-attachments/assets/7487e39d-ea7c-4088-9a40-63d3649b9965">

### Q2 You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 step or 2 steps. In how many distinct ways can you climb to the top?
1) This relates to fibonacci sequence logic that number of ways you can climb a stair is sum of ways you can climb last and 2nd last stair
2) I approached to this logic from a theoretical maths question back while preparing for jee, I applied the same logic in code. (using recursion)
3) Solutions: 
<img width="793" alt="Screenshot 2024-10-16 at 8 12 36 PM" src="https://github.com/user-attachments/assets/2f7ce764-496e-4120-b86d-0262f7a3acc7"> Here number of stairs = 5

### Q3 Find starting and ending position of a given target value in an sorted array
1) in this we initialize the starting index in start variable but we kept updating the ending index in end variable till the end
2) loop keeps iterating, when counter = 0 and start = 0, we initialize start = current index and update end value of current index and break out of that loop, but I have nestedloops so it would still preserve the index after break in the inner most loop
3) in the next iterating innermost loop would start from the next index (due to same nested loops) , from which we break the loop in last iteration
4) Major difficulty I faced in this was how to preserve the index value after using a break statement
5) 
<img width="878" alt="Screenshot 2024-10-21 at 10 42 08 PM" src="https://github.com/user-attachments/assets/eb1e68ce-05c4-4d00-b051-04ac3fe9f14e">

### Q4. String Compression
1) For this I initialized an empty string and took care of first case where a single element is present so I dont have to print 1 in the compressed string just the element char I did that by checking if first and last statement is equal or not
2) In other cases , i initialized a counter varible which subtracts from index i(when there is a discontinuity in list) this gives count of the character in the list
3) for last char type, i initalize a last_char variable which would always update to +1 (in every iteration when the list is continuous wrt to previous element) but it will append to string s only when index is on its last iteration
4) on the last iteration I add an extra 1 to last_char since indexing is done from 0 and we need count
5) Problem I faced solving this was on how to handle the last char type and how to handle case when count is >= 10
6) <img width="897" alt="Screenshot 2024-10-21 at 11 06 28 PM" src="https://github.com/user-attachments/assets/9100ed46-7be0-42fc-98e3-2133e917a88e">

