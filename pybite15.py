names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    i=0
    for name in names:
        offset = 11 -len(names[i])
        print(str(i+1)+". "+names[i]+" "* offset + countries[i])
        i+=1



def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    fmt = '{}. {:<10} {}'
    for i, (name, country) in enumerate(zip(names, countries), 1):
        print(fmt.format(i, name, country))