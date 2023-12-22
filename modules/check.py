import os

def check():
    try:
        os.mkdir("result")
    except FileExistsError:
        pass