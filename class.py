class employee:
    def __init__ (self,fname,lname,salary):
        self.fname=fname
        self.lname = lname
        self.salary = salary



harry = employee('namrata','singh',100000)


print(harry.fname,harry.lname,harry.salary)
