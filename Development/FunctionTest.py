modifiers = ("BROCCOLI", "VIEW", "NODES", "STUFF")
print(modifiers)

AO = (
       "yep",
       "yep",
       "nope",
       modifiers
)
print(AO)
print(AO[3])

def is_GeoNode_modifier():
    # Define active object
    active_object = AO
    a = 2
    # Loop through modifiers on active object
    for x in active_object[3]:
        # print(x)
        # Check whether the modifier is a Geometry Nodes modifier
        if x == 'NODES':
            return True, x
        print(x)


test, value = is_GeoNode_modifier()
if test:
    print(value)

in_out = {
    "in1": "",
    "out1": ""
}

print(in_out)
print(in_out["in1"])
