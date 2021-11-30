import os
import sys


class Passenger:
    __slots__ = "name", "ticket_number", "bags"

    def __init__(self, name, ticket_number:int,bags):
        self.name = name
        self.ticket_number = ticket_number
        self.bags = bags

    def __str__(self):
        return self.name+", Ticket: "+self.ticket_number+", Carry On: "+self.bags


class Gate:
    __slots__ = "passengerList", "gateCapacity", "aircraftCapacity", "gateList", "aircraftList","passengerCount"

    def __init__(self, passengerList:list, gateCapacity:int, aircraftCapacity:int):
        self.passengerList=passengerList
        self.gateCapacity=gateCapacity
        self.aircraftCapacity=aircraftCapacity
        self.gateList = []
        self.aircraftList = []
        self.passengerCount = len(passengerList)

    def simulation(self):
        print("---------------------------")
        print("|   Beginning simulation   |")
        print("---------------------------")
        while(len(self.passengerList)!=0):
            print("-------------------------------------------")
            print("|   Passengers are lining up at the gate  |")
            print("-------------------------------------------")
            i = 0
            while (i < self.gateCapacity):
                self.gateList.append(self.passengerList[0])  # push 1st element
                print(self.passengerList[0])  # printing each passenger element
                self.passengerList.pop(0)  # pop 1st element
                if(len(self.passengerList)==0):
                    break
                i = i + 1
            print("----------------------------------------------------")
            print("|  The gate is full; remaining passengers must wait |")
            print("----------------------------------------------------")
            # <<<<< Loop to reload passengers from the gate into the aircraft until the gate queue is empty >>>>
            while (len(self.gateList) != 0):
                print("--------------------------------------------")
                print("|   Passengers are boarding the aircraft   |")
                print("--------------------------------------------")

                i = 0
                while i < self.aircraftCapacity:  # transfer from gate to aircraft
                    self.aircraftList.append(self.gateList[0])  # push 1st element
                    print(self.gateList[0])  # printing each passenger element
                    self.gateList.pop(0)  # pop 1st element
                    if(len(self.gateList)==0):
                        break
                    i = i + 1

                if len(self.passengerList) == 0:
                    print("--------------------------------------------")
                    print("|     No more passengers are the gate      |")
                    print("--------------------------------------------")

                print(">>The aircraft is full.\n>>Ready for taking off ...\n>>The aircraft has landed.\n>>Passengers are disembarking...\n\n")

                i = 0
                j = 0
                tempAircraftLen=len(self.aircraftList)
                while(i<tempAircraftLen):
                    x = self.aircraftList[j].bags
                    if "False" in x:
                        print(self.aircraftList[j])
                        self.aircraftList.remove(self.aircraftList[j])
                    else:
                        j = j+1
                    i=i+1

                i=0
                tempAircraftLen = len(self.aircraftList)
                while(i< tempAircraftLen):
                    print(self.aircraftList[0])
                    self.aircraftList.remove(self.aircraftList[0])
                    i= i+1
        print("-----------------------------------------------------------------")
        print("| Simulation complete; all passengers are at their destination! |")
        print("-----------------------------------------------------------------")

# <<<<<<<<<<<<<<<<<<<<<< STORING DATA FROM FILE >>>>>>>>>>>>>>>>>>>>>>>>
def fileReader(filename):

    words = []
    with open(filename) as f:
        for line in f:
            for word in line.split(","):
                words.append(word)

    passengerList = []
    i = 0

    while i < (len(words)) :
        passengerList.append(Passenger(words[i], words[i + 1], words[i + 2]))
        i = i + 3
    return passengerList
# <<<<<<<<<<<<<<<<<<<<<<<< END OF DATA STORAGE >>>>>>>>>>>>>>>>>>>>>>>>>

def main():

    # <<<<<<<<<<<<<<<<<<<<<<<<<CMD LINE INPUTS>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if (len(sys.argv) == 2):
        filename = sys.argv[1]
        while os.path.isfile(filename) == False:
            print("<<<< File not found {", filename, "} >>>>")
            filename = input("Enter a valid filename: ")
        print("*** FILE FOUND ***")

    elif (len(sys.argv) == 1):
        print("Usage: python3 airit_simulation.py {filename}")
        filename = input("Enter a filename: ")
        while ((os.path.isfile(filename) == False)):
            filename = input("Enter a valid filename: ")
        print("*** FILE FOUND ***")

    else:
        filename = input("Enter a filename: ")
        while ((os.path.isfile(filename) == False)):
            filename = input("Enter a valid filename: ")
        print("*** FILE FOUND ***")

    # <<<<<<<<<<<<<<<<<<<< END OF CMD LINE INPUTS >>>>>>>>>>>>>>>>>>>>>>>>>

    passengerList = fileReader(filename)

    # <<<<<<<<<<<<<<<<<<<<<<<<< USER INPUTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    gateCapacity =input("\nGate capacity: ")
    while(gateCapacity.isnumeric()==False):
        print("<<<< Enter a numeric value >>>>")
        gateCapacity=input("Gate capacity: ")
    aircraftCapacity = input("Aircraft Capacity: ")
    while (aircraftCapacity.isnumeric() == False):
        print("<<<< Enter a numeric value >>>>")
        aircraftCapacity = input("Aircraft Capacity: ")

    gateCapacity = int(gateCapacity)
    aircraftCapacity = int(aircraftCapacity)
    # <<<<<<<<<<<<<<<<<<<<<<<<< END OF USER INPUTS >>>>>>>>>>>>>>>>>>>>>>>>




    airport = Gate(passengerList, gateCapacity, aircraftCapacity)
    airport.simulation()


if __name__ == "__main__":
    main()
