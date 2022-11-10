import json

class Ticket:

    price = 100.0

    def __init__(self, num, multiplier):
        if (isinstance(num, int) == True):
            self.number = num
        else:
            raise Exception("Ticket number has to be an integer value")
        self.price = round(self.price * multiplier, 2)

    def __getattribute__(self, attr_name):
        try:
            return  object.__getattribute__(self, attr_name)
        except AttributeError:
            return None

class RegularT(Ticket):
    def __init__(self, num):
        Ticket.__init__(self, num, 1.0)
        self.ticketdata = json.dumps(f'{self.number} - regular ticket, price = {self.price}')

class AdvanceT(Ticket):
    def __init__(self, num):
        Ticket.__init__(self, num, 0.6)
        self.ticketdata = json.dumps(f'{self.number} - advance ticket, price = {self.price}')

class StudentT(Ticket):
    def __init__(self, num):
        Ticket.__init__(self, num, 0.5)
        self.ticketdata = json.dumps(f'{self.number} - student ticket , price = {self.price}')

class LateT(Ticket):
    def __init__(self, num):
        Ticket.__init__(self, num, 1.1)
        self.ticketdata = json.dumps(f'{self.number} - late ticket, price = {self.price}')


class Alltickets:
    instances = []

    def addticket(self, ticket):
        if (self.doesexist(ticket.number) == False):
            self.instances.append(ticket)
        else:
            raise Exception("Ticket №", ticket.number, "already exists")

    def doesexist(self, num):
        for ticket in self.instances:
            if ticket.number == num:
                return True
        return False

if __name__ == '__main__':
    alltickets = Alltickets()
    t1 = AdvanceT(1)
    alltickets.addticket(t1)
    t2 = RegularT(2)
    alltickets.addticket(t2)
    t3 = StudentT(3)
    alltickets.addticket(t3)
    t4 = StudentT(4)
    alltickets.addticket(t4)
    t5 = RegularT(5)
    alltickets.addticket(t5)
    t6 = LateT(6)
    alltickets.addticket(t6)
    for ticket in alltickets.instances:
        print(ticket.ticketdata)