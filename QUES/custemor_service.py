'''to create the customer servive add customer into que once the customer is served he has to tbe removed from rthe
 queue'''


from collections import deque
queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueuing:",queue)
first = queue.popleft()
print("Dequeued element:",first)
print("Queue after dequeuing:",queue)
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Front element:",queue[0])
num = int(input("num of customers at cs "))
for i in range (num):
    temp = input("enter the customer name: ")
    queue.append(temp)
print(" *after service* ")
for i in range(num):
    t = queue.popleft()
    print(f"customer {i+1} received the service")
print("not empty") if bool(queue) else print("empty")