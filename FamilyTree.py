"""
File:    family_tree.py
Author:  Olufemi telli
Date:    5/17/23
Section: 21
E-mail:  otelli1@umbc.edu
Description:
  Ive created a family tree and you can see who is in the whole family here
"""


# this function makes a person in the family
def create_person(people, name):
    if name in people:
        print(f"{name} already exists.")
    else:
        people[name] = {
            "name": name,
            "mother": None,
            "father": None,
            "children": []
        }
        #prints the name that was created
        print(f"{name} has been created.")

# this function sets the mother for a person
def set_mother(people, person_name, mother_name):
    if person_name not in people or mother_name not in people:
        print("Person or mother not found.")
    else:
        person = people[person_name]
        mother = people[mother_name]
        if person['mother'] is not None:
            print(f"{person_name} already has a mother.")
        else:
            person['mother'] = mother
            mother['children'].append(person)
            print(f"Mother set for {person_name}.")

#This function sets a father for a person
def set_father(people, person_name, father_name):
    if person_name not in people or father_name not in people:
        print("Person or father not found.")
    else:
        person = people[person_name]
        father = people[father_name]
        if person['father'] is not None:
            print(f"{person_name} already has a father.")
        else:
            person['father'] = father
            father['children'].append(person)
            print(f"Father set for {person_name}.")

#this function displays the people in the family
def display_people(people):
    for person_name, person in people.items():
        print(person_name)
        mother_name = person['mother']['name'] if person['mother'] else 'None Listed'
        father_name = person['father']['name'] if person['father'] else 'None Listed'
        children_names = ', '.join(child['name'] for child in person['children'])
        print(f"    Mother: {mother_name}, Father: {father_name}")
        print(f"    Children: {children_names}" if children_names else "    No children")

#This function will show a specific person
def display_person(people, name):
    name = input("Enter the name of the person: ")
    if name in people:
        print(f"{name} already exists.")
    else:
        people[name] = {
            "name": name,
            "mother": None,
            "father": None,
            "children": []
        }
        print(f"{name} has been created.")
    if name not in people:
        print(f"{name} not found.")
    else:
        person = people[name]
        print(person['name'])
        mother_name = person['mother']['name'] if person['mother'] else 'None Listed'
        father_name = person['father']['name'] if person['father'] else 'None Listed'
        children_names = ', '.join(child['name'] for child in person['children'])
        print(f"    Mother: {mother_name}, Father: {father_name}")
        print(f"    Children: {children_names}" if children_names else "    No children")

# this is to check is a person is an ancestor to another person
def is_ancestor(people, ancestor_name, person_name):
    if ancestor_name not in people or person_name not in people:
        print("Person or ancestor not found.")
    else:
        ancestor = people[ancestor_name]
        person = people[person_name]
        if ancestor['name'] == person['name']:
            print(f"This is {person_name}'s father.")
        elif ancestor['mother'] is not None and is_ancestor(people, ancestor['mother']['name'], person_name):
            print(f"Yes, {ancestor_name} is an ancestor of {person_name}.")
        elif ancestor['father'] is not None and is_ancestor(people, ancestor['father']['name'], person_name):
            print(f"Yes, {ancestor_name} is an ancestor of {person_name}.")
        else:
            print(f"No, {ancestor_name} is not an ancestor of {person_name}.")

#THis is to check is a person is a descendant of another person
def is_descendant(people, descendant_name, person_name):
    if descendant_name not in people or person_name not in people:
        print("Person or descendant not found.")
    else:
        descendant = people[descendant_name]
        person = people[person_name]
        if descendant['name'] == person['name']:
            print(f"Yes, {descendant_name} is a descendant of {person_name}.")
        else:
            for child in person['children']:
                if is_descendant(people, descendant_name, child['name']):
                    print(f"Yes, {descendant_name} is a descendant of {person_name}.")
                    return
            print(f"No, {descendant_name} is not a descendant of {person_name}.")

#the bonus I made it check if there are 2 cousins maybe itll give me even more bonus points?
def is_cousin(people, cousin1_name, cousin2_name):
    cousin1 = people.get(cousin1_name)
    cousin2 = people.get(cousin2_name)
    if cousin1 is None or cousin2 is None:
        print("Person not found.")
    else:
        level1_ancestors = set()
        level2_ancestors = set()

        for parent in (cousin1['mother'], cousin1['father']):
            if parent is not None:
                level1_ancestors.update((grandparent['name'] for grandparent in (parent['mother'], parent['father']) if grandparent is not None))

        for parent in (cousin2['mother'], cousin2['father']):
            if parent is not None:
                level2_ancestors.update((grandparent['name'] for grandparent in (parent['mother'], parent['father']) if grandparent is not None))

        common_ancestors = level1_ancestors.intersection(level2_ancestors)
        if common_ancestors:
            print(f"They are {len(common_ancestors)}-cousins, 0 times removed.")
        else:
            print("They are not cousins.")
#The load file function
def load(tree, filename):
    f = open(filename, "r")
    data = json.load(f)
    f.close()

    index = 0
    while index < len(data):
        person_data = data[index]
        name = person_data[0]
        tree.create_person(name)

        person = tree.people[name]
        mother_name = person_data[1]
        father_name = person_data[2]

        if mother_name:
            tree.set_mother(name, mother_name)
        if father_name:
            tree.set_father(name, father_name)

        index += 1

#The save file function
def save(tree, filename):
    f = open(filename, "w")
    data = []

    for person in tree.people.values():
        person_data = [person.name, None, None]

        if person.mother:
            person_data[1] = person.mother.name
        if person.father:
            person_data[2] = person.father.name

        data.append(person_data)

    json.dump(data, f)
    f.close()

#The main function allows a person to see the family tree

if __name__ == "__main__":
    people = {}

    create_person(people, "Gramps")
    create_person(people, "Dad")
    create_person(people, "Mom")
    create_person(people, "Sister")
    create_person(people, "Brother")
    create_person(people, "Cousin")
    create_person(people, "Aunt")
    create_person(people, "Grandma")

    set_father(people, "Mom", "Gramps")
    set_mother(people, "Mom", "Grandma")
    set_father(people, "Sister", "Dad")
    set_mother(people, "Sister", "Mom")
    set_father(people, "Brother", "Dad")
    set_mother(people, "Brother", "Mom")
    set_mother(people, "Cousin", "Aunt")
    set_mother(people, "Aunt", "Grandma")
    set_father(people, "Aunt", "Gramps")

#this is how the family tree is setup and created
    print("\nDisplaying all people:")
    display_people(people)

    print("\nDisplaying person: Mom")
    display_person(people, "Mom")

    print("\nChecking if Dad is a descendant of Gramps:")
    is_descendant(people, "Dad", "Gramps")

    print("\nChecking if Gramps is an ancestor of Mom:")
    is_ancestor(people, "Gramps", "Mom")

    print("\nChecking if Mom is a descendant of Gramps:")
    is_descendant(people, "Mom", "Gramps")

    print("\nChecking if Brother and Cousin are cousins:")
    is_cousin(people, "Brother", "Cousin")
