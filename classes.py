

# Update the Student Class to include these attributes - first_name, last_name, age, country
    #   Add these methods to the Student class
    #          - show_full_name
    #          - year_of_birth
#              -show_initials


class Student:
     school = "AkiraChix"
     def __init__(self,name,age,nationality):
        self.name= name
        self.age = age
        self.nationality = nationality
     def greet_student(self):
          return f"Hello {self.name }  welcome to {self.school}"
     


     def year_of_birth(self):
         year =2023 -self.age
         return f"Hello {self.name} you were born in {year}"

         
         


     def show_full_name(self):
         
         return f"My name is {self.name}"  

     def show_initials(self):
         initial=self.name.split(" ")
         initials=[name[0].upper() for name in initial]
         return ".".join(initials)
     




     

