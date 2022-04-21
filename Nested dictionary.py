course={
    'php':{'duration':'2months','fees':15000},
    'python':{'duration':'2months','fees':10000},
    'java':{'duration':'2months','fees':5000}

}
print(course)
course['java']['fees']=2200    #updating value
print(course['python']['fees'])

for k,v in course.items():
    print(k,v['duration'],v['fees'])