import tkinter as tk
def read_tasks():
    '''This function returns a list of list of tasks from the saved tasks.csv file'''
    file=open("tasks.csv","rt")
    tasks=[]
    for line in file.readlines():
        # tasks.append(line.split(","))
        # t=[]
        # for x in line.split(","):
            # l=tki.Label(master=window,text=x)
            # t.append(l)
        # tasks.append(t)
        # print(line.split(","))
        l=line.split(",")
        d={"name":l[0],"desc":l[1],"due":l[2][0:-1]}
        tasks.append(d)
    file.close()
    return tasks

def save_tasks(tasks, window):
    file=open("tasks.csv","w")
    for task in tasks:
        file.write(task["name"]+","+task["desc"]+","+task["due"]+"\n")
    file.close()
    window.destroy()

def task_2_widget(tasks,window):
    task_widgets=[]
    btn_state=[]
    for i in range(len(tasks)):
        task_name=tk.Label(window,text=tasks[i]["name"],font=("Helvetica","15"))
        task_desc=tk.Label(window,text=tasks[i]["desc"],font=("Helvetica","15"))
        task_due=tk.Label(window,text=tasks[i]["due"],font=("Helvetica","15"))
        done_state=tk.IntVar()
        btn_state.append(done_state)
        task_done=tk.Checkbutton(window,variable=done_state, command=lambda: remove_task(task_widgets,tasks,btn_state))
        task_widgets.append({"name":task_name,"desc":task_desc,"due":task_due,"done":task_done})
    return (task_widgets,btn_state)

def switch_frames(frm1, frm2):
    frm1.pack_forget()
    frm2.pack(fill=tk.X)

def add_new_task(ent_name, ent_desc, ent_due, tasks, task_widgets, frm_task_holder, frm1, frm2, btn_state):
    count=len(tasks)
    name, desc, due = ent_name.get(), ent_desc.get(), ent_due.get()
    tasks.append({"name":name,"desc":desc,"due":due})
    task_name=tk.Label(frm_task_holder,text=name,font=("Helvetica","15"))
    task_desc=tk.Label(frm_task_holder,text=desc,font=("Helvetica","15"))
    task_due=tk.Label(frm_task_holder,text=due,font=("Helvetica","15"))
    done_state=tk.IntVar()
    btn_state.append(done_state)
    task_done=tk.Checkbutton(frm_task_holder, variable=done_state, command=lambda: remove_task(task_widgets,tasks,btn_state))
    task_widgets.append({"name":task_name,"desc":task_desc,"due":task_due,"done":task_done})
    task_name.grid(row=count,column=0,padx=3,pady=2,sticky="nsew")
    task_desc.grid(row=count,column=1,padx=3,pady=2,sticky="nsew")
    task_due.grid(row=count,column=2,padx=3,pady=2,sticky="nsew")
    task_done.grid(row=count,column=3,padx=3,pady=2,sticky="nsew")
    switch_frames(frm1, frm2)

def remove_task(task_widgets, tasks, btn_state):
    for i in range(len(btn_state)):
        if (btn_state[i].get()==1):
            # print(i)
            break
    else:
        return
    task_widgets[i]["name"].grid_forget()
    task_widgets[i]["desc"].grid_forget()
    task_widgets[i]["due"].grid_forget()
    task_widgets[i]["done"].grid_forget()
    task_widgets[i]["name"].destroy()
    task_widgets[i]["desc"].destroy()
    task_widgets[i]["due"].destroy()
    task_widgets[i]["done"].destroy()
    tasks.pop(i)
    btn_state.pop(i)
    task_widgets.pop(i)
    while i < len(task_widgets):
        task_widgets[i]["name"].grid(row=i,column=0,padx=3,pady=2,sticky="nsew")
        task_widgets[i]["desc"].grid(row=i,column=1,padx=3,pady=2,sticky="nsew")
        task_widgets[i]["due"].grid(row=i,column=2,padx=3,pady=2,sticky="nsew")
        task_widgets[i]["done"].grid(row=i,column=3,padx=3,pady=2,sticky="nsew")
        i+=1

# print(read_tasks())

def time_thread(window):
    print("1s done")
    window.after(1000, time_thread(window))