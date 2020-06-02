d = {"employees": [{"firstName": "John", "lastName": "Doe"}, {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"}, {"firstName": "Jessy", "lastName": "Petter"}]}

emp = d.get("employees")
print(emp[1])