#Queue program for management of api requests
import requests
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
        print("poped element : " + queue.pop(0))
    else:
        print('empty list')
#End Queue operations

print("Handling API Request")
url = 'http://localhost/rmlowweb/test.php'
myobj = {'api_key': '1'}

x = requests.post(url, data = myobj)

def convert(lst):
    return ([i for item in lst for i in item.split()])

lst = [x.text]
con_list = convert(lst)

print("--------------------------------------------------")
print("--------------------------------------------------")
print("Testing insertion upto the max limit")
for j in range(0,len(con_list)):
    err_code = InsertIntoQueue(con_list[j])
    if err_code == 0:
        break
print("--------------------------------------------------")
print("--------------------------------------------------")
print("Removal test of the queue until the last 2 element")
for i in range(0, len(queue) - 2):
    popDataFromQueue()

print("--------------------------------------------------")
print("--------------------------------------------------")
print('Printing the rest of the element in the queue')
print(queue)