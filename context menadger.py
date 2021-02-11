class Hacking:
    def __enter__(self):
        print("Start hacking")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End hacking")


with Hacking():
    print("I'm hacking ")
