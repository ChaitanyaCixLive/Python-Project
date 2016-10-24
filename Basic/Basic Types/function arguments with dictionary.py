def func(name='Bikash', roll=1407001, dept='cse'):
    print(name, roll, dept)

d = {'name': 'roy', 'roll': 1, 'dept': 'CSE'}
func(**d)

d = {'name': 'roy', 'roll': 1}
func(**d)

d = {'name': 'roy', 'roll': 1, 'dept': 'CSE'}
func(d)