#MAIN Class
class employee(object):
    def __init__(self,first_name,second_name,salary,experience):
        self.first_name=first_name
        self.second_name=second_name
        self.salary=salary
        self.experience=experience
    #Get Salary wich everyone employee has as default depends on parameters
    def get_salary(self):
        if self.experience>5:
            return self.salary*1.2+500
        elif self.experience>2:
            return self.experience+200
    def __repr__(self):
        return "%s %s: got salary: %s"%(self.first_name,self.second_name,self.get_salary())


class developer(employee):
    def __init__(self,first_name,second_name,salary,experience,higher_manager_first,higher_manager_second):
        self.first_name=first_name
        self.second_name=second_name
        self.salary=salary
        self.experience=experience
        self.higher_manager_first=higher_manager_first
        self.higher_manager_second=higher_manager_second
    def __repr__(self):
        return "%s %s: manager: %s %s, experiance: %s"% \
               (self.first_name,self.second_name,self.higher_manager_first, \
                self.higher_manager_second,self.experience)
class designer(employee):
    def __init__(self,first_name,second_name,salary,experience,higher_manager,effect_coef):
        self.first_name=first_name
        self.second_name=second_name
        self.salary=salary
        self.experience=experience
        self.higher_manager=higher_manager
        self.effect_coef=effect_coef
    # Get salary; Inherit from parent and calculate with effectivness coefficient
    def get_salary(self):
        return super(designer,self).get_salary()*self.effect_coef
class manager(employee):
    def __init__(self,first_name,second_name,salary,experience,higher_manager,devel_t,design_t):
        self.first_name=first_name
        self.second_name=second_name
        self.salary=salary
        self.experience=experience
        self.higher_manager=higher_manager
        self.devel_t=devel_t
        self.design_t=design_t
    def get_salary(self):
        if self.design_t+self.devel_t>10:
            return super(manager,self).get_salary()+300
        elif self.design_t+self.devel_t>5:
            return super(manager,self).get_salary()+200
        if self.devel_t>(self.design_t+self.devel_t)/2:
            return super(manager,self).get_salary()*1.1
#Simple Entry
#Managers Information (Mini Database)
manager_list=["Nikolaienko","Yarosch","Ryrmak"]
manager_dependancy=[["Vladyslav",5,3],["Oleksiy",0,5],["Maksym",5,0]]
#Simple Employee
first_name="Vasya"
second_name="Pypkin"
salary=1000
experience=7
higher_manager_first="Nikolaienko"
# Get information from simple mini database about manager
higher_manager_second=manager_dependancy[manager_list.index(higher_manager_first)][0]
dev_t=manager_dependancy[manager_list.index(higher_manager_first)][1]
des_t=manager_dependancy[manager_list.index(higher_manager_first)][2]
#print information about employee
emp=employee(first_name,second_name,salary,experience)
print(emp)
#print information about developer, who has it's own manager(using infirmation about manager)
emp=developer(first_name,second_name,salary,experience,higher_manager_first,higher_manager_second)
print(emp)
#print information about manager, take into account his data
emp=manager(higher_manager_first,higher_manager_second,salary,experience,"Dmytro",dev_t,des_t)
print(emp)
#check that we have't any double counting
print(emp.get_salary())

