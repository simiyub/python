
#__name__ : built in function which gets assigned a name
#if

def my_func():
    print("my_func in check_if_run_directly.py")

print("top level in check_if_run_directly.py")

if __name__ == "__main__":
    print("my_func run directly")
else:
    print("my_func run as an import")