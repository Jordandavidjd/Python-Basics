class student:
    # constructor
    def __init__(self, name, branch, usn):
        self.name = name
        self.branch = branch
        self.usn = usn
        self.display()

    def display(self):
        print("Name is ", self.name)
        print("Branch is ", self.branch)
        print("Usn is ", self.usn)


s1 = student("Shwetha", "Ec", "1at20ec139")
