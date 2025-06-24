'''WAPP to take the length of queue as input add the elements and print the elements present in the queue and remove
 one by one from queue and check whether the queue is empty or not and print the front peek and rear peek
'''
from collections import deque
queue =  deque()

num = int(input("num of customers at cs "))
for i in range (num):
    temp = input("enter the customer name: ")
    queue.append(temp)
print("first elemnent in queue is: ",queue[0])
print("last elemnent in queue is: ",queue[len(queue)-1])
print(" *dequeuing* ")
for i in range(num):
    t = queue.popleft()
    print(f"element {i+1} is popped")
print("not empty") if bool(queue) else print("empty")
