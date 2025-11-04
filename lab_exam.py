import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from tkinter import messagebox, BooleanVar
from tkinter import ttk
import random

mint_green = "#4BB17B"  
#Create the window
root = tk.Tk()
root.state("zoomed")
root.config(bg="white")
# --
mainContentFrame = tk.Frame(root,bg="white")
rightSideFrame=tk.Frame(mainContentFrame,bg="white",width=600,relief='raised',bd=2,)

fig, ax = plt.subplots(figsize=(9, 8),facecolor="#F3F3F3")  # width=9 inches, height=8 inches
canvas=FigureCanvasTkAgg(fig, master=rightSideFrame)
canvas.get_tk_widget().place(rely=0.5,relx=0.5,anchor="center")

toolbar = NavigationToolbar2Tk(canvas, rightSideFrame)
toolbar.update()
toolbar.pack_forget()  # hide immediately
currentVal = {}
showToggle = tk.BooleanVar(value=False)

def createLinePlot(xValues,yValues,formatVals,first,toggle,labels):
    global ax, currentVal,showToggle,toolBar
    fig.clear()  # clear the entire figure
    ax = fig.add_subplot(111)  # create a new axes each time
    finalValues={}
    ax.set_aspect('auto')

    if(first): #If first time or cleared
        toolbar.pack_forget()
        showToggle.set(False)
        ax.plot([0],[0])
        ax.set_title("Line Graph")
        ax.set_ylabel("Y Label")
        ax.set_xlabel("X Label")
        ax.text(0.5, 0.5, 'Input data to generate the plot.',ha='center', va='center', transform=ax.transAxes, fontsize=12, alpha=0.6)

    else:
        showToggle.set(True)
        finalValues = {
            "x" : xValues,
            "y" : yValues,
            "marker" : formatVals[0],
            "markerSize" :  formatVals[1],
            "markerFaceColor": formatVals[2],
            "markerEdgeColor": formatVals[3],
            "lineStyle": formatVals[4],
            "color": formatVals [5],
            "lineWidth": formatVals[6],
            "title":labels[0],
            "xlabel":labels[1],
            "ylabel":labels[2],
        }
        if toggle:
            print("Toggle is Used")
            finalValues = currentVal.copy()
        else:
            print("Did not use Toggle")
            currentVal = finalValues.copy()

        ax.plot(finalValues["x"],finalValues["y"],marker=finalValues["marker"],markersize=finalValues["markerSize"],markerfacecolor=finalValues["markerFaceColor"],markeredgecolor=finalValues["markerEdgeColor"],linestyle=finalValues["lineStyle"],color=finalValues["color"],linewidth=finalValues["lineWidth"])
        ax.set_title(finalValues["title"], fontsize=14, fontweight="bold", color="black")
        ax.set_xlabel(finalValues["xlabel"],labelpad=20, fontdict={"fontsize": 12})
        ax.set_ylabel(finalValues["ylabel"],labelpad=20, fontdict={"fontsize": 12})
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    
        #Toggle Options
        ax.grid(checkGrid.get())
        if checkyTick.get():
            ax.set_yticks(finalValues["y"])  # show only the actual bar heights
        ax.autoscale()  # recompute the axis limits and ticks automatically
    canvas.draw()

def createBarPlot(xValues,yValues,colorBar,edgeColor,hatchBar,widthBar,first,toggle,labels):
    global ax,currentVal,showToggle,toolBar
    fig.clear()
    ax = fig.add_subplot(111)
    finalValues = {}
    ax.set_aspect('auto')

    if (first):  # If first time or cleared
        showToggle.set(False)
        toolbar.pack_forget()
        ax.bar([0], [0], width=0.5)
        ax.set_title("Bar Graph")
        ax.set_ylabel("Y Label")
        ax.set_xlabel("X Label")
        ax.text(0.5, 0.5, 'Input data to generate the plot.',ha='center', va='center', transform=ax.transAxes, fontsize=12, alpha=0.6)
        
    else:
        showToggle.set(True)
        finalValues = {
            "x" : xValues,
            "y" : yValues,
            "widthBar" : widthBar,
            "colorBar" :  colorBar,
            "edgeColor": edgeColor,
            "hatchBar": hatchBar,
            "title":labels[0],
            "xlabel":labels[1],
            "ylabel":labels[2],
        }
        if toggle:
            print("Toggle is Used")
            finalValues = currentVal.copy()
        else:
            print("Did not use Toggle")
            currentVal = finalValues.copy()

        if not checkHori.get():
            bars=ax.bar(finalValues["x"], finalValues["y"], width=finalValues["widthBar"],color=finalValues["colorBar"],edgecolor=finalValues["edgeColor"],hatch=finalValues["hatchBar"])
        else:
            bars = ax.barh(finalValues["x"], finalValues["y"], height=finalValues["widthBar"],color=finalValues["colorBar"], edgecolor=finalValues["edgeColor"], hatch=finalValues["hatchBar"])
       
        ax.set_title(finalValues["title"], fontsize=14, fontweight="bold", color="black")
        ax.set_xlabel(finalValues["xlabel"],labelpad=20, fontdict={"fontsize": 12})
        ax.set_ylabel(finalValues["ylabel"],labelpad=20, fontdict={"fontsize": 12})
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
         #Toggles
        ax.grid(checkGrid.get())
        if checkTextOnTop.get(): #Toggle Text
            if not checkHori.get():
                for i, bar in enumerate(bars):
                    barHeight = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width() /2,barHeight, str(finalValues["y"][i]),ha="center",va="bottom")
            else:
                for i, bar in enumerate(bars):
                    barWidth = bar.get_width()
                    ax.text(barWidth,bar.get_y() + bar.get_height() / 2, str(finalValues["y"][i]),ha="left",va="center")

        if checkyTick.get(): ax.set_yticks(finalValues["y"])  # show only the actual bar heights
        
        if checkLegend .get(): #Toggle Legend
            ax.legend(bars,finalValues["y"],title="Categories")
        ax.autoscale()  # recompute the axis limits and ticks automatically
    canvas.draw()

