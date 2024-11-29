#Evan Rhea
# Task manager but with a new GUI!
import tkinter as GUI
import json


# Start of Functionality

task_list = [("Tasks: ")]



def NewTask():
    NewBoi = NTask.get()
    task_list.append(NewBoi)
    Tasks.config(text=task_list)
    print(task_list)


def DeleteTask():
    DelBoi = DTask.get()
    if DelBoi in task_list:
        task_list.remove(DelBoi)
        Tasks.config(text=task_list)
        print(task_list)

def EditTask():
    def NewEditTask():
            FinalNewTask = AdjustedTask.get()
            task_list.append(FinalNewTask)
            task_list.remove(EdTask)
            Tasks.config(text=task_list)
    EdTask = ETask.get()
    if EdTask in task_list:
        EdIndex = task_list.index(EdTask)
        print(EdIndex)
        
        AdjustedTask = GUI.Entry(Manager, font='Impact 20')
        AdjustedTask.place(x=1350, y=500, width = 100, height = 150)
        CreateFinalNewTask = GUI.Button(Manager, text="Generate new task", command=NewEditTask)
        CreateFinalNewTask.place(x=1350, y=600, width = 100, height = 200)


def SaveTask():
    TaskJSON = json.dumps(task_list)
    with open("Tasks.json", "w") as outfile:
         json.dump(TaskJSON, outfile)


def LoadTask():
     with open("Tasks.json") as infile:
          TaskJSON = json.load(infile)
          task_listLoad = json.loads(TaskJSON)
          task_list.extend(task_listLoad[1:-1])
          Tasks.config(text=task_list)
          print(task_list)

# End of functions and functionality      


# Graphical Interface section

Manager = GUI.Tk()

NewButton = GUI.Button(Manager, text="Create New task", command=NewTask)
NewButton.place(x=750, y=600, width = 100, height = 200)

NTask = GUI.Entry(Manager, font='Impact 20')
NTask.place(x=750, y=500, width = 100, height = 150)

DeleteButton = GUI.Button(Manager, text="Delete task", command=DeleteTask)
DeleteButton.place(x=950, y=600, width = 100, height = 200)

DTask = GUI.Entry(Manager, font='Impact 20')
DTask.place(x=950, y=500, width = 100, height = 150)



EditButton = GUI.Button(Manager, text="Edit task", command=EditTask)
EditButton.place(x=1150, y=600, width = 100, height = 200)

ETask = GUI.Entry(Manager, font='Impact 20')
ETask.place(x=1150, y=500, width = 100, height = 150)

Tasks = GUI.Label(Manager, text=task_list, font='Impact 30')
Tasks.place(x=750, y=0)

QuitApplication = GUI.Button(Manager, text="QUIT", command = Manager.destroy)
QuitApplication.place(x=750, y=800, width = 500, height = 200)












SaveButton = GUI.Button(Manager, text="SAVE", command=SaveTask)
SaveButton.place(x=250, y=800, width = 500, height = 200)

LoadButton = GUI.Button(Manager, text="LOAD", command=LoadTask)
LoadButton.place(x=1250, y=800, width = 500, height = 200)

Manager.mainloop()