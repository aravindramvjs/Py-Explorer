'''kwargs = keyword variable length argument'''
'''which passes the keyword to the argument'''
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person("sarvesh",mob="9080668509",city='chennai')

