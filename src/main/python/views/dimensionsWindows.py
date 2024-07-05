##############################################################################################
### Import ###################################################################################
##############################################################################################

from tkinter import Button, END, Label, Text, Toplevel

from src.main.python.models import Languages
from src.main.python.utiles import Dimensions

##############################################################################################
### Class ####################################################################################
##############################################################################################

class DimensionsWindows(Toplevel):
    """
    Dimensions of the windows
    """
    components_dim: int = 10  # Dimensions of the components
    language: Languages  # language of the application
    text_area_height: Text  # Text area height
    text_area_width: Text  # Text area width

    def __init__(self, lang: Languages) -> None:
        """
        Constructor of the class
        """
        super().__init__()
        self.language = lang
        self.title(self.language.get_dictionary()["Dim"]["Title"])
        self.create_widgets()
        self.resizable(False, False)

    def create_widgets(self) -> None:
        """
        Create the widgets of the application
        :return: None
        """

        row = 0
        column = 0

        label_1 = Label(
            self, font=("Arial", 10),
            text=f"{self.language.get_dictionary()['Dim']['Height']}"
        )
        label_1.grid(
            row=row, column=column, sticky="nsew"
        )

        column += 1

        self.text_area_height = Text(self, height=1, width=1)
        self.text_area_height.insert(END, Dimensions["Interface"]["Height"])
        self.text_area_height.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        label_2 = Label(
            self, font=("Arial", 10),
            text=f"* {self.language.get_dictionary()['Dim']['Width']}"
        )
        label_2.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        self.text_area_width = Text(self, height=1, width=1)
        self.text_area_width.insert(END, Dimensions["Interface"]["Width"])
        self.text_area_width.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        row += 1
        column = 0

        default = Button(
            self, command=self.default,
            text=f"{self.language.get_dictionary()['Dim']['Default']}"
        )
        default.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        max_dim = Button(
            self, command=self.max_dim,
            text=f"{self.language.get_dictionary()['Dim']['MaxDim']}"
        )
        max_dim.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        validate = Button(
            self, command=self.validate,
            text=f"{self.language.get_dictionary()['Dim']['Validate']}"
        )
        validate.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        cancel = Button(
            self, command=self.cancel,
            text=f"{self.language.get_dictionary()['Dim']['Cancel']}"
        )
        cancel.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

    def validate(self) -> None:
        """
        Validate the dimensions
        :return: None
        """
        try:
            Dimensions["Interface"]["Height"] = int(self.text_area_height.get("1.0", END))
            Dimensions["Interface"]["Width"] = int(self.text_area_width.get("1.0", END))
        except ValueError:
            pass
        self.destroy()

    def cancel(self) -> None:
        """
        Cancel the dimensions
        :return: None
        """
        self.destroy()

    def default(self) -> None:
        """
        Set the default dimensions
        :return: None
        """
        Dimensions["Interface"]["Height"] = Dimensions["Interface_Default"]["Height"]
        Dimensions["Interface"]["Width"] = Dimensions["Interface_Default"]["Width"]
        self.destroy()

    def max_dim(self) -> None:
        """
        Set the max dimensions
        :return: None
        """
        Dimensions["Interface"]["Height"] = self.winfo_screenheight()
        Dimensions["Interface"]["Width"] = self.winfo_screenwidth()
        self.destroy()

##############################################################################################
### End : src/main/python/views/dimensionsWindows.py ##########################################
##############################################################################################
