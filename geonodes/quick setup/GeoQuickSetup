
"""
See YouTube tutorial here: https://youtu.be/Is8Qu7onvzM
"""
import random
import time

import bpy


################################################################
# helper functions BEGIN
################################################################


def purge_orphans():
    """
    Remove all orphan data blocks

    see this from more info:
    https://youtu.be/3rNqVPtbhzc?t=149
    """
    if bpy.app.version >= (3, 0, 0):
        # run this only for Blender versions 3.0 and higher
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    else:
        # run this only for Blender versions lower than 3.0
        # call purge_orphans() recursively until there are no more orphan data blocks to purge
        result = bpy.ops.outliner.orphans_purge()
        if result.pop() != "CANCELLED":
            purge_orphans()


def clean_scene():
    """
    Removing all of the objects, collection, materials, particles,
    textures, images, curves, meshes, actions, nodes, and worlds from the scene

    Checkout this video explanation with example

    "How to clean the scene with Python in Blender (with examples)"
    https://youtu.be/3rNqVPtbhzc
    """
    # make sure the active object is not in Edit Mode
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    # make sure non of the objects are hidden from the viewport, selection, or disabled
    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False

    # select all the object and delete them (just like pressing A + X + D in the viewport)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    # find all the collections and remove them
    collection_names = [col.name for col in bpy.data.collections]
    for name in collection_names:
        bpy.data.collections.remove(bpy.data.collections[name])

    # in the case when you modify the world shader
    # delete and recreate the world object
    world_names = [world.name for world in bpy.data.worlds]
    for name in world_names:
        bpy.data.worlds.remove(bpy.data.worlds[name])
    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]

    purge_orphans()


def active_object():
    """
    returns the currently active object
    """
    return bpy.context.active_object


def time_seed():
    """
    Sets the random seed based on the time
    and copies the seed into the clipboard
    """
    seed = time.time()
    print(f"seed: {seed}")
    random.seed(seed)

    # add the seed value to your clipboard
    bpy.context.window_manager.clipboard = str(seed)

    return seed


def set_fcurve_extrapolation_to_linear():
    for fc in bpy.context.active_object.animation_data.action.fcurves:
        fc.extrapolation = "LINEAR"


def create_data_animation_loop(obj, data_path, start_value, mid_value, start_frame, loop_length, linear_extrapolation=True):
    """
    To make a data property loop we need to:
    1. set the property to an initial value and add a keyframe in the beginning of the loop
    2. set the property to a middle value and add a keyframe in the middle of the loop
    3. set the property the initial value and add a keyframe at the end of the loop
    """
    # set the start value
    setattr(obj, data_path, start_value)
    # add a keyframe at the start
    obj.keyframe_insert(data_path, frame=start_frame)

    # set the middle value
    setattr(obj, data_path, mid_value)
    # add a keyframe in the middle
    mid_frame = start_frame + (loop_length) / 2
    obj.keyframe_insert(data_path, frame=mid_frame)

    # set the end value
    setattr(obj, data_path, start_value)
    # add a keyframe in the end
    end_frame = start_frame + loop_length
    obj.keyframe_insert(data_path, frame=end_frame)

    if linear_extrapolation:
        set_fcurve_extrapolation_to_linear()


def set_scene_props(fps, frame_count):
    """
    Set scene properties
    """
    scene = bpy.context.scene
    scene.frame_end = frame_count

    # set the world background to black
    world = bpy.data.worlds["World"]
    if "Background" in world.node_tree.nodes:
        world.node_tree.nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)

    scene.render.fps = fps

    scene.frame_current = 1
    scene.frame_start = 1


def scene_setup():
    fps = 30
    loop_seconds = 12
    frame_count = fps * loop_seconds

    seed = 0
    if seed:
        random.seed(seed)
    else:
        time_seed()

    clean_scene()

    set_scene_props(fps, frame_count)


################################################################
# helper functions END
################################################################


def update_geo_node_tree(node_tree):
    
    in_node = node_tree.nodes["Group Input"]
    out_node = node_tree.nodes["Group Output"]
    
#    # training
#    node_x_location = 0
#    node_y_location = 0
    
    # Define start location
    node_xC1_location = -100
    node_yC1_location = -200
    
    # Define steps per added node
    node_location_step_x = 250
    node_location_step_y = 200
    
