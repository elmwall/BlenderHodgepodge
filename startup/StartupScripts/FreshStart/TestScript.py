# a=int(input("Testvalue: "))
# b = bool(a==1)
# print(b)
# c=int(input("Testvalue 2: "))
# if not c:
#     print("nope")
# def is_new_scene():
#     # Kontrollera om det finns några objekt i scenen
#     if a==1 and not c:
#         return True

# def main():
#     # Kontrollera om scenen är helt ny
#     print("run func")
#     if is_new_scene():
#         print("Success!")

# # is_new_scene()
# main()

FreshStart_ini = "FreshStart_ini.txt"
parameters = {}

with open(FreshStart_ini, "r") as ini:
    for line in ini:
        key, value = line.strip().split(":")
        parameters[key] = value
parameters.pop("Function")

for x in parameters.keys():
    numeral = parameters[x][0]
    parameters[x] = int(numeral)

print()
if parameters["remove_cube"]:
    print("remove cube\n")

if parameters["remove_light"]:
    print("remove light\n")

if parameters["add_sun"]:
    print("add sun")
    energy = float(parameters["sun_strength"])
    print("energy:", energy)
    inclination = float(parameters["sun_inclination"])*10
    print("inclination:", inclination)
    direction = 0-36*float(parameters["sun_direction"])
    print("direction:", direction)
    degrees = (inclination, 0, direction)
    print("degrees:", degrees)

