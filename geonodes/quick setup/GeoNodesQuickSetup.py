bl_info = {
    "name": "GeoNodes Quick Setup",
    "author": "JonasE",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "description": "Adds a setup in Geometry Nodes for distributing instances on faces",
    "warning": "",
    "doc_url": "",
    "category": "Geometry Nodes",
}


import bpy


def create_node(node_tree, type_name, node_x_location, node_y_location, node_location_step_x, node_location_step_y):
    # Add node
    node_obj = node_tree.nodes.new(type=type_name)
    # Set location of node
    node_obj.location.x = node_x_location
    node_obj.location.y = node_y_location
    node_x_location += node_location_step_x
    node_y_location += node_location_step_y
    
    return node_obj, node_x_location, node_y_location


def connect_sockets(node_tree, from_node, to_node, from_socket, to_socket):
    
    # Connect specified nodes (from_node to to_node), via specified sockets (from_socket to to_socket)
    node_tree.links.new(from_node.outputs[from_socket], to_node.inputs[to_socket])


def update_geo_node_tree(node_tree):
    
    in_node = node_tree.nodes["Group Input"]
    out_node = node_tree.nodes["Group Output"]
    
   
    node_x_location = -100
    node_y_location = -200
    
    
    distr_points_node, node_x_location, node_y_location = create_node(node_tree, "GeometryNodeDistributePointsOnFaces", node_x_location, node_y_location, 250, 0)
    
    instance_points_node, node_x_location, node_y_location = create_node(node_tree, "GeometryNodeInstanceOnPoints", node_x_location, node_y_location, 250, 200)
    
    join_geometry_node, node_x_location, node_y_location = create_node(node_tree, "GeometryNodeJoinGeometry", node_x_location, node_y_location, 250, 0)
    
    
    #Update location of outputnode
    out_node.location.x = node_x_location
    out_node.location.y = node_y_location
    
    connect_sockets(node_tree, in_node, distr_points_node, "Geometry", "Mesh")
    
    connect_sockets(node_tree, distr_points_node, instance_points_node, "Points", "Points")
    
    connect_sockets(node_tree, instance_points_node, join_geometry_node, "Instances", "Geometry")
    
    connect_sockets(node_tree, in_node, join_geometry_node, "Geometry", "Geometry")
    
    connect_sockets(node_tree, join_geometry_node, out_node, "Geometry", "Geometry")
    

#def create_centerpiece():
#    bpy.ops.mesh.primitive_plane_add()
#    bpy.ops.node.new_geometry_nodes_modifier()
#    node_tree = bpy.data.node_groups["Geometry Nodes"]
#    update_geo_node_tree(node_tree)


def main():
#    node_tree = bpy.data.node_groups["Geometry Nodes"]
    active_object = bpy.context.active_object
    for modifier in active_object.modifiers:
                # Kontrollera om modifiern är en Geometry Nodes-modifier
                if modifier.type == 'NODES':
                    # Hämta nodgruppen för Geometry Nodes-modifiern
                    node_tree = modifier.node_group
    update_geo_node_tree(node_tree)




class RunGeoNodeQuickSetup(bpy.types.Operator):
    bl_idname = "node.run_geonode_quicksetup"
    bl_label = "Run Geo Node Quick Setup"
    
    def execute(self, context):
        # Placera din skriptkod här
        active_object = context.active_object
        
        if active_object and active_object.type == 'MESH':
            # Loopa igenom alla modifierns objekt
            for modifier in active_object.modifiers:
                # Kontrollera om modifiern är en Geometry Nodes-modifier
                if modifier.type == 'NODES':
                    # Hämta nodgruppen för Geometry Nodes-modifiern
                    main()
                    break
        
        return {'FINISHED'}


class GEONODE_panel_nodesetup(bpy.types.Panel):
    # Where to add the panel in the UI: in the 3D viewport sidebar region
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    
    # Labels
    bl_category = "Quick Setup"   # sidebar tab name
    bl_label = "Setups"       # panel top
    
    bl_idname = "NODE_EDITOR_PT_my_panel"
    
    # Layout
    def draw(self, context):
        """define panel layout"""
        layout = self.layout
        layout.operator("node.run_geonode_quicksetup", text = "Instances on Faces")

quicksetup_classes = (
    RunGeoNodeQuickSetup,
    GEONODE_panel_nodesetup
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






