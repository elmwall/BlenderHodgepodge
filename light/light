bl_info = {
    "name": "New Object",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "3D Viewport > Sidebar > Light Panel",
    "description": "Panel for adding lights",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}

# Give Python access to Blender functionality
import bpy

#class LIGHT_operator_addPointLight(bpy.types.Operator):
#    """Create a point light with specific strength and position"""
#    bl_idname = "object.addPointLight"
#    bl_label = "Add Custom Point Light"

class VIEW3D_panel_LightPanel(bpy.types.Panel):
    # Where to add the panel in the UI: in the 3D viewport sidebar region
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    # Labels
    bl_category = "I MADE A PANEL!!!"   # sidebar tab name
    bl_label = "It has TEXT!"       # panel top
    
    # Layout
    def draw(self, context):
        """define panel layout"""
        row = self.layout.row()
        row.operator("object.light_add", text = "And a BUTTONNNN!!!!")

# Register with Blender
def register():
    bpy.utils.register_class(VIEW3D_panel_LightPanel)

def unregister():
    bpy.utils.unregister_class(VIEW3D_panel_LightPanel)
    
if __name__ == "__main__":
    register()
    
#    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
