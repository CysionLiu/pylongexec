import json


class People():
    def __init__(self, name, age, pet):
        self.name = name
        self.age = age
        self.pet = pet


class Pet():
    def __init__(self, pet_type, pet_name):
        self.pet_type = pet_type
        self.pet_name = pet_name


def pet2json():
    pet = Pet('Cat', 'Lili')
    js = json.dumps(pet.__dict__)
    print(js)


def simple_person():
    pet = Pet('Cat', 'Lili')
    p = People('Xiaoming', 12,pet.__dict__)
    json_data = json.dumps(p.__dict__)
    print(json_data)


if __name__ == '__main__':
    pet2json()
    simple_person()
