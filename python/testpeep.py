new_dict = dict()

files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
}   


    
for v, k in files.items():
    if k in new_dict:
        new_dict[k].append(v)
        print(v + " In " + k)
    else:
        new_dict[k] = [v]


print(new_dict)