def createPiePlot(xValues,yValues,pieColor,pieHatch,explode,percentage,first,toggle,labels):
    global ax,currentVal,toolBar
    fig.clear()
    ax = fig.add_subplot(111)
    ax.set_title("Pie Graph",pad=40)
    finalValues = {}
    if (first):  # If first time or cleared
        # ax.plot(xTest,yTest)
        showToggle.set(False)
        ax.pie([1], labels=[''],colors=['lightgrey'], )
        toolbar.pack_forget()
        ax.text(0.5, 0.5, 'Input data to generate the plot.',ha='center', va='center', transform=ax.transAxes, fontsize=12, alpha=0.6)

    else:
        showToggle.set(True)
        finalValues = {
            "x": xValues,
            "y": yValues,
            "colors": pieColor,
            "hatch": pieHatch,
            "explode": explode,
            "title": labels[0],
        }
        if toggle:
            print("Toggle is Used")
            finalValues = currentVal.copy()
        else:
            print("Did not use Toggle")
            currentVal = finalValues.copy()

        #Setting Labels
        ax.set_title(finalValues["title"], fontsize=14, fontweight="bold", color="black")

        if not checkPercent.get():
            ax.pie(finalValues["y"], labels=finalValues["x"],colors=finalValues["colors"],hatch=finalValues["hatch"],explode=finalValues["explode"],shadow = checkShadow.get())
        else:
            wedges, texts, autotexts =ax.pie(finalValues["y"], labels=finalValues["x"], colors=finalValues["colors"], hatch=finalValues["hatch"],explode=finalValues["explode"], shadow=checkShadow.get(),autopct="%1.1f%%")
            if checkPctWhite.get():
                print("Pumasok sa change color pct")
                for percentText in autotexts:
                    percentText.set_color ("white")
                    percentText.set_fontweight("bold")

        toolbar.pack(side=tk.BOTTOM, fill=tk.X)

        if checkLegend.get():ax.legend(title="Categories")
    canvas.draw()

createLinePlot([],[],[],True,False,[]) #initially load the line graph

#FUNCTIONS --
formatValues = []
colorValues=[]
entryValues=[]
finalValues=[] #The final values
plotTypes=["Line Graph","Bar Graph","Pie Graph"]
colorOption=["red", "blue", "yellow", "green", "purple", "orange", "pink", "brown","cyan", "magenta", "lime", "teal", "violet", "indigo", "maroon", "navy", "olive", "gold", "silver", "turquoise", "beige", 
             "lavender", "tan", "skyblue", "khaki", "orchid", "tomato", "crimson", "darkgreen", "darkblue", "darkred", "darkorange", "lightblue", "lightgreen", "lightpink"]

def confirmPop(text):
    conf = tk.messagebox.askyesno("Confirm",text)
    return conf

def mesBox(text):
    tk.messagebox.showinfo("Input Error",text)

def onCustomSelect(event,type,graph,whatWidget):#if the user chose the custom instead of random
    if (event.widget.get()=="Custom"):
        if(graph =="barColor"):
            openColorPopUp(type,whatWidget)
        elif(graph =="hatch"):
            openHatchPopUp(type,whatWidget)

#Color for Bar
hatchPatternVal=[] #hatch Pattern for Bar
colorBar=[] #Color for Bar
edgeColor=[] #Edge Color for Bar
pieColor=[] #Color for Pie
pieHatch=[] #Pie Hatch
explodeVal=[] #Pie Explode Values
lastColBar=["red","red","red","red","red"] # Default Vals
lastColEdge=["red","red","red","red","red"]
lastColPie=["red","red","red","red","red"]

