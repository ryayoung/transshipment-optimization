import pandas as pd

class Excel:
    def __init__(self, filename):
        self.file = pd.ExcelFile(filename)
    def sheet_df(self, name):
        return pd.read_excel(self.file, sheet_name=name, index_col=0)
    def print(self):
        print(*self.file.sheet_names, sep="\n")