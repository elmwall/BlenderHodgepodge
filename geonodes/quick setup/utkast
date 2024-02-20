#import bpy

#class RunGeoNodeScriptOperator(bpy.types.Operator):
#    bl_idname = "object.run_geo_node_script"
#    bl_label = "Run Geo Node Script"
#    
#    def execute(self, context):
#        # Placera din skriptkod här
#        active_object = context.active_object
#        
#        if active_object and active_object.type == 'MESH':
#            # Loopa igenom alla modifierns objekt
#            for modifier in active_object.modifiers:
#                # Kontrollera om modifiern är en Geometry Nodes-modifier
#                if modifier.type == 'NODES':
#                    # Hämta nodgruppen för Geometry Nodes-modifiern
#                    node_group = modifier.node_group

#                    # Placera den nya noden i nodträdet efter önskad position
#                    distribute_node = node_group.nodes.new(type='GeometryNodeDistributePointsOnFaces')
#                    distribute_node.location = (0, 0)
#                    # Anslut noder om det behövs
#                    
#                    # Avbryt loopen efter att den önskade modifiern har hittats
#                    break
#        
#        return {'FINISHED'}

#def register():
#    bpy.utils.register_class(RunGeoNodeScriptOperator)

#def unregister():
#    bpy.utils.unregister_class(RunGeoNodeScriptOperator)

#if __name__ == "__main__":
#    register()



#import bpy

#class RunGeoNodeScriptOperator(bpy.types.Operator):
#    bl_idname = "object.run_geo_node_script"
#    bl_label = "Run Geo Node Script"
#    
#    def execute(self, context):
#        # Placera din skriptkod här
#        active_object = context.active_object
#        
#        if active_object and active_object.type == 'MESH':
#            # Loopa igenom alla modifierns objekt
#            for modifier in active_object.modifiers:
#                # Kontrollera om modifiern är en Geometry Nodes-modifier
#                if modifier.type == 'NODES':
#                    # Hämta nodgruppen för Geometry Nodes-modifiern
#                    node_group = modifier.node_group

#                    # Placera den nya noden i nodträdet efter önskad position
#                    distribute_node = node_group.nodes.new(type='GeometryNodeDistributePointsOnFaces')
#                    distribute_node.location = (0, 0)
#                    # Anslut noder om det behövs
#                    
#                    # Avbryt loopen efter att den önskade modifiern har hittats
#                    break
#        
#        return {'FINISHED'}

#def register():
#    bpy.utils.register_class(RunGeoNodeScriptOperator)

#def unregister():
#    bpy.utils.unregister_class(RunGeoNodeScriptOperator)

#if __name__ == "__main__":
#    register


import bpy

class RunGeoNodeScriptOperator(bpy.types.Operator):
    bl_idname = "object.run_geo_node_script"
    bl_label = "Run Geo Node Script"
    
    def execute(self, context):
        # Hämta det aktiva området (area) i Blender-gränssnittet
        active_area = bpy.context.area
        print(active_area)
#        # Kontrollera om det aktiva området är en Geometry Node Editor
#        if active_area.type == 'NODE_EDITOR' and active_area.spaces.active.type == 'GeometryNodeEditor':
#            # Hämta det aktiva nodträdet i Geometry Node Editor
#            active_node_tree = bpy.context.screen.node_tree

#            # Kontrollera om det finns ett aktivt nodträd
#            if active_node_tree:
#                # Loopa igenom alla noder i det aktiva nodträdet
#                for node in active_node_tree.nodes:
#                    # Kontrollera om noden är en Geometry Nodes-modul
#                    if node.type == 'GeometryNodeTree':
#                        # Nu har du hittat det aktiva nodträdet i Geometry Node Editor
#                        # Du kan göra ändringar här
#                        print("Aktivt nodträd i Geometry Node Editor hittad:", active_node_tree.name)
#                        break
#            else:
#                print("Inget aktivt nodträd i Geometry Node Editor.")
#        else:
#            print("Aktivt område är inte en Geometry Node Editor.")

def register():
    bpy.utils.register_class(RunGeoNodeScriptOperator)

def unregister():
    bpy.utils.unregister_class(RunGeoNodeScriptOperator)

if __name__ == "__main__":
    register()


#import bpy

#class RunGeoNodeScriptOperator(bpy.types.Operator):
#    bl_idname = "object.run_geo_node_script"
#    bl_label = "Run Geo Node Script"
#    
#    def execute(self, context):
#        # Kontrollera om den aktiva redigeraren är en NODE_EDITOR och om det är en GeometryNodeEditor
#        if context.area.type == 'NODE_EDITOR' and context.space_data.tree_type == 'GeometryNodeTree':
#            # Hämta det aktiva nodträdet i Geometry Node Editor
#            active_node_tree = context.space_data.node_tree

#            # Kontrollera om det finns ett aktivt nodträd
#            if active_node_tree:
#                # Loopa igenom alla noder i det aktiva nodträdet
#                for node in active_node_tree.nodes:
#                    # Kontrollera om noden är en Geometry Nodes-modul
#                    if node.type == 'GeometryNodeTree':
#                        # Nu har du hittat det aktiva nodträdet i Geometry Node Editor
#                        # Du kan göra ändringar här
#                        print("Running script in Geometry Node Editor")
#                        return {'FINISHED'}
#        else:
#            print("Script can only be run in the Geometry Node Editor.")
#        
#        return {'CANCELLED'}

#def register():
#    bpy.utils.register_class(RunGeoNodeScriptOperator)

#def unregister():
#    bpy.utils.unregister_class(RunGeoNodeScriptOperator)

#print("check")
#if __name__ == "__main__":
#    register()


#import bpy

## Hämta det aktiva området (area) i Blender-gränssnittet
#active_area = bpy.context.area

## Kontrollera om det aktiva området är en Geometry Node Editor
#if active_area.type == 'NODE_EDITOR' and active_area.spaces.active.type == 'GeometryNodeEditor':
#    # Hämta nodgruppen för den aktiva nodeditorn
#    node_group = active_area.spaces.active.edit_tree
#    if node_group is not None:
#        # Gör något med nodgruppen
#        print("Aktiv nodgrupp i Geometry Node Editor hittad:", node_group.name)
#    else:
#        print("Ingen aktiv nodgrupp i Geometry Node Editor hittad.")
#else:
#    print("Aktivt område är inte en Geometry Node Editor.")



#import bpy

## Hämta det aktiva området (area) i Blender-gränssnittet
#active_area = bpy.context.area

## Kontrollera om det aktiva området är en Geometry Node Editor
#if active_area.type == 'NODE_EDITOR' and active_area.spaces.active.type == 'GeometryNodeEditor':
#    # Hämta det aktiva nodträdet i Geometry Node Editor
#    active_node_tree = bpy.context.screen.node_tree

#    # Kontrollera om det finns ett aktivt nodträd
#    if active_node_tree:
#        # Loopa igenom alla noder i det aktiva nodträdet
#        for node in active_node_tree.nodes:
#            # Kontrollera om noden är en Geometry Nodes-modul
#            if node.type == 'GeometryNodeTree':
#                # Nu har du hittat det aktiva nodträdet i Geometry Node Editor
#                # Du kan göra ändringar här
#                print("Aktivt nodträd i Geometry Node Editor hittad:", active_node_tree.name)
#                break
#    else:
#        print("Inget aktivt nodträd i Geometry Node Editor.")
#else:
#    print("Aktivt område är inte en Geometry Node Editor.")