def openColorPopUp(type,comboBox):
    print(f"ComBox is {comboBox}")
    popup=tk.Toplevel(root)
    popup.title("Custom")
    popup.geometry("300x300")
    popup.grab_set() #Disable user to click outside the tab
    print("The type is "+type)
    colorValuesTemp=[]
    global colorValues,lastColBar,lastColEdge,lastColPie
    colorValues =[]
    popHead=tk.Frame(popup,bg=mint_green,height=30)
    popHead.pack_propagate(False)
    popHead.pack(fill="x")
    tk.Label(popHead,text="Set Colors",bg=mint_green,fg="white",font=("Arial",12,"bold")).place(relx=0.5,rely=0.5,anchor="center")
    
    #Center Frame
    centerFPop=tk.Frame(popup)
    centerFPop.pack_propagate(False)
    centerFPop.pack(pady=10,padx=15,fill="both",expand=True)
    
    # Inner container (to center the grid content)
    innerFrame = tk.Frame(centerFPop)
    innerFrame.place(relx=0.5, rely=0.5, anchor="center")
    prevCol=[]

    if(type == "Bar Colors"):
         print("pumunta here sa Color Bar")
         prevCol = lastColBar
    elif(type == "Edge Color"):
        print("pumunta here sa edge Bar")
        prevCol = lastColEdge
    elif (type == "Colors"):
        prevCol=lastColPie

    # Creating the entries for x and y
    for j in range(5):
        # Label
        itemLabelPop = tk.Label(innerFrame, text=f"Value #{j + 1}:", font=('Arial', 10))
        itemLabelPop.grid(row=j, column=0, sticky="e", padx=5, pady=10)

        indexOfLastColor = colorOption.index(prevCol[j]) #Getting the index of the last selected Color
        dropDownPop = ttk.Combobox(innerFrame, values=colorOption, state="readonly", width=10) #Drop Down 
        dropDownPop.current(indexOfLastColor)
        dropDownPop.grid(row=j, column=1, sticky="ew", padx=5, pady=10)
        
        colorLabel=tk.Label(innerFrame,bg=dropDownPop.get(),width=2,relief="solid") # Color Labels
        colorLabel.grid(row=j, column=2, sticky="e", padx=5, pady=10)
        dropDownPop.bind("<<ComboboxSelected>>", lambda event, lbl=colorLabel: lbl.config(bg=event.widget.get()))

        colorValuesTemp.append(dropDownPop)

    def saveColors():
        global colorBar,edgeColor,pieColor,lastColBar,lastColEdge,lastColPie
        if confirmPop("Change Colors?"):
            for i in colorValuesTemp:
                colorValues.append(i.get())
            if(type == "Bar Colors"):
                print("pumunta here sa Color Bar")
                colorBar = colorValues
                lastColBar=colorBar
            elif(type == "Edge Color"):
                print("pumunta here sa edge Bar")
                edgeColor = colorValues
                lastColEdge=edgeColor
            elif (type == "Colors"):
                pieColor=colorValues
                lastColPie=pieColor

            popup.destroy()

    def closePop():
        if confirmPop("Close Custom Tab?"):
            popup.destroy()

    butFrame = tk.Frame(popup)
    butFrame.pack(side="bottom", pady=10)  # Bottom center
    tk.Button(butFrame, command=saveColors, text="Save", bg="#2E8B57", fg="white", font=("Arial", 10, "bold"), width=10 ).pack(side="left",padx=1)
    tk.Button(butFrame, command=closePop, text="Close", bg="#CD5C5C", fg="white", font=("Arial", 10, "bold"), width=10 ).pack(side="left",padx=1)
    popup.protocol("WM_DELETE_WINDOW", closePop)

prevBarHatch=["/","/","/","/","/",] #Defaults Values for hatch and explode
prevPieHatch=["/","/","/","/","/",]
prevExplode=["0.0","0.0","0.0","0.0","0.0",]

def openHatchPopUp(type,widget):
    global hatchPatternVal,hatchPat, explodeVal,prevBarHatch,prevPieHatch,prevExplode
    popup=tk.Toplevel(root)
    popup.title("Custom")
    popup.geometry("300x300")
    popup.grab_set()
    tempHatch=[]
    hatchPatternVal=[]
    hatchPat=[]

    whatText = tk.StringVar()
    if (type == "Explode"):
     whatText.set("Explode")
    else:
        whatText.set("Hatch Patterns")

    popHead=tk.Frame(popup,bg=mint_green,height=30)
    popHead.pack_propagate(False)
    popHead.pack(fill="x")
    tk.Label(popHead,text=f"Set {whatText.get()}",bg=mint_green,fg="white",font=("Arial",12,"bold")).place(relx=0.5,rely=0.5,anchor="center")

    #Center Frame
    centerFPop=tk.Frame(popup)
    centerFPop.pack_propagate(False)
    centerFPop.pack(pady=15,padx=15,fill="both",expand=True)

    # Inner container (to center the grid content)
    innerFrame = tk.Frame(centerFPop)
    innerFrame.place(relx=0.5, rely=0.5, anchor="center")
    prevChoice=[]
    optionUse=[]
    if(type=="Hatch Pattern"): #For bar hatch
        optionUse=hatchPattern
        prevChoice =  prevBarHatch
    elif (type == "Pie Hatch Pattern"):
        optionUse=hatchPattern
        prevChoice = prevPieHatch
    else:
        optionUse=explodeOption
        prevChoice = prevExplode

    # Creating the entries for x and y
    for j in range(5):
        # Label
        itemLabelPop = tk.Label(innerFrame, text=f"Value #{j + 1}:", font=('Arial', 10))
        itemLabelPop.grid(row=j, column=0, sticky="e", padx=5, pady=10)
        # Entry
        indexOfItem = optionUse.index(prevChoice[j])
        dropDownPop = ttk.Combobox(innerFrame, values=optionUse, state="readonly", width=10)
        dropDownPop.current(indexOfItem)
        dropDownPop.grid(row=j, column=1, sticky="ew", padx=5, pady=10)
        tempHatch.append(dropDownPop)

    def saveHatch():
        global hatchPatternVal, pieHatch,explodeVal,prevBarHatch,prevPieHatch,prevExplode
        if confirmPop("Confirm?"):
            for i in tempHatch:
                hatchPat.append(i.get())
            if (type == "Hatch Pattern"): #For Bar 
                hatchPatternVal=hatchPat
                prevBarHatch = hatchPatternVal
            elif(type=="Pie Hatch Pattern"): # For Pie
                pieHatch = hatchPat
                prevPieHatch=pieHatch
            elif(type=="Explode"): # For Pie Explode
                explodeVal = hatchPat
                prevExplode=explodeVal
            popup.destroy()

    def closeHatch():
        if confirmPop("Close Custom Tab?"):
            popup.destroy()
    
    butFrame = tk.Frame(popup)
    butFrame.pack(side="bottom", pady=10)  # Bottom center

    tk.Button(butFrame, command=saveHatch, text="Save", bg="#2E8B57", fg="white", font=("Arial", 10, "bold"), width=10 ).pack(side="left",padx=1)
    tk.Button(butFrame, command=closeHatch, text="Close", bg="#CD5C5C", fg="white", font=("Arial", 10, "bold"), width=10 ).pack(side="left",padx=1)
    popup.protocol("WM_DELETE_WINDOW", closeHatch)

