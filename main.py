"""
Main cli or app entry point
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query_viz import query_transform, viz
import os 


# if __name__ == "__main__":
#     path = "/Repos/ht117@duke.edu/Individual_Project3_Kelly_Tong"
    
#     if os.path.exists(path):
#         os.chdir(path)
#         current_directory = os.getcwd()
#         print(current_directory)
#         extract()
#         load()
#         query_transform()
#         viz()
#     else:
#         print(f"The path {path} does not exist.")

if __name__ == "__main__":
    current_directory = os.getcwd()
    print(current_directory)
    extract()
    load()
    query_transform()
    viz()