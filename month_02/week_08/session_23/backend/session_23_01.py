import os

currend_dir = os.getcwd()
print(f"Cureent directory: {currend_dir}")


data_file= os.path.join(currend_dir, "data", "sample.txt")
print(f"data file path:{data_file}")


if os.path.exists(data_file):
    print(f"File exists: {data_file}")
else:
    print(f"File does not exist: {data_file}")