#Format Container Content
explodeOption=["0.0","0.1","0.3"]
lineStyle=["Solid '-'","Dashed '--'","Dash-dot '-.'","Dotted ':'","None"]
markerShape=['o','p','^','v','x','+','*','.']
t=["Bar Color","Edge Color"]
linePlot=["Marker Shape","Marker Size","Marker Color","Marker Edge Color","Line Style","Line Color","Line Width"]
barPlot=["Bar Width","Bar Colors","Edge Color","Hatch Pattern"]
piePlot=["Explode","Colors","Pie Hatch Pattern"]
hatchPattern =["None","/","\\",'|',"-","+","x","o","O",".","*","//","\\\\","||","--","++","xx","oo","OO","..","**","/o","|/","|*","'-\'","+o","x*","o-","O|","O.","*_"]

def changeContent(): #Changing the content of the format label frame
    global dropDownC
    padyAll=10
    fontS =11
    # Clear previous widgets inside LabelFrame
    print(f"Drop down is: {dropDown.get()}")
    for widget in graphFormatLabelFrame.winfo_children():
        widget.destroy()
        
    if dropDown.get() == "Line Graph":
        createLinePlot([],[],[],True,False,[])
        count = 0  # row counter
        for j, values in enumerate(linePlot):
            col = j % 2  # 2 columns
            # Label
            formatLabel = tk.Label(graphFormatLabelFrame, text=f"{values}:", bg="white", font=('Arial', fontS))
            formatLabel.grid(row=count, column=col * 2, sticky="w", padx=10, pady=padyAll)
            # Entry
            if (j == 0 or j == 2 or j == 3 or j == 4 or j == 5):
                ops=[]
                if(j==0): ops = markerShape
                elif j==2 or j==3 or j==5: ops = colorOption
                elif j==4: ops = lineStyle
                formatEntry = ttk.Combobox(graphFormatLabelFrame, state="readonly", values=ops,width=10)
                formatEntry.current(0)
                formatEntry.grid(row=count, column=col * 2 + 1, sticky="ew", padx=3, pady=padyAll)
            else:
                if(j==1):
                    formatEntry = ttk.Spinbox(graphFormatLabelFrame, from_=2,to=20,increment=1,width=10,state="readonly")
                    formatEntry.set(6)
                    formatEntry.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)
                else:
                    formatEntry = ttk.Spinbox(graphFormatLabelFrame, from_=0.5, to=5, increment=0.5, width=10,state="readonly")
                    formatEntry.set(1)
                    formatEntry.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)
            # Increment row after every 2 entries
            if col == 1:
                count += 1
        # Make all columns expandable
        for c in range(4):  # 2 columns * 2 (label+entry)
            graphFormatLabelFrame.grid_columnconfigure(c, weight=1)
    elif(dropDown.get()=="Bar Graph"):
        createBarPlot([],[],[],[],[],0,True,False,[]) # Reset the graph
        count = 0  # row counter
        for j, values in enumerate(barPlot):
            col = j % 2  # 2 columns
            # Label
            formatLabel = tk.Label(graphFormatLabelFrame, text=f"{values}:", bg="white", font=('Arial', fontS))
            formatLabel.grid(row=count, column=col * 2, sticky="w", padx=5, pady=padyAll)
            # Entry
            if(j==1 or j==2): # Color
                dropDownC = ttk.Combobox(graphFormatLabelFrame, values=["Default Colors","Random","Custom"], state="readonly", width=10)
                dropDownC.current(0)
                dropDownC.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)
                dropDownC.bind("<<ComboboxSelected>>", lambda event, v=values, c=dropDownC: onCustomSelect(event, v,"barColor",c))
            elif(j==0):
                spinBox = ttk.Spinbox(graphFormatLabelFrame, from_=0.1,to=1.0, increment=0.1,state="readonly", width=10)
                spinBox.set(0.5)
                spinBox.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)
            elif (j==3): #Hatch
                dropDownH = ttk.Combobox(graphFormatLabelFrame, values=["None","Random","Custom"], state="readonly", width=10)
                dropDownH.current(0)
                dropDownH.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)
                dropDownH.bind("<<ComboboxSelected>>", lambda event, v=values, c=dropDownH: onCustomSelect(event, v, "hatch",c))
            else:
                formatEntry = tk.Entry(graphFormatLabelFrame, bg="white", highlightthickness=1, width=10)
                formatEntry.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)

                formatValues.append(formatEntry)
                # Increment row after every 2 entries
            if col == 1:
                count += 1
        # Make all columns expandable
        for c in range(4):  # 2 columns * 2 (label+entry)
            graphFormatLabelFrame.grid_columnconfigure(c, weight=1)
    elif(dropDown.get()=="Pie Graph"):
        createPiePlot([],[],[],[],[],[],True,False,[])
        count = 0  # row counter
        for j, values in enumerate(piePlot):
            col = j % 2  # 2 columns
            # Label
            formatLabel = tk.Label(graphFormatLabelFrame, text=f"{values}:", bg="white", font=('Arial', fontS))
            formatLabel.grid(row=count, column=col * 2, sticky="w", padx=5, pady=padyAll)
            if(j==0): #Explode
                dropDownPieEx = ttk.Combobox(graphFormatLabelFrame, values=["None","Random","Custom"], state="readonly", width=10)
                dropDownPieEx.current(0)
                dropDownPieEx.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)
                dropDownPieEx.bind("<<ComboboxSelected>>",lambda event, v=values, c=dropDownPieEx: onCustomSelect(event, v, "hatch",c))
            elif(j==1): #Color of pie
                dropDownPieColor = ttk.Combobox(graphFormatLabelFrame, values=["Default Colors","Random","Custom"], state="readonly", width=10)
                dropDownPieColor.current(0)
                dropDownPieColor.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)
                dropDownPieColor.bind("<<ComboboxSelected>>", lambda event, v=values, c=dropDownPieColor: onCustomSelect(event, v, "barColor",c))
            elif(j==2): #Hatch
                dropDownPieHatch = ttk.Combobox(graphFormatLabelFrame, values=["None","Random","Custom"], state="readonly", width=10)
                dropDownPieHatch.current(0)
                dropDownPieHatch.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=padyAll)
                dropDownPieHatch.bind("<<ComboboxSelected>>",lambda event, v=values,c=dropDownPieHatch: onCustomSelect(event, v, "hatch",c))
            if col == 1:
             count += 1
        # Make all columns expandable
        for c in range(4):  
            graphFormatLabelFrame.grid_columnconfigure(c, weight=1)

