import enum
class Gender(enum.Enum):
    male="Male"
    female="Female"

class Member:
    
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=Gender(gender)
        self.mother=None
        self.father=None
        self.spouse=None    
        self.children=[]

    def set_mother(self,mother):
        #print(mother.gender,Gender.female.value)
        if not isinstance(mother,Member):
            raise ValueError("Value error for mother")
        if mother.gender!=Gender.female.value:
            raise ValueError("mother should be female")
        else:
            self.mother=mother

    def set_father(self,father):
        #print(father.gender,Gender.male.value)
        if not isinstance(father,Member):
            raise ValueError("Value error for father")
        if father.gender!=Gender.male.value:
            raise ValueError("father should be male")
        else:
            self.father=father

    def set_spouse(self,spouse):
        if not isinstance(spouse,Member):
            return None
        if self.gender==spouse.gender:
                #print("fun2")
            print("same gender")
        else:
                #print("fun3")
            self.spouse=spouse
    
    def add_child(self,child):
        if not isinstance(child,Member):
            raise ValueError("child should be in members")
        else:
            #print("adding child")
            self.children.append(child)
    def get_paternal_grandmother(self):
        if not self.father:
            return None
        if not self.father.mother:
            return None
        return self.father.mother
    def get_maternal_grandmother(self):
        if not self.mother:
            return None
        if not self.mother.mother:
            return None
        return self.mother.mother
    def get_spouse_mother(self):
        #print(self.spouse)
        if not self.spouse:
            return None
        

        return self.spouse.mother

    def get_paternal_aunt(self):
        #print("paternal aunt")
        grandmother = self.get_paternal_grandmother()
        if not grandmother:
            return None
        if not grandmother.children:
            return None
        else:
            return list(filter(lambda x: x.gender==Gender.female.value, grandmother.children))
    def get_paternal_uncle(self):
        #print("paternal uncle")
        grandmother = self.get_paternal_grandmother()
        if not grandmother:
            return None
        if not grandmother.children:
            return None
        else:
            
            return list(filter(lambda x: x.gender==Gender.male.value and x.name!=self.father.name, grandmother.children))
    
    def get_maternal_aunt(self):
        #print("maternal aunt")
        grandmother = self.get_maternal_grandmother()
        if not grandmother:
            return None
        if not grandmother.children:
            return None
        else:
            
            #print(list(filter(lambda x: x.gender==Gender.female.value and x.name!=self.mother.name, grandmother.children)))
            return list(filter(lambda x: x.gender==Gender.female.value and x.name!=self.mother.name, grandmother.children))
    def get_maternal_uncle(self):
        #print("maternal uncle")
        grandmother = self.get_maternal_grandmother()
        if not grandmother:
            return None
        if not grandmother.children:
            return None
        else:
            return list(filter(lambda x: x.gender==Gender.male.value, grandmother.children))
    def get_sibling_spouses(self):
        siblings = self.get_siblings()
        #print(siblings)
        if not siblings:
            return []
        sibling_spouses = [
            sibling.spouse for sibling in siblings if sibling.spouse
        ]
        return sibling_spouses
    

    def get_spouse_siblings(self):
        if not self.spouse:
            return []
        
        return self.spouse.get_siblings()
    
    def get_sister_inlaw(self):
            
        if not self.get_sibling_spouses():
            results1=[]
        else:
            results1 = [x for x in self.get_sibling_spouses() if x.gender==Gender.female.value]
        
       
        if not self.get_spouse_siblings():
            results2=[]
        else:
            results2 = [x for x in self.get_spouse_siblings() if x.gender==Gender.female.value]
      
        results=results1+results2
        
        
        if not results:
            return []
        return results
    def get_brother_inlaw(self):
        
        if not self.get_sibling_spouses():
            results1=[]
        else:
            results1 = [x for x in self.get_sibling_spouses() if x.gender==Gender.male.value]
        
       
        if not self.get_spouse_siblings():
            results2=[]
        else:
            results2 = [x for x in self.get_spouse_siblings() if x.gender==Gender.male.value]
      
        results=results1+results2
        
        
        if not results:
            return []
        return results
        
    def get_son(self):
        #print("printing son")
        if not self.children:
            return None
        return list(filter(lambda x:x.gender==Gender.male.value , self.children))
    def get_daughter(self):
        #print("printing daughters")
        if not self.children:
            return None
        return list(filter(lambda x:x.gender==Gender.female.value , self.children))
        
    def get_siblings(self): 
        #print("printing siblings")
        #print(self.name)
        #print(self.mother)
        if not self.mother:
            #print(self.mother)
            return None
        if not self.mother.children:

            return None
        #print(list(filter(lambda x:x.name!=self.name , self.mother.children)))
        return list(filter(lambda x:x.name!=self.name ,self.mother.children ))

    def get_relationship(self, relationship_type):
        #print(relationship_type)
        relationship_method_switch = {
            'Paternal-Aunt': self.get_paternal_aunt,
            'Paternal-Uncle': self.get_paternal_uncle,
            'Maternal-Aunt': self.get_maternal_aunt,
            'Maternal-Uncle': self.get_maternal_uncle,
            'Brother-In-Law': self.get_brother_inlaw,
            'Sister-In-Law': self.get_sister_inlaw,
            'Son': self.get_son,
            'Daughter': self.get_daughter,
            'Siblings': self.get_siblings
        }
        
        relationship_method = relationship_method_switch.get(
            relationship_type, None)
        #print(relationship_method)
        if relationship_method:
             return relationship_method()
        else:
            return []
    



    
    
    
    
    
    

    



    


    