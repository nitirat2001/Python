name=input('name:')
last_name=input('lastname:')
year=input('year:')
branch=input('branch:')
gender=input('gender:') 
address=input('gratuated from:')

class nisit:
    def __init__(self,name,last_name,year,branch,gender,address):
        self.name=name
        self.last_name=last_name
        self.year=year
        self.branch=branch
        self.gender=gender
        self.address=address
    
    def show(self):
        print('-'*15,'แนะนำตัว','-'*15)
        print('Hello my name is:'+self.name,'\nlastname:'+self.last_name,'\nyear:'+self.year,'\nbranch:'+self.branch,'\nGender:'+self.gender,'\ngratuated from:'+self.address)

x=nisit(name,last_name,year,branch,gender,address)        
x.show()




