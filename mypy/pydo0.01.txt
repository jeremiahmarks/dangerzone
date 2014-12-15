

#python todo list modules from jlmarks

thePlan = """
One of the things that I remember most from class is the concept that failure to
plan the application will likely result in the application failing. 

So here is my plan:

    I will start by writing a simple, extensible to do list. 
    
    A top level TodoItem with name=todaysDate will house all of the other
    todo items. In essence, a todo item can hold another todo item. 
    
    Every todo item must have a UID and a name
        
    
    The application will create a "to-do list", add an item or two, print
    the todo list, and then quit.
    
    

"""

class TodoItem:
    
    def __init__(self, uid, name):
        self.name = name
        self.uid = uid
        self.subitems=[]
        
    def addSubitem(self, uid, name):
        self.subitems.append(TodoItem(uid, name))
        
    def printList(self):
        print (self.name)
        for todoitem in self.subitems:
            print todoitem.name

def run():
    uid=1
    theList=TodoItem(uid, "27 Dec 2012")
    theList.addSubitem(uid+1, "This would be the fist item")
    theList.printList()
    
if __name__=="__main__":
    run()
