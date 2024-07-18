import queue

my_queue = queue.Queue()
# print( my_queue )

numbers_List = [ 2 , 4 , 6 , 8 , 10 ]
for number in numbers_List:
    my_queue.put( number )

print( my_queue.get() )
print( my_queue.get() )
print( my_queue.get() )
print( my_queue.get() )

print("-------------------------------")

myQueue = queue.LifoQueue()   #Lifo means Last Input First Output.
numbersList = [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 ]
for number in numbersList:
    myQueue.put( number )

print( myQueue.get() )
print( myQueue.get() )
print( myQueue.get() )

print("+++++++++++++++++++++++++++++++")

user_Queue = queue.PriorityQueue()
user_Queue.put( ( 3 , "Computer" ) )
user_Queue.put( ( 7 , "Laptop" ) )
user_Queue.put( ( 4 , "Machine" ) )
user_Queue.put( ( 9 , "Cable" ) )
user_Queue.put( ( 1 , "Mobile" ) )
user_Queue.put( ( 5 , "System" ) )
user_Queue.put( ( 8 , "Car" ) )

# print( user_Queue.get() )
# print( user_Queue.get() )

# while not user_Queue.empty():
#     print( user_Queue.get() )

while not user_Queue.empty():
    print( user_Queue.get()[1] )