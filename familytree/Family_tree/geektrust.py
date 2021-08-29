from family import FamilyTree
import sys

class Geektrust:
    def __init__(self):
        self.tree = FamilyTree()
        
    def main(self, filename):
        id=0
        
        with open(filename) as f:
            lines = f.readlines()
        for line in lines:
            
            if line.startswith("ADD_CHILD"):
                line=line.rstrip('\n')

                if len(line.split(' '))==3:
                    method, name, gender = line.split(' ')
                    id += 1
                    #print(id)
                    self.tree.add_child(name, gender)
                
                    
                elif len(line.split(' '))==4:
                    method, mother_name, child_name, gender = line.split(' ')
                    id+=1
                    #print(id)
                    self.tree.add_child(child_name, gender, mother_name)
                    

            if line.startswith("ADD_SPOUSE"):
               
                
                line=line.rstrip('\n')
                if len(line.split(' '))==4:
                    method, name, spouse_name, gender = line.split(' ')
                    id+=1
                    #print(id)
                    self.tree.add_spouse(name, gender, spouse_name)
            
            if line.startswith("GET_RELATIONSHIP"):
                id += 1
               # print(id)
                line=line.rstrip('\n')
                method, name, relationship = line.split(' ')
                self.tree.get_relationship(name, relationship)
        


if __name__=="__main__":
    geektrust = Geektrust()
    filename = sys.argv[1]
    
    geektrust.main('initialization.txt')
    geektrust.main(filename)


    