def getRandom(option,what):
    if(what=="explode"): return random.choices(option, k=5)   
    else: return random.sample(option,5)
 
def saveFormat(feature):
    global formatValues, finalValues,colorOption,hatchPattern,colorBar,edgeColor,hatchPatternVal,pieColor,pieHatch,explodeVal,explodeOption,chartLabels,lastColBar,lastColEdge,lastColPie,prevPieHatch,prevBarHatch,prevExplode
    formatValues=[]
    finalValues=[]
    finalChartLabelVal=[]
    print(f"Lenght of Entry Values is :{len(entryValues)}")
    finVal=0
    for val in chartLabels: # Check if chart label entries are empty
        if val.get().strip()=="":
            mesBox("Chart Labels are Empty. Please complete Chart Labels Entries")
            return
        else:
            finalChartLabelVal.append(val.get())
        
    graphType=labelText.get()
    checkDup = [v.get() for v in entryValues[:5]]   #Check if X values has duplicate
    if len(checkDup) != len(set(checkDup)):
        # There is a duplicate
        mesBox("Error, Please Input Unique X Values")
        return
    
    for index, value in enumerate(entryValues): # Getting the data of values in entries
        val_text = value.get().strip()
        if (val_text == ""): 
             mesBox("Some fields are empty. Please complete all entries.") #Check if chart label entries are empty 
             return
        try:
            if(index >= 5):
                finVal=float(val_text)
                if (graphType == "Pie Graph" and finVal <0): #in Pie Graph Only
                    mesBox("Error, Please Input Positive Numbers Only")
                    return
            else:
                finVal=val_text

            finalValues.append(finVal)
        except ValueError:
            mesBox("Please enter numeric values in the Values box") #If the Value is not an integer
            print(f"The error is {value.get()}")
            return
        
    #Final Confirmation
    if(not feature):
     if(not confirmPop("Are you Sure?")):return
     mesBox("Successful")

    print(f"The Final Values of X and Y is: {finalValues}")
    graphType=labelText.get()
    percent=False
    for index ,widget in enumerate(graphFormatLabelFrame.winfo_children()):
        print("The index is :",index)
        if (isinstance(widget,(tk.Entry, ttk.Combobox, tk.Spinbox))):
            print(f"THE GRAPH IS: {graphType}")
            value = widget.get()
            if (graphType == "Line Graph"):
                if value in lineStyle and "'" in value:
                    value = value.split("'")[1]  # split by the single quote and get the part in the middle For line graph
            elif (graphType == "Bar Graph"):
                if(index == 3  or index == 5):#For Color
                    if(value =="Random"):
                            if(index == 3):
                                value = "color bar custom"
                                colorBar=getRandom(colorOption,"c")
                            else:
                                value = "edge color Custom"
                                edgeColor=getRandom(colorOption,"c")

                    elif value =="Default Colors":
                        if (index == 3):
                            value = "color Bar None "
                            colorBar = None
                        else:
                            value = "edge Color None "
                            edgeColor = None
                    else:
                        value = "color custom"
                elif (index == 7): #For Hatch
                    if(value =="Random"):
                        value="hatch Random"
                        hatchPatternVal = getRandom(hatchPattern,"c")
                    elif value =="None":
                        hatchPatternVal=None
                        value= "hatch None"
                    else:
                        value="Hatch custom"
            elif (graphType == "Pie Graph"): #Pie graph
                if(index == 3 ):#For Pie Color
                    if(value =="Random"):
                        value = "Color Pie Random"
                        pieColor=getRandom(colorOption,"c")
                    elif value == "Default Colors":
                        value ="pie None color"
                        pieColor =None
                    else:
                        value = "pie custom color"
                elif (index == 5): #For Hatch
                    if(value =="Random"):
                        value="hatch Pie Random"
                        pieHatch = getRandom(hatchPattern,"c")
                    elif value == "None":
                        value = "hatch None Custom"
                        pieHatch = None
                    else:
                        value= "hatch pie Custom"
                elif(index == 1):
                    if(value =="Random"):
                        value="explode Pie Random"
                        explodeVal = getRandom(explodeOption,"explode")
                    elif value =="None":
                        value = "explode pie None"
                        explodeVal =None
                    else:
                        value= "explode pie Custom"
                elif index == 7:
                    if(value == "Actual Number"):
                        percent = False
                    else:
                        percent = True

            formatValues.append(value)

    if not hatchPatternVal == None:
        hatchPatternVal= [None if h=="None" else h for h in hatchPatternVal]

    if not pieHatch == None:
        pieHatch = [None if h=="None" else h for h in pieHatch]
    
    # Default values
    defaults = {
        "colorBar": ["blue"] * 5,
        "edgeColor": ["red"] * 5,
        "pieColor": ["red"] * 5,
        "hatchPatternVal": ["/"] * 5,
        "pieHatch": ["/"] * 5,
        "explodeVal": ["0.0"] * 5,
    }

   # Apply defaults only if empty
    colorBar = defaults["colorBar"] if colorBar == [] else colorBar
    edgeColor = defaults["edgeColor"] if edgeColor == [] else edgeColor
    pieColor = defaults["pieColor"] if pieColor == [] else pieColor
    hatchPatternVal = defaults["hatchPatternVal"] if hatchPatternVal == [] else hatchPatternVal
    pieHatch = defaults["pieHatch"] if pieHatch == [] else pieHatch
    explodeVal = defaults["explodeVal"] if explodeVal == [] else explodeVal

    print(f"The Format Values are: {formatValues}\n\n")
    print(f"Chart Labels are: {finalChartLabelVal}\n")
    print("----------------BAR PLOT FORMAT------------------ ")
    print(f"The Hatch are: {hatchPatternVal}")
    print(f"The Bar Color are: {colorBar}")
    print(f"The Edge Color are: {edgeColor}")
    print("-----------------------------------\n\n")
    print("----------------PIE PLOT FORMAT------------------ ")
    print(f"The Pie Hatch are: {pieHatch}")
    print(f"The Pie Color are: {pieColor}")
    print(f"The Explode Pie are: {explodeVal}")
    print("---------------------------------------\n\n")
    finalXy = np.array(finalValues)
    x= np.array(finalXy[:5])
    y = np.array([float(n) for n in finalXy[5:]])
    print("X Value is :",x)
    print("Y Value is :", y)

    #The last Save Items
    lastColBar= colorBar if not colorBar == None else defaults["colorBar"]
    lastColEdge= edgeColor if not edgeColor == None else defaults["edgeColor"]
    lastColPie= pieColor if not pieColor == None else defaults["pieColor"]
    prevBarHatch= hatchPatternVal if not hatchPatternVal == None else defaults["hatchPatternVal"]
    prevPieHatch= pieHatch if not pieHatch == None else defaults["pieHatch"]
    prevExplode= explodeVal if not explodeVal == None else defaults["explodeVal"]

    if graphType == "Line Graph": plotGraph("line",finalChartLabelVal,x,y,formatValues,[],[],[],[],[],[],False,feature)
    elif graphType == "Bar Graph":plotGraph("bar",finalChartLabelVal,x,y,formatValues[0],colorBar,edgeColor,hatchPatternVal,[],[],[],False,feature)
    elif graphType == "Pie Graph": plotGraph("pie",finalChartLabelVal ,x, y, [], colorBar, edgeColor, pieHatch,pieColor,pieHatch,explodeVal,percent,feature)