#    # training
#    mesh_cube_node = node_tree.nodes.new(type="GeometryNodeMeshCube")
#    mesh_cube_node.location.x = node_x_location
#    mesh_cube_node.location.y = node_y_location
#    node_x_location += node_location_step_x
#    
#    # training
#    subdivide_mesh_node = node_tree.nodes.new(type="GeometryNodeSubdivideMesh")
#    subdivide_mesh_node.location.x = node_x_location
#    subdivide_mesh_node.location.y = node_y_location
#    node_x_location += node_location_step_x
    
    # Add Distribute Points on Faces node
    distr_points_node = node_tree.nodes.new(type="GeometryNodeDistributePointsOnFaces")
    # Set location of node
    distr_points_node.location.x = node_xC1_location
    distr_points_node.location.y = node_yC1_location
    node_xC1_location += node_location_step_x
    
    # Add Instance on Points node
    instance_points_node = node_tree.nodes.new(type="GeometryNodeInstanceOnPoints")
    # Set location of node
    instance_points_node.location.x = node_xC1_location
    instance_points_node.location.y = node_yC1_location
    node_xC1_location += node_location_step_x
    node_yC1_location += node_location_step_y
    
    # Add Join Geometry node
    join_geometry_node = node_tree.nodes.new(type="GeometryNodeJoinGeometry")
    # Set location of node
    join_geometry_node.location.x = node_xC1_location
    join_geometry_node.location.y = node_yC1_location
    node_xC1_location += node_location_step_x
    
    #Update location of outputnode
    out_node.location.x = node_xC1_location
    out_node.location.y = node_yC1_location
    
#    # training
#    from_node = mesh_cube_node
#    to_node = subdivide_mesh_node
#    node_tree.links.new(from_node.outputs["Mesh"], to_node.inputs["Mesh"])
    
    # Connect specified nodes (from_node to to_node), via specified sockets (from_socket to to_socket)
    from_nodeC1 = in_node
    from_socketC1 = "Geometry"
    to_nodeC1 = distr_points_node
    to_socketC1 = "Mesh"
    node_tree.links.new(from_nodeC1.outputs[from_socketC1], to_nodeC1.inputs[to_socketC1])
    
    from_nodeC1 = distr_points_node
    from_socketC1 = "Points"
    to_nodeC1 = instance_points_node
    to_socketC1 = "Points"
    node_tree.links.new(from_nodeC1.outputs[from_socketC1], to_nodeC1.inputs[to_socketC1])
    
    from_nodeC1 = instance_points_node
    from_socketC1 = "Instances"
    to_nodeC1 = join_geometry_node
    to_socketC1 = "Geometry"
    node_tree.links.new(from_nodeC1.outputs[from_socketC1], to_nodeC1.inputs[to_socketC1])
    
    from_nodeC1 = in_node
    from_socketC1 = "Geometry"
    to_nodeC1 = join_geometry_node
    to_socketC1 = "Geometry"
    node_tree.links.new(from_nodeC1.outputs[from_socketC1], to_nodeC1.inputs[to_socketC1])
    
    from_nodeC1 = join_geometry_node
    from_socketC1 = "Geometry"
    to_nodeC1 = out_node
    to_socketC1 = "Geometry"
    node_tree.links.new(from_nodeC1.outputs[from_socketC1], to_nodeC1.inputs[to_socketC1])
    
    
    

def create_centerpiece():
    bpy.ops.mesh.primitive_plane_add()
    bpy.ops.node.new_geometry_nodes_modifier()
    node_tree = bpy.data.node_groups["Geometry Nodes"]
    update_geo_node_tree(node_tree)


def main():
    """
    Python code to generate an animated geo nodes node tree
    that consists of a subdivided & triangulated cube with animated faces
    """
    scene_setup()
    create_centerpiece()


if __name__ == "__main__":
    main()















#import bpy




#node_tree = bpy.data.node_groups["G"]
#active_node_group = bpy.context.space_data.edit_tree

#print(active_node_group)













# Hämta referens till den aktiva nodgruppen
#node_group = bpy.context.space_data.node_tree

## Skapa en ny Distribute Points on Faces nod och lägg till den i nodgruppen
#distribute_node = node_tree.nodes.new(type='GeometryNodeDistributePoints')
#distribute_node.location = (0, 0)  # Justera positionen vid behov

# Hitta de två markerade noderna som du vill ansluta
#selected_nodes = [node for node in node_group.nodes if node.select]

# Anslut input i distribute_node till Mesh output i första valda noden
#if len(selected_nodes) >= 1:
#    input_socket = distribute_node.inputs['Geometry']
#    output_socket = selected_nodes[0].outputs['Mesh']
#    node_group.links.new(input_socket, output_socket)

# Anslut Points output i distribute_node till Points input i andra valda noden
#if len(selected_nodes) >= 2:
#    output_socket = distribute_node.outputs['Points']
#    input_socket = selected_nodes[1].inputs['Geometry']
#    node_group.links.new(output_socket, input_socket)


#def update_geo_node_tree(node_tree):
#    out_node = node_tree.nodes["Group Output"]
#    distr_node = node_tree.nodes.new(type="GeometryNodeDistributePointsOnFaces")

