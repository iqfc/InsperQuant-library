# Excel files to csv (folder)
import os
import pandas as pd

os.chdir("E:\FACULDADE\IQFC\Dados Indicadores")
files_ = os.listdir()

if "csv" not in files_:
    os.mkdir("csv")

files_ = [_ for _ in files_ if _.split(".")[-1][-4:-1] == "xls" ]

for file_ in files_:
    data = pd.read_excel(file_)
    name = file_.split(".")[0] + ".csv"
    file_path = os.path.join("csv", name)
    data.to_csv(file_path, index = False)

