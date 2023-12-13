from abc import ABCMeta,abstractclassmethod

class personne(metaclass= ABCMeta):
    _counter = 0
    def __init__(self, code , nom , prenom ,age):
        self._code = code
        self._nom = nom
        self._prenom = prenom
        self._age = age
        personne._counter +=1
    
    @property
    def getcode(self):
        return self._code

    @property
    def getnom(self):
        return self._nom
    @property     
    def getprenom(self):
        return self._prenom

    @property
    def getage(self):
        return self._age
    
    @property
    def getcounter(self):
        return self._counter
    
#setters
    def setcode(self,code):
        self._code = code

    def setnom(self,nom):
        self._nom = nom

    def setprenom(self,prenom):
        self._prenom = prenom

    def setage(self,age):
        self._age = age

#methodes
    @abstractclassmethod
    def TOSTRING(self):
        pass

    def equals(self,r2): #the comparison between two code.
        #the first code.
        code1 = self.getcode
        #the second code.
        code2 = r2.getcode
        if (code1 == code2)  :
            return True
        else:
            return False
        
#childs class
class employee(personne):
    _counter = 0
    def __init__(self, code, nom, prenom, age,grade):
        super().__init__(code, nom, prenom, age)
        self._grade = grade
        employee._counter += 1

    @property
    def getgrade(self):
        return self._grade
    
    def setgrade(self,grade):
        self._grade = grade

    def TOSTRING(self):
        print(f" code :{self.getcode}")
        print(f" nom :{self.getnom}")
        print(f" prenom :{self.getprenom}")
        print(f" age :{self.getage}")
        print(f" the grade :{self.getgrade}")


class eleve(personne):
    _counter = 0
    def __init__(self, code, nom, prenom, age,niveau , moyenne):
        super().__init__(code, nom, prenom, age)
        self._niveau = niveau
        self._moyenne = moyenne
        eleve._counter += 1

    @property
    def getniveau(self):
        return self._niveau
    
    @property
    def getmoyenne(self):
        return self._moyenne
    
    def setniveau(self,niveau):
        self._niveau = niveau

    def TOSTRING(self):
        print(f" code :{self.getcode}")
        print(f" nom :{self.getnom}")
        print(f" prenom :{self.getprenom}")
        print(f" age :{self.getage}")
        print(f" the niveau :{self.getniveau}")
        print(f" the moyenne :{self.getmoyenne}")

class test():

    emp1  =    employee("ze","ert","ty",23,45)
    emp2  =    employee("ze","ert","ty",27,85)
    emp3  =    employee("ze","ert","ty",33,47)
    ele1  =    eleve("edc","edcv","ert",15,5,15)
    ele2  =    eleve("edc","edcv","ert",19,9,16)
    ele3  =    eleve("edc","edcv","ert",17,7,19)

    emp1.TOSTRING()
    emp2.TOSTRING()
    emp3.TOSTRING()
    
    ele1.TOSTRING()
    ele2.TOSTRING()
    ele3.TOSTRING()

    #ele1  =    personne("edc","edcv","ert",15)
    #ele2  =    personne("edc","edcv","ert",19)
    if ele1.equals(ele2) == True:
        print("equal.")

    else :
        print("not")

    print(personne._counter)
    print("employes",employee._counter)
    print("eleves",eleve._counter)




    



    

