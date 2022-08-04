FirstName = input('please Enter your first name:')
LastName = input('please Enter your last name:')
IfaAge = input('Do you want Enter your age please ansewer with yes / no .')
IfJob = input('Do you want Enter your job please ansewer with yes / no .')
print('===================================================================')
Mydict = {
    'FirstName': FirstName,
    'LastName': LastName
}
if IfaAge == 'yes':
    age = input('so please enter your age:')
    Mydict['age'] = age
if IfJob == 'yes':
    job = input('so please enter your job:')
    Mydict['job'] = job
print('the user id is ==', Mydict)

