# Created by sqec aka SquareScreamYT
# https://youtube.com/@sqec

# How to use
# Goto the Sandboxels GitHub repo and fork it
# Download the zip file
# Extract the zip file
# Go to the mods folder and create a js file
# Generate an element and paste it in the js file
# Upload the js file to your fork of the Sandboxels repo
# Create a pull request

"""
Todo:
Multiple Elements
Color Gradients
TempHigh, StateHigh etc
Info/Help Button
Behavior Grids
Reactions
"""

import customtkinter as ctk
import tkinter as tk
from CTkColorPicker import *
import re
import pyperclip

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

appWidth = 700
appHeight = 500

class PageFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
class CodeFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def brightness(hex_color):
            """
            Calculate brightness value of a hex color 
            """
            
            # Remove '#' from hex color if present
            hex_color = hex_color.lstrip('#')
            
            # Convert hex to RGB
            r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            # Calculate brightness as average of RGB values
            brightness = (r + g + b) / 3
            
            return brightness

        def ask_color():
            pick_color = AskColor() # open the color picker
            color = pick_color.get() # get the color string
            self.ElementColorButton.configure(fg_color=color)
            if brightness(color) > 160:
                self.ElementColorButton.configure(text_color="black")
            else:
                self.ElementColorButton.configure(text_color="white")
            self.ElemSelectedColor = color

        def othercategory(chosencategory):
            if chosencategory == "Other":
                self.ElementCategoryEnter = ctk.CTkEntry(self.ThePageFrame,
                    placeholder_text="Other")
                self.ElementCategoryEnter.grid(row=5, column=1,
                    columnspan=3, padx=20,
                    pady=20, sticky="ew")
                self.othercat = True
                self.TheCodeFrame.place(x=120, y=770)
            elif chosencategory != "Other" and self.othercat == True:
                self.ElementCategoryEnter.destroy() 
                self.othercat = False
                self.TheCodeFrame.place(x=120, y=700)
        
        def finalname(input_str):
            cleaned = re.sub(r"\s", '_', input_str)
            cleaned = re.sub(r'[^a-zA-Z0-9_-]', '', cleaned)
            cleaned = cleaned.lower()
            return cleaned
        
        def numerify(num):
            numerified = re.sub(r'[^0-9.]', '', num)
            return numerified
                
        # IMPORTANT!! generate results

        self.gencodevar = ""

        def generatecode():
            if re.sub('_', '', finalname(self.nameEntry.get())) == "":
                elemname = "element_1"
            else:
                elemname = finalname(self.nameEntry.get())
            endcode =   "elements."+str(elemname)+"={\n"
            elemcolor = self.ElemSelectedColor
            endcode = endcode+"    color:\""+str(elemcolor)+"\",\n"
            elembehavior = self.ElementBehaviorOptionMenu.get()
            endcode = endcode+"    behavior:behaviors."+str(elembehavior)+",\n"
            if self.ElementCategoryOptionMenu.get() == "Other" and self.othercat == True:
                if re.sub('_', '', finalname(self.ElementCategoryEnter.get())) == "":
                    elemcategory = "Other"
                else:
                    elemcategory = finalname(self.ElementCategoryEnter.get())
            else:
                elemcategory = self.ElementCategoryOptionMenu.get().lower()
            endcode = endcode+"    category:\""+str(elemcategory)+"\",\n"
            elemstate = self.stateVar.get()
            endcode = endcode+"    state:\""+str(elemstate)+"\",\n"
            elemhidden = self.HiddenVar.get()
            endcode = endcode+"    hidden:"+str(elemhidden)+",\n"
            self.HardnessVar = self.hardnessEntry.get()
            if numerify(self.HardnessVar) != ""and re.sub('_', '', finalname(self.breakIntoEntry.get())) != "":
                elemhardness = self.hardnessEntry.get()
                endcode = endcode+"    hardness:"+str(elemhardness)+",\n"
            if re.sub('_', '', finalname(self.breakIntoEntry.get())) == "":
                pass
            else:
                elembreakinto = finalname(self.breakIntoEntry.get())
                endcode = endcode+"    breakInto:\""+str(elembreakinto)+"\",\n"
            
            endcode = endcode+"}"
            self.TheActualCode.configure(text=endcode)
            self.gencodevar = endcode
            return endcode
        def copycode():
            pyperclip.copy(self.gencodevar)
            

        self.title("Sandboxels Mod Maker")
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(False, False)

        self.ThePageFrame = PageFrame(master=self, width=700, height=500, corner_radius=0, fg_color="transparent")
        self.ThePageFrame.grid(row=0, column=0, sticky="nsew")

        self.PopupTitleLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="Sandboxels Mod Maker", font=("Helvetica", 20))
        self.PopupTitleLabel.grid(row=0, column=1,
                            padx=20, pady=20,
                            sticky="ew")

        self.ElementNameLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="Name:")
        self.ElementNameLabel.grid(row=1, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        self.nameEntry = ctk.CTkEntry(self.ThePageFrame,
                        placeholder_text="element_1")
        self.nameEntry.grid(row=1, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        
        self.ElementColorLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="Color:")
        self.ElementColorLabel.grid(row=2, column=0,
                            padx=20, pady=20,
                            sticky="ew")
        
        self.ElemSelectedColor = "#ff0000"
        self.ElementColorButton = ctk.CTkButton(self.ThePageFrame, text="Choose Color", text_color="white", command=ask_color, hover_color="#333", fg_color="red")
        self.ElementColorButton.grid(row=2, column=1, columnspan = 1,
                                padx=20, pady=20,
                                sticky="w")
        
        self.ElementBehaviorLabel = ctk.CTkLabel(self.ThePageFrame,
                            text="Behavior:")
        self.ElementBehaviorLabel.grid(row=3, column=0,
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
        self.ElementBehaviorOptionMenu.grid(row=3, column=1,
                                    padx=20, pady=20,
                                    columnspan=3, sticky="ew")
        
        self.ElementCategoryLabel = ctk.CTkLabel(self.ThePageFrame,
                            text="Category:")
        self.ElementCategoryLabel.grid(row=4, column=0,
                                padx=20, pady=20,
                                sticky="ew")
        
        self.othercat = True
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
                                    "States",
                                    "Other"],command=othercategory)
        self.ElementCategoryOptionMenu.grid(row=4, column=1,
                                    padx=20, pady=20,
                                    columnspan=3, sticky="ew")
        #self.ElementCategoryEnter = ctk.CTkEntry(self,

        self.ElementStateLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="State:")
        self.ElementStateLabel.grid(row=6, column=0, 
                            padx=20, pady=20,
                            sticky="ew")

        self.stateVar = tk.StringVar(value="solid")

        self.SolidRadioButton = ctk.CTkRadioButton(self.ThePageFrame,
                                text="Solid",
                                variable=self.stateVar,
                                        value="solid")
        self.SolidRadioButton.grid(row=6, column=1,
                                padx=20, pady=20,
                                sticky="e")

        self.LiquidRadioButton = ctk.CTkRadioButton(self.ThePageFrame,
                                    text="Liquid",
                                    variable=self.stateVar,
                                    value="liquid")
        self.LiquidRadioButton.grid(row=6, column=2,
                                    padx=20, pady=20,
                                    sticky="e")
        
        self.GasRadioButton = ctk.CTkRadioButton(self.ThePageFrame,
                                    text="Gas",
                                    variable=self.stateVar,
                                    value="gas")
        self.GasRadioButton.grid(row=6, column=3,
                                padx=20, pady=20,
                                sticky="w")
        
        self.HiddenVar = tk.StringVar(value="false")
        
        self.ElementHiddenLabel = ctk.CTkLabel(self.ThePageFrame, text="Hidden:")
        self.ElementHiddenLabel.grid(row=7, column=0,
                                padx=20, pady=20)

        self.HiddenRadioButton = ctk.CTkRadioButton(self.ThePageFrame,  
                                        text="Yes",
                                        variable=self.HiddenVar,
                                        value="true")
        self.HiddenRadioButton.grid(row=7, column=1,
                                padx=20, pady=20, sticky="e")

        self.NotHiddenRadioButton = ctk.CTkRadioButton(self.ThePageFrame,
                                            text="No",
                                            variable=self.HiddenVar,
                                            value="false")
        self.NotHiddenRadioButton.grid(row=7, column=2,
                                padx=20, pady=20, sticky="e")

        
        self.ElementBreakIntoLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="Break Into:")
        self.ElementBreakIntoLabel.grid(row=8, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        self.breakIntoEntry = ctk.CTkEntry(self.ThePageFrame,
                        placeholder_text="smashed_element")
        self.breakIntoEntry.grid(row=8, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        
        self.ElementHardnessLabel = ctk.CTkLabel(self.ThePageFrame,
                            text="Hardness:")
        self.ElementHardnessLabel.grid(row=9, column=0,
                                padx=20, pady=20,
                                sticky="e")
        
        self.HardnessVar = ""
        self.hardnessEntry = ctk.CTkEntry(self.ThePageFrame,
                        placeholder_text="0")
        self.hardnessEntry.grid(row=9, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        '''
        self.HardnessDisp = ctk.CTkLabel(self.ThePageFrame, textvariable=HardnessVar)
        self.HardnessDisp.grid(row=8, column=2,
                                padx=20, pady=20,)'''
        

        # generate code
        self.generateCodeButton = ctk.CTkButton(self.ThePageFrame, text="Generate Code", command=generatecode)
        self.generateCodeButton.grid(row=10, column=1, columnspan=2,
                                padx=20, pady=20, sticky="ew")
        self.copyCodeButton = ctk.CTkButton(self.ThePageFrame, text="Copy Code", command=copycode)
        self.copyCodeButton.grid(row=10, column=3, columnspan=1,
                                padx=20, pady=20, sticky="ew")
        
        # spacing
        self.codeSpacingLabel = ctk.CTkLabel(self.ThePageFrame,
                                text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", font=("Helvetica", 20))
        self.codeSpacingLabel.grid(row=11, column=1, columnspan=2,
                                   padx=20, pady=20, sticky="ew")

        self.TheCodeFrame = CodeFrame(master=self.ThePageFrame, width=500, height=300, corner_radius=20, fg_color="gray")
        self.TheCodeFrame.place(x=120, y=700)
        
        self.TheActualCode = ctk.CTkLabel(self.TheCodeFrame, font=("Fira Code", 15), text_color="#050505", justify="left",
                            text="press the generate code button to generate code")
        self.TheActualCode.grid(row=0, column=1, columnspan=1,
                                padx=20, pady=20,
                                sticky="ew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
