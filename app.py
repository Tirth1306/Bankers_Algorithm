import subprocess
import os
import time
from tkinter import *


app = Tk()
app.title("Banker's Algorithm")
app.geometry('1200x600')

top_frame = Frame(app)
top_frame.pack(side = LEFT)

out_frame = Frame(app)
out_frame.pack(side = RIGHT)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

Button(top_frame, text="Restart", command=restart_program).pack()

Label(top_frame, text='No of Processes').pack()
prc = Entry(top_frame)
prc.pack()

Label(top_frame, text='No of Resources').pack()
rcs = Entry(top_frame)
rcs.pack()


def GiveInput():
    # if os.path.exists("Output.osproject"):
    #     os.remove('Output.osproject')
    processes = int(prc.get())
    resources = int(rcs.get())

    Label(top_frame, text=f'Max Available Resources Space separated... {resources} Entries required').pack()
    ar = Entry(top_frame)
    ar.pack()

    AlWd = []
    for _ in range(processes):
        Label(top_frame, text=f'Allocated Resource for Process {_+1} Space separated... {resources} Entries required').pack()
        temp = Entry(top_frame)
        temp.pack()
        AlWd.append(temp)

    MaxWd = []
    for _ in range(processes):
        Label(top_frame, text=f'Max Resource for Process {_+1} Space separated... {resources} Entries required').pack()
        temp = Entry(top_frame)
        temp.pack()
        MaxWd.append(temp)

    def Compute():
        # out_frame.pack_forget()
        # with open('data.osproject','w') as file:
        #     pass
            # file.write(f"{NoOfProcesses}\n")
            # file.write(f"{NoOfResources}\n")
            # file.write(ar.get()+"\n")
            # for _ in AlWd:
            #     file.write(_.get()+"\n")
            # for _ in MaxWd:
            #     file.write(_.get()+"\n")
        processes = int(prc.get())
        resources = int(rcs.get())
        max_resources = [int(x) for x in ar.get().split(' ')]
        currently_allocated = [[int(x) for x in _.get().split(' ')] for _ in AlWd]
        max_need = [[int(x) for x in _.get().split(' ')] for _ in MaxWd]
        # max_resources = list(map(int, ar.get().split(' ')))

        # cmd = ["Algo2.exe",">>" ,"Output.osproject"]
        # returned_value = subprocess.call(cmd)
        # print('returned value:', returned_value)
        # os.system("Algo2.exe")
        # time.sleep(1)

        # os.system("./Algo2 >> Output.osproject")
        # os.system("./Algo")
        # subprocess.run(['./Algo'])
        # print(x)
        allocated = [0] * resources
        for i in range(processes):
            for j in range(resources):
                allocated[j] += currently_allocated[i][j]
        # print(f"\ntotal allocated resources : {allocated}")
        output = f"\ntotal allocated resources : {allocated}"

        available = [max_resources[i] - allocated[i] for i in range(resources)]
        # print(f"total available resources : {available}\n")
        output += f"\ntotal available resources : {available}\n"

        output += "\nMax needs of resources: \n"
        for o in max_need:
            output += str(o)
            output += '\n'
        running = [True] * processes
        count = processes
        while count != 0:
            safe = False
            for i in range(processes):
                if running[i]:
                    executing = True
                    for j in range(resources):
                        if max_need[i][j] - currently_allocated[i][j] > available[j]:
                            executing = False
                            break
                    if executing:
                        output += f"\nprocess {i + 1} is executing"
                        # print(f"process {i + 1} is executing")
                        running[i] = False
                        count -= 1
                        safe = True
                        for j in range(resources):
                            available[j] += currently_allocated[i][j]
                        break
            if not safe:
                output += "\nthe processes are in an unsafe state."
                # print("the processes are in an unsafe state.")
                break

            output += f"\nthe process is in a safe state.\navailable resources : {available}\n"
            # print(f"the process is in a safe state.\navailable resources : {available}\n")
        # time.sleep(1)
        # with open('Output.osproject','r') as f:
        #     Output = f.read()
        # print(Output)

        X = Label(out_frame, text=output)
        X.pack()


    Compute = Button(top_frame, text='Compute', command = Compute)
    Compute.pack()


GiveInput = Button(top_frame, text='GiveInput', command = GiveInput)
GiveInput.pack()

app.mainloop()
