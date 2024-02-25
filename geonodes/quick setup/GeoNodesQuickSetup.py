bl_info = {
    "name": "GeoNodes Quick Setup",
    "author": "JonasE",
    "version": (1, 2),
    "blender": (4, 0, 0),
    "description": "Adds a setup in Geometry Nodes for distributing instances on faces",
    "warning": "",
    "doc_url": "",
    "category": "Geometry Nodes",
}


import bpy


# Function for adding new nodes and positioning nodes
def create_node(node_tree, type_name, node_x_location, node_y_location, node_location_step_x, node_location_step_y):
    
    # Add node
    node_obj = node_tree.nodes.new(type=type_name)
    
    # Distance to previous node in x and y, accumulative
    node_x_location += node_location_step_x
    node_y_location += node_location_step_y
    # Set location of node
    node_obj.location.x = node_x_location
    node_obj.location.y = node_y_location
        
    return node_obj, node_x_location, node_y_location


# Function to connect nodes
def connect_sockets(node_tree, from_node, to_node, from_socket, to_socket):
    
    # Connect specified nodes (from_node to to_node), 
    # via specified sockets (from_socket to to_socket)
    node_tree.links.new(from_node.outputs[from_socket], to_node.inputs[to_socket])


# Modify node tree through defined functions for adding and connecting nodes
def update_geo_node_tree(node_tree):
    # Specify nodes which will provide input and receive output from created node setup
    
    in_out = ("Group Input", "Group Output")
    keys = node_tree.nodes.keys()
    
    in_out_values = {
        "Group Input": "",
        "Group Output": ""
    }
    
    for x in in_out:
        if x in keys:
            in_out_values[x] = node_tree.nodes[x]
        else:
            return
    
    in_node, out_node = in_out_values["Group Input"], in_out_values["Group Output"]

#    in_node = node_tree.nodes["Group Input"]
#    out_node = node_tree.nodes["Group Output"]
    
    # Start position of added nodes
    node_x_location = -100
    node_y_location = -200
    
    # Added nodes:
    # Distribute Points on Faces
    # Add Instance on Points
    # Add Join Geometry
    distr_points_node, node_x_location, node_y_location = create_node(node_tree, "GeometryNodeDistributePointsOnFaces", node_x_location, node_y_location, 0, 0)
    instance_points_node, node_x_location, node_y_location = create_node(node_tree, "GeometryNodeInstanceOnPoints", node_x_location, node_y_location, 250, 0)
    join_geometry_node, node_x_location, node_y_location = create_node(node_tree, "GeometryNodeJoinGeometry", node_x_location, node_y_location, 250, 200)
    
    #Update location of outputnode
    out_node.location.x = node_x_location + 250
    out_node.location.y = node_y_location + 0
    
    # Connecttions: 
    # Group Input (Geometry) --> (Mesh) Distribute Points on Faces 
    # Distribute Points on Faces (Points) --> (Points) Instance on Points
    # Instance on Points (Instances) --> (Geometry) Join Geometry
    # Connect: Group Input (Geometry) --> (Geometry) Join Geometry
    # Connect: Join Geometry (Geometry) --> (Geometry) Group Output
    connect_sockets(node_tree, in_node, distr_points_node, "Geometry", "Mesh")
    connect_sockets(node_tree, distr_points_node, instance_points_node, "Points", "Points")
    connect_sockets(node_tree, instance_points_node, join_geometry_node, "Instances", "Geometry")
    connect_sockets(node_tree, in_node, join_geometry_node, "Geometry", "Geometry")
    connect_sockets(node_tree, join_geometry_node, out_node, "Geometry", "Geometry")


# Check modifiers and whether one is a
# The function should only be applied for Geometry Nodes modifier on an active object 
def check_geonode_modifiers():
    # Define active object
    active_object = bpy.context.active_object
    for modifier in active_object.modifiers:
        # Check whether the modifier is a Geometry Nodes modifier
        # Also check if the modifier is active, and thus the one open in Geometry Node Editor
        if modifier.type == "NODES" and modifier.is_active:
            return True, modifier


# Function to call to specify the node tree and run the node tree modifications onto that
def main():
    # Verify Geometry Node group
    is_geonode_modifier, modifier = check_geonode_modifiers()
    # Run functions: Set name of modifier to be edited, and perform modification
    if is_geonode_modifier:
        try:
            node_tree = modifier.node_group
            update_geo_node_tree(node_tree)
        except:
            return


class RunQuickSetup(bpy.types.Operator):
    bl_idname = "node.run_geonode_quicksetup"  # Reference to call the class
    bl_label = "Run GeoNode Quick Setup"
    
    def execute(self, context):
        # Verify Geometry Node group, if true: run main
        try:
            is_geonode_modifier, modifier = check_geonode_modifiers()
        except:
            return {'CANCELLED'}
        if is_geonode_modifier:
            main()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


class GeoNodePanel(bpy.types.Panel):
    # Where to add the panel in the UI: in the 3D viewport sidebar region
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    
    # Labels
    bl_category = "Quick Setup"   # sidebar tab name
    bl_label = "Setups"       # panel top
    
    bl_idname = "NODE_EDITOR_PT_quicksetup_panel"
    
    # Layout
    def draw(self, context):
        """define panel layout"""
        layout = self.layout
        layout.operator("node.run_geonode_quicksetup", text = "Instances on Faces")

quicksetup_classes = (
    RunQuickSetup,
    GeoNodePanel
)



# Register with Blender
def register():
    for cls in quicksetup_classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(quicksetup_classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()






