class Baggage:
    baggage_list = []  

    def __init__(self, ID, Weight, Departure, Destination, PassengerName):
        self._ID = ID
        self._Weight = Weight
        self._Departure = Departure
        self._Destination = Destination
        self._PassengerName = PassengerName
        Baggage.baggage_list.append(self)

    #顯示資訊
    def DisplayBaggageInfo(self):
        
        print(f"Baggage ID: {self._ID}")
        print(f"Weight: {self._Weight}")
        print(f"Departure: {self._Departure}")
        print(f"Destination: {self._Destination}")
        print(f"Passenger Name: {self._PassengerName}")
        print("================================")

    #更改ID
    def ChangeID(self, NewID):
        self._ID = NewID

    #更改重量
    def ChangeWeight(self, NewWeight):
        self._Weight = NewWeight

    #更改出發地
    def ChangeDeparture(self, NewDeparture):
        self._Departure = NewDeparture 

    #更改目的地
    def ChangeDestination(self, NewDestination):
        self._Destination = NewDestination 

    #更改乘客名字
    def ChangePassengerName(self, NewPassengerName):
        self._PassengerName = NewPassengerName 
   
    #查詢行李
    def SearchBaggage(BaggageID):
        for baggage in Baggage.baggage_list:
            if baggage._ID == BaggageID:
                baggage.DisplayBaggageInfo()
                return
            print(f"The baggage is not found!")





class BoardingPass:
    #BPNumber = Boarding Pass Number  /  BGNumber = Boarding Gate Number 
    def __init__(self, Name, BPNumber, Time, BGNumber, Seat, NumberOfBags, BaggageID):
        self._Name = Name
        self._BPNumber = BPNumber
        self._Time = Time
        self._BGNumber = BGNumber
        self._Seat = Seat
        self._NumberOfBags = NumberOfBags
        self._BaggageID = BaggageID
    
    '''
    def DisplayBoardingPassInfo(self):
        
        print(f"Name: {self._Name}")
        print(f"Boarding Pass Number: {self._BPNumber}")
        print(f"Time: {self._Time}")
        print(f"Boarding Gate Number: {self._BGNumber}")
        print(f"Passenger Seat: {self._Seat}")
        print(f"Number of Baggage: {self._NumberOfBags}")
        print(f"Baggage ID: {self._BaggageID}")
        print("================================") 
    '''    


def main():

    #行李
    Baggage1 = Baggage('B124', 15, 'Taipei', 'New York', 'David')
    Baggage2 = Baggage('B254', 20, 'Tokyo', 'Paris', 'Jane')

    print("==========Baggage Info==========")
    Baggage1.DisplayBaggageInfo()
    
    print("==========Change Info==========")
    Baggage1.ChangeID('B1NEW')
    Baggage1.ChangeWeight(17)
    Baggage1.ChangeDeparture('New York')
    Baggage1.ChangeDestination('Tokyo')
    Baggage1.ChangePassengerName('Harry')
    Baggage1.DisplayBaggageInfo()
    

    print("==========Baggage Info==========")
    Baggage2.DisplayBaggageInfo()
    
    print("==========Change Info==========")
    Baggage2.ChangeID('B2NEW')
    Baggage2.ChangeWeight(13)
    Baggage2.ChangeDeparture('Taipei')
    Baggage2.ChangeDestination('Tokyo')
    Baggage2.ChangePassengerName('Kite')
    Baggage2.DisplayBaggageInfo()
    

    input_id = input("Please enter the Baggage ID: ")
    Baggage.SearchBaggage(input_id)

    '''
    #登機證
    BP1 = BoardingPass('Wilson', 'BP12', '9:00', 'HA85', '1A', 2, 'BP14')
    BP2 = BoardingPass('Eason', 'BP34', '20:00', 'HB97', '2B', 3, 'BP25')

    BP1.DisplayBoardingPassInfo()
    BP2.DisplayBoardingPassInfo()
    '''



if __name__ == "__main__":
    main()    