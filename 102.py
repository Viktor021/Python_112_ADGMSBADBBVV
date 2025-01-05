from plyer import filechooser

file_path = filechooser.open_file()
print("Selected file:", file_path)

files_path = filechooser.open_file(multiple=True)
print("Selected files:", files_path)

save_path = filechooser.save_file()
print("Save file path:", save_path)