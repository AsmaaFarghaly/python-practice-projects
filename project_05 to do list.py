tasks=[]
print("To DO list")

while True:
    print("--------------------------")
    print("choose an option: ")
    print("1: add task ")
    print("2: view tasks ")
    print("3: delet task ")
    print("4: exit")
    print("--------------------------")
    
    
    choice = input("enter your choice (1-4): ")
    
    if choice == "1" :
        value =input("enter a task: ")
        tasks.append(value)
        print("task added!")
        
        
        
    elif choice == "2":
        if not tasks:
            print("no taskes yet")
            
        else:
            print("your tasks")
            i =1
            for data in tasks:
                print(i,data)
                i+=1
                
    
    elif choice == "3":
        if not tasks:
            print("no tasks yet")
            
        else:
            print("your tasks: ")
            i=1
            for data in tasks:
                print(i,data)
                i+=1
                
            task_number=int(input("enter task number to delete: "))
            
            if task_number >=1 and task_number <=len(tasks):
                deleted = tasks.pop(task_number-1)
                print(f"deleted task: {deleted}")
                
            print (tasks)
            
                
    elif choice =="4":
        print("goodbye!")
        break
                
    else:
        print("invalid request: try again")