# Global variables
printers = []
EOL = "\n"

# Class

class Printer: 
    def __init__(self, name, time="") -> None:
        self.name = name
        self.time = time
        self.status = False 
        self.maker = ""

    def name(self):
        return self.name

    def start(self):
        return self.time

    def check_status(self):
        status = ""
        status = "is printing" if self.status else "is free"
        print(f"{self.name} {status}\nPrinting:{self.maker}\nTime:{self.time}")
    
    def new_print(self):
        print("")
        self.status = True
        print(f"Adding new print to {self.name}")
        self.maker = input("Who is printing: ") 
        self.time = input("Enter printing time: ") 
        next_in_waiting()
        print("Your name is automatically moved from the waitinglist")
        get_printers()
    

    def done_printing(self):
        print()
        print(f"{self.name} is now free to use")
        self.maker = ""
        self.time = ""
        self.status = False 
        print() 

# Functions

def options():
    print("(1) See waitinglist")
    print("(2) Add name to waitinglist")
    print("(3) Chose printer to use")
    print("(4) Done printing")
    print("(#) Exit the program.")

def view(): 
    lines = []
    with open('waitinglist.txt') as f: 
        lines = f.readlines() 

    count = 0
    for line in lines:
        count += 1
        print(f'{count}: {line}')


def add_to_list():
    with open("waitinglist.txt", "a", encoding="utf-8") as waiting_list:
        name = input("Enter name:")  
        waiting_list.write(name+"\n")
    get_printers()
    

def pick_printer():
    print()
    print("Choose a printer:")
    print("Pick the index you want to use.")
    for i, printer in enumerate(printers):
        print(f"{i}, {printer.name}")
    pick = input(">>> ")
    return printers[int(pick)]


def used_printer():
    print()
    print("Choose used printer:")
    print("Pick the index you have used.")
    for i, printer in enumerate(printers):
        print(f"{i}, {printer.name}")
    pick = input(">>> ")
    return printers[int(pick)]


def menu():
    choice = ""
    while choice != "#":
        print("""----Options----""")
        options()
        choice = input(">>> ")
        if choice == "1":
            view()

        elif choice == "2":
            add_to_list()

        elif choice == "3":
            printer = pick_printer()
            printer.new_print()

        elif choice == "4":
            printer = used_printer()
            printer.done_printing()

        elif choice == "#":
            # Avslutar loppen och programet
            print("Goodbye!")

        else:
            # Felaktigt input gör att menyn loppas  
            print("Incorrect input")


def next_in_waiting():
    waiters = []
    with open("waitinglist.txt", "r", encoding="utf-8") as f:
        waiters = f.readlines()
    next_in_line = waiters.pop(0)
    with open("waitinglist.txt", "w", encoding="utf-8") as f:
        for line in waiters:
            f.write(line)


def get_printers():
    print()
    print("----Printers----")
    for printer in printers:
        printer.check_status()
        print()


def main():
    
    #global printers
    
    nemy = Printer("Nemy")
    tomda = Printer("Tomda")
    printers.append(nemy)
    printers.append(tomda)
    print("Loading Printers...")
    print("Following printers are online:")
    for printer in printers:
        print(printer.name)

    get_printers()
    menu()
    print()
    
if __name__ == "__main__":
    main()