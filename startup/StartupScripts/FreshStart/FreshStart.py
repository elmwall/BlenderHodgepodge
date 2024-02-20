bl_info = {
    "name": "FreshStart",
    "author": "JonasE",
    "version": (1, 6),
    "blender": (4, 0, 0),
    "description": "Alters set of startup objects",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy
import math


def is_new_scene():
    # Hämta alla objekt i scenen
    all_objects = bpy.context.scene.objects

    # Förväntade objektnamn
    expected_objects = ["Camera", "Cube", "Light"]

    # Hämta de faktiska objektnamnen i scenen
    actual_object_names = [obj.name for obj in all_objects]
    
    # Kontrollera om scenen är sparad 
    is_saved = bpy.data.is_saved

    # Jämför de förväntade objektnamnen med de faktiska och att filen inte är sparad
    # Detta addon ska bara appliceras vid startup av en ny scen och ska inte ha oönskade effekter på en sparad fil.
    # En öppnad sparad fil kan ha fler eller färre objekt och kommer dessutom stå som sparad. 
    # Detta test gör alltså en dubbel kontroll för att säkerställa att det är en helt ny scen.
    if set(actual_object_names) == set(expected_objects) and not is_saved:
        return True


def main(context):
    if is_new_scene():
        # Rensa all tidigare markerad data
        bpy.ops.object.select_all(action='DESELECT')

        # Välj kuben och punktljuset
        cube = bpy.data.objects.get('Cube')
        light = bpy.data.objects.get('Light')

        if cube:
            bpy.context.view_layer.objects.active = cube
            cube.select_set(True)

        if light:
            bpy.context.view_layer.objects.active = light
            light.select_set(True)

        # Ta bort kub och punkljus
        bpy.ops.object.delete(use_global=False)
        
        # Välj kameran
        camera = bpy.data.objects.get('Camera')
        
        # Kontrollera om kameran finns och är synlig
        if camera:
            # Göm kameran
            camera.hide_viewport = True
            camera.hide_render = True
        
        bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(-4, -4, 4), scale=(1, 1, 1))
        
        # Hämta den senast tillagda ljuskällan
        sun = bpy.context.active_object
        
        # Sätt rotation i grader
        rotation_in_degrees = (30, 0, 0)
        rotation_in_radians = [math.radians(deg) for deg in rotation_in_degrees]
        sun.rotation_euler = rotation_in_radians

        # Sätt styrkan till 5
        sun.data.energy = 5.0
        
        # Utskrift för att indikera att main körs vid uppstart.
        # Detta meddelande kommer stå vid uppstart av en ny scen och även av en sparad fil innan själva filen laddas.
        print("FreshStart addon executed at Blender startup.")
    else:
        # Detta meddelande skrivs ut när en sparad fil laddas och försäkrar att innehållet inte påverkats.
        print("FreshStart addon not applied on saved filed.")


# Registera handler för att köra main vid uppstart och avregistrera den direkt efter
bpy.app.handlers.persistent(main)
bpy.app.handlers.load_post.append(main)

def register():
    pass

def unregister():
    # Avregistrera main här om det behövs
    bpy.app.handlers.load_post.remove(main)
    bpy.app.handlers.persistent(main)

if __name__ == "__main__":
    main(None)