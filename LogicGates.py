
class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

class AndGate (BinaryGate):

    def __init__(self,n):
        super(AndGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        super(OrGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):

    def __init__(self,n):
        super(NotGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPin()
        if a:
            return 0
        else:
            return 1

class NandGate(AndGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class NorGate(OrGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class Connector:

    def __init__(self,fgate, tgate):
        self.fromgate = fgate
        self.tgate = tgate

        tgate.setNextPin(self)
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate
"""
G1 = BinaryGate("l1")
G1.getLabel()

g1 = AndGate('G1')
print(g1.getOutput())

g2 = OrGate('G2')
print(g2.getOutput())

g3 = NotGate('G3')
print(g3.getOutput())

g4 = NorGate('G4')
print(g4.getOutput())
"""

def main():
    #prove that NOT( (A and B) or (C and D) ) == Not(A and B) and Not(C and D)
    AB = AndGate('A&B')
    print(AB.getOutput())
    CD = AndGate('C&D')
    ABorCD = OrGate('AB|CD')
    print(CD.getOutput())
    ABorCD.pinA = AB.pinA
    ABorCD.pinB = CD.pinB
    print(ABorCD.getOutput())
    F1 = NotGate('NOT( AB|CD )')
    print(F1.getOutput())

    h1 = NotGate('Not(A&B)')
    print(h1.getOutput())
    h2 = NotGate('Not(C&D)')
    print(h2.getOutput())
    F2 = AndGate('Not(A&B)+Not(C&D)')
    print(F2.getOutput())
    print(F2.getOutput() == F1.getOutput())
main()