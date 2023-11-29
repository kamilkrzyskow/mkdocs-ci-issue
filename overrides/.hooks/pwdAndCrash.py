import sys
import os

def on_config(config):
    print("---")
    [print(p) for p in sys.path]
    print(f"{os.getcwd()=}")
    print("---")
    
    
def on_post_build(config):
    raise Exception("Abort Deploy Just Testing")