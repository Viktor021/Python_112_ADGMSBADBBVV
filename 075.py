from zipfile import ZipFile

with ZipFile("binod.zip", "r") as zip_object:
    zip_object.extractall()

print(zip_object.namelist())