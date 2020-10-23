namespace = {'global': {'parent': 'None', 'children': []}}

def create(namesp, parent):
    namespace[parent]['children'].append(namesp)
    namespace[namesp] = {'parent': parent, 'children': []}  
    
def add(namesp, var):
    namespace[namesp]['children'].append(var)
    namespace[var] = {'parent': namesp}
    
def get(namesp, var):
    if var in namespace[namesp]['children']:
        print(namesp)
    else:
        if namespace[namesp]['parent'] != 'None': 
            get(namespace[namesp]['parent'], var)
        else:
            print('None')
            
for i in range(int(input())):
    cmd, namesp, arg = input().split()
    globals()[cmd](namesp, arg)