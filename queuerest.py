#Queue program for management of api requests
import requests
import os
sizeset = 20
queue = []

#Queue operations
def InsertIntoQueue(data):
    if(sizeset == len(queue)):
        print('size exceeded stopping insertion')
        return 0
    else:
        if(data in queue):
            print("element already exists : " + data)
        else:
            print("inserting element : " + data)
            queue.append(data)

def popDataFromQueue():
    if(len(queue) != 0): 
        # print("poped element : " + queue.pop(0))
        os.system(queue.pop(0))
    else:
        print('empty list')
#End Queue operations

print("Handling API Request")
url = 'http://localhost/rmlowweb/test.php'
myobj = {'api_key': '3'}

x = requests.post(url, data = myobj)
err_code = InsertIntoQueue(x.text)
print("--------------------------------------------------")
print("--------------------------------------------------")
print(len(queue))
print("Removal test of the queue until the last 2 element")
for i in range(0, len(queue)):
    popDataFromQueue()

print("--------------------------------------------------")
print("--------------------------------------------------")
print('Printing the rest of the element in the queue')
print(queue)