# Created by sqec aka SquareScreamYT
# https://youtube.com/@sqec

# requires customtkinter and ctkcolorpicker

# Version 1.0

"""
Todo:
Multiple Elements
Color Gradients
TempHigh, StateHigh etc
Frame the Generated Code
"""

import customtkinter as ctk
import tkinter as tk
from CTkColorPicker import *
import re

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

appWidth = 700
appHeight = 500

class PageFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def ask_color():
            pick_color = AskColor() # open the color picker
            color = pick_color.get() # get the color string
            self.ElementColorButton.configure(fg_color=color)
            self.ElemSelectedColor = color

        def othercategory(chosencategory):
            if chosencategory == "Other":
                self.ElementCategoryEnter = ctk.CTkEntry(self,
                    placeholder_text="Other")
                self.ElementCategoryEnter.grid(row=4, column=1,
                    columnspan=4, padx=20,
                    pady=20, sticky="ew")
            else:
                self.ElementCategoryEnter.destroy() 
        
        def finalname(input_str):
            cleaned = re.sub(r'[^a-zA-Z0-9_-]', '', input_str)
            cleaned = cleaned.replace(' ', '_')
            cleaned = cleaned.lower()
            return cleaned
                
        # IMPORTANT!! generate results
        def generatecode():
            if re.sub('_', '', finalname(self.nameEntry.get())) == "":
                elemname = "element_1"
            else:
                elemname = finalname(self.nameEntry.get())
            elemcolor = self.ElemSelectedColor
            elembehavior = self.ElementBehaviorOptionMenu.get()
            elemcategory = self.ElementCategoryOptionMenu.get()
            elemstate = self.stateVar.get()
            elemhidden = self.HiddenVar.get()
            elemhardness = self.HardnessVar.get()
            if re.sub('_', '', finalname(self.breakIntoEntry.get())) == "":
                elembreakinto = "crushed_element"
            else:
                elembreakinto = finalname(self.breakIntoEntry.get())
            endcode =   "elements."+str(elemname)+"\n"\
                        "    color:\""+str(elemcolor)+"\",\n"\
                        "    behavior:behaviors."+str(elembehavior)+",\n"\
                        "    category:\""+str(elemcategory)+",\n"\
                        "    state:\""+str(elemstate)+",\n"\
                        "    hidden:"+str(elemhidden)+",\n"\
                        "    hardness:"+str(elemhardness)+",\n"\
                        "    breakInto:\""+str(elembreakinto)+"\",\n"\
                        "}"
            self.TheActualCode.configure(text=endcode)
            return endcode
            

        self.title("Sandboxels Mod Maker")
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(False, False)

        self.ThePageFrame = PageFrame(master=self, width=700, height=500, corner_radius=0, fg_color="transparent")
        self.ThePageFrame.grid(row=0, column=0, sticky="nsew")

        self.ElementNameLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="Name:")
        self.ElementNameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        self.nameEntry = ctk.CTkEntry(self.ThePageFrame,
                        placeholder_text="element_1")
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        
        self.ElementColorLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="Color:")
        self.ElementColorLabel.grid(row=1, column=0,
                            padx=20, pady=20,
                            sticky="ew")
        
        self.ElemSelectedColor = "#ff0000"
        self.ElementColorButton = ctk.CTkButton(self.ThePageFrame, text="Choose Color", text_color="white", command=ask_color, hover_color="#333", fg_color="red")
        self.ElementColorButton.grid(row=1, column=1,
                                padx=20, pady=20,
                                sticky="ew")
        
        self.ElementBehaviorLabel = ctk.CTkLabel(self.ThePageFrame,
                            text="Behavior:")
        self.ElementBehaviorLabel.grid(row=2, column=0,
                                padx=20, pady=20,
                                sticky="ew")

        self.ElementBehaviorOptionMenu = ctk.CTkOptionMenu(self.ThePageFrame,
                                    values=["POWDER",
                                    "POWDER_OLD",
                                    "AGPOWDER",
                                    "LIQUID",
                                    "LIQUID_OLD",
                                    "AGLIQUID",
                                    "SUPERFLUID",
                                    "SUPERFLUID_OLD",
                                    "LIGHTWEIGHT",
                                    "SLIDE",
                                    "WALL",
                                    "UL_UR",
                                    "UL_UR_OPTIMIZED",
                                    "GAS",
                                    "DGAS",
                                    "GAS_OLD",
                                    "SUPPORT",
                                    "SUPPORTPOWDER",
                                    "DELETE",
                                    "FILL",
                                    "CLONER",
                                    "STURDYPOWDER",
                                    "SELFDELETE",
                                    "FOAM",
                                    "BUBBLE",
                                    "STICKY",
                                    "MOLTEN",
                                    "RADMOLTEN",
                                    "RADPOWDER",
                                    "BOUNCY",
                                    "FLY",
                                    "CRAWLER"])
        self.ElementBehaviorOptionMenu.grid(row=2, column=1,
                                    padx=20, pady=20,
                                    columnspan=3, sticky="ew")
        
        self.ElementCategoryLabel = ctk.CTkLabel(self.ThePageFrame,
                            text="Category:")
        self.ElementCategoryLabel.grid(row=3, column=0,
                                padx=20, pady=20,
                                sticky="ew")

        self.ElementCategoryOptionMenu = ctk.CTkOptionMenu(self.ThePageFrame,
                                    values=["Land",
                                    "Liquids",
                                    "Life",
                                    "Powders",
                                    "Solids",
                                    "Energy",
                                    "Weapons",
                                    "Gases",
                                    "Food",
                                    "Machines",
                                    "Special",
                                    "States"])
                                    # "Other"],command=othercategory)
        self.ElementCategoryOptionMenu.grid(row=3, column=1,
                                    padx=20, pady=20,
                                    columnspan=3, sticky="ew")
        #self.ElementCategoryEnter = ctk.CTkEntry(self,
        #            placeholder_text="Other")

        self.ElementStateLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="State:")
        self.ElementStateLabel.grid(row=5, column=0, 
                            padx=20, pady=20,
                            sticky="ew")

        self.stateVar = tk.StringVar(value="solid")

        self.SolidRadioButton = ctk.CTkRadioButton(self.ThePageFrame,
                                text="Solid",
                                variable=self.stateVar,
                                        value="solid")
        self.SolidRadioButton.grid(row=5, column=1,
                                padx=20, pady=20,
                                sticky="e")

        self.LiquidRadioButton = ctk.CTkRadioButton(self.ThePageFrame,
                                    text="Liquid",
                                    variable=self.stateVar,
                                    value="liquid")
        self.LiquidRadioButton.grid(row=5, column=2,
                                    padx=20, pady=20,
                                    sticky="e")
        
        self.GasRadioButton = ctk.CTkRadioButton(self.ThePageFrame,
                                    text="Gas",
                                    variable=self.stateVar,
                                    value="gas")
        self.GasRadioButton.grid(row=5, column=3,
                                padx=20, pady=20,
                                sticky="e")
        
        self.HiddenVar = tk.StringVar(value="false")
        
        self.ElementHiddenLabel = ctk.CTkLabel(self.ThePageFrame, text="Hidden:")
        self.ElementHiddenLabel.grid(row=6, column=0,
                                padx=20, pady=20)

        self.HiddenRadioButton = ctk.CTkRadioButton(self.ThePageFrame,  
                                        text="Yes",
                                        variable=self.HiddenVar,
                                        value="true")
        self.HiddenRadioButton.grid(row=6, column=1,
                                padx=20, pady=20, sticky="e")

        self.NotHiddenRadioButton = ctk.CTkRadioButton(self.ThePageFrame,
                                            text="No",
                                            variable=self.HiddenVar,
                                            value="false")
        self.NotHiddenRadioButton.grid(row=6, column=2,
                                padx=20, pady=20, sticky="e")
        
        self.ElementBreakIntoLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="Break Into:")
        self.ElementBreakIntoLabel.grid(row=7, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        self.breakIntoEntry = ctk.CTkEntry(self.ThePageFrame,
                        placeholder_text="smashed_element")
        self.breakIntoEntry.grid(row=7, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        
        self.ElementHardnessLabel = ctk.CTkLabel(self.ThePageFrame,
                            text="Hardness:")
        self.ElementHardnessLabel.grid(row=8, column=0,
                                padx=20, pady=20,
                                sticky="e")
        
        self.HardnessVar = ctk.IntVar()
        self.ElementHardnessSlider = ctk.CTkSlider(self.ThePageFrame, from_=0, to=100, variable=self.HardnessVar)
        self.ElementHardnessSlider.grid(row=8, column=1,
                                padx=20, pady=20, sticky="w")
        '''
        self.HardnessDisp = ctk.CTkLabel(self.ThePageFrame, textvariable=HardnessVar)
        self.HardnessDisp.grid(row=8, column=2,
                                padx=20, pady=20,)'''
        

        # generate code
        self.generateCodeButton = ctk.CTkButton(self.ThePageFrame, text="Generate Code", command=generatecode)
        self.generateCodeButton.grid(row=9, column=1, columnspan=3,
                                padx=20, pady=20, sticky="ew")
        
        self.TheActualCode = ctk.CTkLabel(self.ThePageFrame, font=("Fira Code", 15), text_color="#F9FBFE",
                            text="press the generate code button to generate the code")
        self.TheActualCode.grid(row=10, column=1, columnspan=5,
                                padx=20, pady=20,
                                sticky="ew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
