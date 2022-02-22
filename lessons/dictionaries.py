"""Demonstratinos of dictionary capabilities."""


# Declaring the type of dictionary 
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key calue pairing in the dictionary 
schools["UNC"] = 19400
schools["duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal represntation
print(schools)

# access a value by its key -- also called lookup
print(f"UNC has {schools['UNC']} students")

# remove a key value pair from a dictionary by its key
schools.pop("duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools 
print(f"Duke is present: {is_duke_present}")

# reassign a key value pair
schools["UNC"] = 20000

print(schools)


# example of empty dictionary literal
schools = {} 
# same as dict()


# Alternatively initliaze key value pairs
schools = {"UNC": 19400, "duke": 6700, "NCSU": 2615}


# example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")


# what happens when you try to access a key that does not exist
print(schools["UNCC"])
