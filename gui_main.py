import tkinter as tki
import task_functions as func
root=tki.Tk()
root.title("To-Do List")
p1=tki.PhotoImage(file="mini-project\\list_icon.png")
root.iconphoto(False,p1)
# root.geometry("300x300")

# CREATING THE HEADER
lbl_header=tki.Label(root,
                    text="To-Do List....\nYour tasks are:",
                    font=("Helvetica","20"),
                    fg="blue",
                    bg="#FFFFC4"
                    )
lbl_header.pack(fill=tki.X)

#CREATING A FRAME TO SHOW TASK TABLE
frm_task_table=tki.Frame(root)
frm_task_table.pack(fill=tki.BOTH)

# ADDING TASKS TITLES TO THE CONTAINER WITH THEIR OWN FRAME INTO THE TASK TABLE
frm_task_title=tki.Frame(frm_task_table,bg="black")
frm_task_title.pack(fill=tki.X)
lbl_name=tki.Label(frm_task_title,text="Name")
lbl_description=tki.Label(frm_task_title,text="Description")
lbl_due=tki.Label(frm_task_title,text="Due")
lbl_done=tki.Label(frm_task_title,text="Done?")
lbl_name.grid(row=0,column=0,padx=3,pady=2,sticky="nsew")
lbl_description.grid(row=0,column=1,padx=3,pady=2,sticky="nsew")
lbl_due.grid(row=0,column=2,padx=3,pady=2,sticky="nsew")
lbl_done.grid(row=0,column=3,padx=3,pady=2,sticky="nsew")
frm_task_title.rowconfigure(0,weight=1)
for j in range(4):
        frm_task_title.columnconfigure(j,weight=1)

# CREATING THE TASK CONTAINER
frm_task_holder=tki.Frame(frm_task_table,bg="#DDDDDD")
frm_task_holder.pack(fill=tki.X)
# LOADING THE TASKS
tasks=func.read_tasks()
# CREATING A CONTAINER TO HOLD THE TASK WIDGETS
task_widget,checkbutton_states=func.task_2_widget(tasks, frm_task_holder)
frm_task_holder.pack(fill=tki.X)
# ADDING TASKS IN THE TASKS HOLDER
for r in range(len(task_widget)):
    task_widget[r]["name"].grid(row=r,column=0,padx=3,pady=2,sticky="nsew")
    task_widget[r]["desc"].grid(row=r,column=1,padx=3,pady=2,sticky="nsew")
    task_widget[r]["due"].grid(row=r,column=2,padx=3,pady=2,sticky="nsew")
    task_widget[r]["done"].grid(row=r,column=3,padx=3,pady=3,sticky="nsew")
    # print(r)
for c in range(4):
    frm_task_holder.columnconfigure(c,weight=1)

# ADDING THE NEW TASK BUTTON TO THE ORIGINAL FIRST FRAME
btn_new_task=tki.Button(frm_task_table,text="Add a task",command=lambda: func.switch_frames(frm_task_table,frm_new_task))
btn_new_task.pack(side=tki.BOTTOM)

# CREATING NEW FRAME TO ADD A TASK
frm_new_task=tki.Frame(root,bg="orange")
lbl_name_addframe=tki.Label(frm_new_task,text="Task name:")
lbl_name_addframe.grid(row=0,column=0)
lbl_desc_addframe=tki.Label(frm_new_task,text="Task description:")
lbl_desc_addframe.grid(row=1,column=0)
lbl_due_addframe=tki.Label(frm_new_task,text="Task due:")
lbl_due_addframe.grid(row=2,column=0)
ent_name_addframe=tki.Entry(frm_new_task)
ent_name_addframe.grid(row=0,column=1)
ent_desc_addframe=tki.Entry(frm_new_task)
ent_desc_addframe.grid(row=1,column=1)
ent_due_addframe=tki.Entry(frm_new_task)
ent_due_addframe.grid(row=2,column=1)
# ADDING BUTTON TO ADD AND SAVE THE TASK AND CANCEL
btn_add=tki.Button(frm_new_task,text="Add",command=lambda: func.add_new_task(ent_name_addframe, ent_desc_addframe, ent_due_addframe, tasks, task_widget, frm_task_holder, frm_new_task, frm_task_table, checkbutton_states))
btn_add.grid(row=3,column=1)
btn_cancel=tki.Button(frm_new_task,text="Cancel",command=lambda: func.switch_frames(frm_new_task, frm_task_table))
btn_cancel.grid(row=3,column=0)

root.protocol("WM_DELETE_WINDOW",lambda : func.save_tasks(tasks, root))
root.mainloop()