def plotGraph(graph,labels,finX,finY,linePlot, #For line Plot
              colorBar,edgeColor,hatchBar, #For Bar Plot:
              pieColor,pieHatch,explode,percent, #For Pie Plot
              toggle): #Toggle
    if graph == "line": # Line Plot
        print("Here line")
        #Convert string vals to int
        lineFormat =[]
        for index, value in enumerate(linePlot):
            if(index == 1 or index == 6):
                value = float(value)

            lineFormat.append(value)
        createLinePlot(finX,finY,lineFormat,False,toggle,labels)

    elif graph == "bar":
        print("Here bar")
        createBarPlot(finX, finY, colorBar, edgeColor,hatchBar,float(linePlot),False,toggle,labels)

    elif graph == "pie":
        newEx = explode
        if not explode == None:
            newEx=[]
            for i in explode:
                newEx.append(float(i))

        print("Here bar")
        createPiePlot(finX, finY, pieColor, pieHatch,newEx,percent,False,toggle,labels)

    toggleEffect(True)

def toggleFeature(feature): saveFormat(True)

#Header for main
headerMain = tk.Frame(root, bg=mint_green, height=90)
headerMain.pack_propagate(False)
headerMain.pack(fill="x")

headerText = tk.Label(headerMain, text="Midterm Lab Exam", bg=mint_green, font=("Arial", 22, "bold"), fg="white" )
headerText.place(relx=0.5, rely=0.5, anchor="center")
# Main content
mainContentFrame.config(bg="#F3F3F3")
mainContentFrame.pack_propagate(False)
mainContentFrame.pack(padx=20, pady=20, expand=True, fill="both")

# Left Side
leftSideFrame = tk.Frame(mainContentFrame, bg="white", relief="raised", bd=2)
leftSideFrame.pack_propagate(False)
leftSideFrame.pack(expand=True, fill="both", side="left", padx=(0, 12))

leftSideHeadFrame = tk.Frame(leftSideFrame, bg="#3E9063", height=40)
leftSideHeadFrame.pack(fill="x")

