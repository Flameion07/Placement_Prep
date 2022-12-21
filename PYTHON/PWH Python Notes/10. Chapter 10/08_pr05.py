class Train:
    
    def __init__(self) -> None:
        self.seats = 78
        self.fare = 175

    def bookTicket(self):
        self.seats -= 1

    def getStatus(self):
        print(self.seats)

    def getFareInfo(self):
        print(self.fare) 

tr = Train()
tr.getFareInfo()
tr.getStatus()
tr.bookTicket()
tr.getStatus()