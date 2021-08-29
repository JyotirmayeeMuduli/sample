from member import Member, Gender
class FamilyTree():
    def __init__(self):
        self.family_tree=dict()
    
    
    def add_child(self,name, gender,mother_name="None"):
            #print("hi")
            #print(self.family_tree.items())
            id=len(self.family_tree.keys())+1
            member=Member(id, name,gender)
            
            
            if not self.family_tree:
                
                self.family_tree[name]=member
                member.gender=gender
                print( "CHILD_ADDITION_SUCCEEDED"+member.name)
                return
            if name in self.family_tree:
                
                print("CHILD_ADDITION_FAILED1"+member.name)
                return
            
            mother = self.family_tree.get(mother_name,None)
            
            if not mother:
                print("PERSON NOT FOUND")
                return
            
            if mother.gender!= Gender.female.value:
                
                print("CHILD_ADDITION_FAILED2"+member.name)
                return
            
            father = mother.spouse
            if not father:
                print("CHILD_ADDITION_FAILED3")
                return
            father_name=father.name
            member.set_mother(mother)
            member.set_father(father)
            self.family_tree[mother_name].add_child(member)
            self.family_tree[father_name].add_child(member)
            self.family_tree[name] = member
            member.gender=gender
            
            print( "CHILD_ADDITION_SUCCEEDED"+member.name)
           
            
    def add_spouse(self, name, gender, spouse_name):
            #print("hi")
            _id = len(self.family_tree.keys()) + 1
            member = Member(_id, spouse_name, gender)
            #if tree not empty
            if not self.family_tree:
                print("SPOUSE_ADDITION_FAILED empty 2"+member.name)
                return
            #if spouse exists already
            if spouse_name in self.family_tree.keys():
                print("SPOUSE_ADDITION_FAILED already present"+member.name)
                return
               
            #get spouse object
            spouse = self.family_tree.get(name, None)
            #print(member.id)
            #print(spouse.children)
            if not spouse:
                print("PERSON_NOT_FOUND"+member.name)
                return
            if spouse.gender == member.gender:
                print("SPOUSE_ADDITION_FAILED4"+member.name)
                return
                #spouse is already married
            if spouse.spouse is not None:
                print("SPOUSE_ADDITION_FAILED5"+member.name)
                return

            try:
                
                self.family_tree[spouse_name] = member
               
                member.set_spouse(spouse)
                member.gender=gender
                self.family_tree[spouse_name] = member
                spouse.set_spouse(member)
                
                print("SPOUSE_ADDITION_SUCCEEDED"+member.name)
                
            except ValueError:
                print("SPOUSE_ADDITION_FAILED6"+member.name)
            
    
    def get_relationship(self, name, relationship_type):
       
        member = self.family_tree.get(name, None)
        if not member:
            print("PERSON_NOT_FOUND")
            return
        result = member.get_relationship(relationship_type)
        
        if not result:
            print("None")
        else:
            for res in result:
                #print("printing ",end=" ")
                print(res.name, end=" ")
            print()
            
           