leftSideHeadLabel = tk.Label(leftSideHeadFrame, text="Input Panel", fg="white", bg="#3E9063", font=("Arial", 14, "bold") )
leftSideHeadLabel.place(relx=0.5,rely=0.5,anchor="center")
type =["Label","Value"]

labelText = tk.StringVar()
labelText.set("Line Graph")

#Drop down widget
dropDown = ttk.Combobox(leftSideFrame,values=plotTypes,state="readonly",textvariable=labelText)
dropDown.current(0)
dropDown.pack(pady=(15, 8), padx=(10, 5))
chartLabels=[]
titleLab=["Title","X Label","Y Label"]

def createChartLabel():
    global chartLabels
    for i in range(1):
        fontS=11
        titleFrame = tk.LabelFrame(leftSideFrame,height=100,bg="white",text="Chart Labels")
        titleFrame.pack_propagate(False)
        titleFrame.pack(fill="both",padx=20,pady=5)
        count = 0  # row counter
        for j in range(3):
            col = j % 2  # 2 columns
            # Label
            itemLabel = tk.Label(titleFrame, text=f"{titleLab[j]}:", bg="white", font=('Arial', fontS))
            itemLabel.grid(row=count, column=col * 2, sticky="w", padx=5, pady=5)
            # Entry
            chartEntry = tk.Entry(titleFrame, bg="white", highlightthickness=1)
            chartEntry.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=5)
            chartLabels.append(chartEntry) #Get the CHART LABEL ENTRY
            # Increment row after every 2 entries
            if col == 1:
                count += 1
        # Make all columns expandable
        for c in range(3): 
            titleFrame.grid_columnconfigure(c, weight=1)

createChartLabel()

def resetButton():
    resetAllValues(True)

def resetAllValues(ask):
    global hatchPatternVal,pieHatch,pieColor,edgeColor,colorBar,formatValues,explodeVal,entryValues,toggles,currentVa,chartLabels,lastColBar,lastColEdge,lastColPie
    if ask:
        conf=confirmPop("Reset the Entries and Figure?")
        if(not conf):
            return
        else:
            for i in entryValues:
                i.delete(0, tk.END)
            for i in chartLabels:
                i.delete(0, tk.END)

    hatchPatternVal = []
    pieHatch = []
    pieColor = []
    edgeColor = []
    colorBar = []
    formatValues = []
    explodeVal = []
    lastColBar=["blue","blue","blue","blue","blue"]
    lastColEdge=["red","red","red","red","red"]
    lastColPie=["red","red","red","red","red"]
    currentVal={}

    for index ,widget in enumerate(graphFormatLabelFrame.winfo_children()):
        print("The index is :",index)
        if (isinstance(widget,( ttk.Combobox,))):
            widget.current(0)

    for i in toggles:
        i.set(False)

    showToggle.set(False)
    toggleEffect(False)
    
    graphType = labelText.get()
    if(graphType == "Line Graph"): createLinePlot([],[],[],True,False,[])
    elif(graphType=="Bar Graph"): createBarPlot([], [], [], [],[],0,True,False,[])
    elif graphType=="Pie Graph": createPiePlot([], [], [], [], [], [], True,False,[])
        
def update_labelframe(event):
    resetAllValues(False)
    graphFormatLabelFrame.config(text=labelText.get())
    changeContent()
    toggleEffect(False)

dropDown.bind("<<ComboboxSelected>>", update_labelframe)
#Creating the entries for x and y
whatVal=["X","Y"]
for i in range(2):
    fontS=11
    leftLabelFrame = tk.LabelFrame(leftSideFrame,height=100,bg="white",text=f"Input {type[i]} ({whatVal[i]} Value)")
    leftLabelFrame.pack_propagate(False)
    leftLabelFrame.pack(fill="both",padx=20,pady=10)
    count = 0  # row counter

    for j in range(5):
        col = j % 2  # 2 columns
        # Label
        itemLabel = tk.Label(leftLabelFrame, text=f"{type[i]} #{j + 1}:", bg="white", font=('Arial', fontS))
        itemLabel.grid(row=count, column=col * 2, sticky="w", padx=5, pady=5)
        # Entry
        itemEntry = tk.Entry(leftLabelFrame, bg="white", highlightthickness=1, borderwidth=1)
        itemEntry.grid(row=count, column=col * 2 + 1, sticky="ew", padx=5, pady=5)

        entryValues.append(itemEntry)

        # Increment row after every 2 entries
        if col == 1:
            count += 1

    # Make all columns expandable
    for c in range(4):  
        leftLabelFrame.grid_columnconfigure(c, weight=1)

#Label Frame for Formatting plots
graphFormatLabelFrame = tk.LabelFrame(leftSideFrame,bg="white",text=f"{labelText.get()} Format")
graphFormatLabelFrame.pack_propagate(False)
graphFormatLabelFrame.pack(fill="both", padx=20, pady=(5, 15), expand=True)
changeContent()

# Buttons container
buttonFrame = tk.Frame(leftSideFrame, bg="white", height=60)
buttonFrame.pack_propagate(False)
buttonFrame.pack(fill="x", padx=20, pady=(0, 10))

containerB = tk.Frame(buttonFrame, bg="white")
containerB.pack(expand=True)

submitButton = tk.Button(containerB, text="Submit", bg="#2E8B57", font=("Arial", 10, "bold"), fg="white", width=10, height=2,  command=lambda :saveFormat(False), activebackground="#3CB371" )
submitButton.pack(side="left", padx=12)

