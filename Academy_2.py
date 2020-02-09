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
            self.salary=self.salary*1.2+500
            return self.salary
        elif self.experience>2:
            self.experience+=200
            return self.salary
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
        super(designer,self).get_salary()
        self.salary=self.salary*self.effect_coef
        return self.salary
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
        super(manager,self).get_salary()
        if self.design_t+self.devel_t>10:
            self.salary+=300
        elif self.design_t+self.devel_t>5:
            self.salary+=200
        if self.devel_t>(self.design_t+self.devel_t)/2:
            self.salary*=1.1
        return self.salary
#Simple Entry
manager_list=["Nikolaienko","Yarosch","Ryrmak"]
manager_dependancy=[["Vladyslav",5,3],["Oleksiy",0,5],["Maksym",5,0]]
first_name="Vasya"
second_name="Pypkin"
salary=1000
higher_manager_first="Nikolaienko"
higher_manager_second=manager_dependancy[manager_list.index(higher_manager_first)][0]
dev_t=manager_dependancy[manager_list.index(higher_manager_first)][1]
des_t=manager_dependancy[manager_list.index(higher_manager_first)][2]
experience=7
emp=employee(first_name,second_name,salary,experience)
print(emp)
emp=developer(first_name,second_name,salary,experience,higher_manager_first,higher_manager_second)
print(emp)
emp=manager(higher_manager_first,higher_manager_second,salary,experience,"Dmytro",dev_t,des_t)
#--------------------------------------------------------------------------------------
#If i uncomment line below it count two times salary and second line would be wrong.
#It's interesting. If it would be a situation when I needed get information few times,
# what should I do?
#--------------------------------------------------------------------------------------
#print(emp)
print(emp.get_salary())