resetButton = tk.Button(containerB, text="Clear All", bg="#CD5C5C", font=("Arial", 10, "bold"), fg="white", width=10, height=2, command=resetButton, activebackground="#E57373" )
resetButton.pack(side="left", padx=12)

# Right Side
rightSideFrame.config(bg="#F3F3F3")
rightSideFrame.pack_propagate(False)
rightSideFrame.pack(expand=True, fill="both", side="left")

# Right Header
rightSideHeadFrame = tk.Frame(rightSideFrame, bg="#3E9063", height=40)
rightSideHeadFrame.pack_propagate(False)
rightSideHeadFrame.pack(fill="x")
rightSideHeadLabel = tk.Label(rightSideHeadFrame, text="Visualization Panel", fg="white", bg="#3E9063", font=("Arial", 14, "bold") )
rightSideHeadLabel.place(relx=0.5,rely=0.5,anchor="center")

#Toggles Var
checkGrid = tk.BooleanVar(value=True)
checkyTick= tk.BooleanVar(value=False)
checkTextOnTop = tk.BooleanVar(value=False)
checkLegend = tk.BooleanVar(value=True)
checkShadow = tk.BooleanVar(value=False)
checkHori = tk.BooleanVar(value=False)
checkPercent =tk.BooleanVar(value=False)
checkPctWhite=tk.BooleanVar(value=False)
checkBoxFrame = tk.Frame(rightSideFrame, width=130, height=500, bg="white", relief="groove", bd=2)
checkBoxFrame.pack_propagate(False)
toggles=[checkGrid,checkyTick,checkTextOnTop,checkLegend,checkHori,checkShadow,checkPercent,checkPctWhite]

def createCheckBox(graphType):
    global checkBoxFrame
    print("Graph TYPE is ",graphType)
    tk.Label(checkBoxFrame, text="Display Options", font=("Arial", 11, "bold"), bg="white", fg="#3E9063" ).grid(row=0, column=0, pady=(10, 10), sticky="w")
    
    if(graphType=="Line Graph"):
        tk.Checkbutton(checkBoxFrame, text="Toggle Grid", command=lambda: toggleFeature("grid"), variable=checkGrid, fg="black", bg="white", font=("Arial", 10) ).grid(row=1, column=0, pady=8, sticky="w")
        tk.Checkbutton(checkBoxFrame, text="Toggle Y Ticks", command=lambda: toggleFeature("yTick"), variable=checkyTick, fg="black", bg="white", font=("Arial", 10) ).grid(row=2, column=0, pady=8, sticky="w")
    elif graphType == "Bar Graph":
        tk.Checkbutton(checkBoxFrame, text="Toggle Grid", command=lambda: toggleFeature("grid"), variable=checkGrid, fg="black", bg="white", font=("Arial", 10) ).grid(row=1, column=0, pady=8, sticky="w")
        tk.Checkbutton(checkBoxFrame, text="Toggle Y Ticks", command=lambda: toggleFeature("yTick"), variable=checkyTick, fg="black", bg="white", font=("Arial", 10) ).grid(row=2, column=0, pady=8, sticky="w")
        tk.Checkbutton(checkBoxFrame, text="Toggle Y Value Text", command=lambda: toggleFeature("textOnTop"), variable=checkTextOnTop, fg="black", bg="white", font=("Ari" "al", 10) ).grid(row=3, column=0, pady=8, sticky="w")
        tk.Checkbutton(checkBoxFrame, text="Toggle Legend", command=lambda: toggleFeature("legend"), variable=checkLegend, fg="black", bg="white", font=("Arial", 10) ).grid(row=4, column=0, pady=8, sticky="w")
        tk.Checkbutton(checkBoxFrame, text="Toggle Horizontal Bar", command=lambda: toggleFeature("shadow"), variable=checkHori, fg="black", bg="white", font=("Arial", 10) ).grid(row=5, column=0, pady=8, sticky="w")
    elif graphType =="Pie Graph":
        tk.Checkbutton(checkBoxFrame, text="Toggle Legend", command=lambda: toggleFeature("legend"), variable=checkLegend, fg="black", bg="white", font=("Arial", 10) ).grid(row=1, column=0, pady=8, sticky="w")
        tk.Checkbutton(checkBoxFrame, text="Toggle Shadow", command=lambda: toggleFeature("shadow"), variable=checkShadow, fg="black", bg="white", font=("Arial", 10) ).grid(row=2, column=0, pady=8, sticky="w")
        tk.Checkbutton(checkBoxFrame, text="Toggle Percentage Text", command=lambda: toggleFeature("shadow"), variable=checkPercent, fg="black", bg="white", font=("Arial", 10) ).grid(row=3, column=0, pady=8, sticky="w")
        tk.Checkbutton(checkBoxFrame, text="Change Color of Percentage Text", command=lambda: toggleFeature("shadow"), variable=checkPctWhite, fg="black", bg="white", font=("Arial", 10) ).grid(row=4, column=0, pady=8, sticky="w")

def toggleEffect(state):
    global checkBoxFrame
    if state:
        print("SHOW TOGGLE")
        checkBoxFrame.destroy()
        checkBoxFrame = tk.Frame(rightSideFrame, width=130, height=500, bg="white", relief="groove", bd=2)
        checkBoxFrame.pack_propagate(False)
        checkBoxFrame.place(relx=1.0, rely=0.08, anchor="ne")
        currentGraph = labelText.get()
        createCheckBox(currentGraph)
    else:
        checkBoxFrame.destroy()

root.mainloop()