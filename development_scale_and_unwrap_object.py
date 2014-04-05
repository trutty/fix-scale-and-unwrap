bl_info = {
    "name": "Fix Scale and Unwrap",
    "author": "Christian Schulz",
    "version": (0, 9),
    "blender": (2, 70),
    "location": "View3D > Toolbar",
    "description": "The method can be performed in object mode. First, the scale of the selected object will be fixed. Afterwards the object will be unwrapped depending on its seams. If multiple objects are selected, every item will be processed.",
    "category": "Object"}

import bpy

class VIEW3D_PT_tools_scaleandunwrapobject(bpy.types.Panel):
    """
    Define the location, name of the plugin within the Blender UI.
    Additionally define in which context the plugin can be executed.
    """
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools'
    bl_context = "objectmode"
    bl_label = "Fix Scale and Unwrap"
    bl_description = "Fix Scale and Unwrap an object"

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        col.operator("object.scale_and_unwrap_object")

class ScaleAndUnwrapObject(bpy.types.Operator):
    """
    Make it possible to undo operations and define certain parameters.
    """
    bl_idname = "object.scale_and_unwrap_object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        """
        1. Set active object to the one selected. If multiple objects are selected it will iterate over every item.
        2. Apply fix scale to the active object
        3. Open the object in edit mode
        4. Select the whole mesh
        5. Unwrap everything (seams should already be marked)
        6. Go back in object mode
        7. If multiple objects are selected, go back to step 1
        8. Report if every item was processed
        """

        # counters for validation
        item_counter = 0
        number_of_items = len(bpy.context.selected_objects)

        # iterate over selected objects
        for obj in bpy.context.selected_objects:

            # set active object
            bpy.context.scene.objects.active = obj

            # check if object is visible to avoid exception
            if bpy.ops.object.mode_set.poll():

                # apply scale
                bpy.ops.object.transform_apply(
                    location=False,
                    rotation=False,
                    scale=True)

                # go in edit mode
                bpy.ops.object.mode_set(mode='EDIT')

                # select everything
                bpy.ops.mesh.select_all(action='SELECT')

                # unwrap
                bpy.ops.uv.unwrap(
                    method='ANGLE_BASED',
                    fill_holes=True,
                    use_subsurf_data=False,
                    correct_aspect=True,
                    margin=0.001)

                # go in object mode
                bpy.ops.object.mode_set(mode='OBJECT')

                item_counter += 1

        self.report(
            {'INFO'},
            'Processed items '+str(item_counter)+'/'+str(number_of_items))

        if item_counter == number_of_items:
            self.report(
                {'INFO'},
                'All items processed')
        else:
            self.report(
                {'ERROR'},
                'Not every item was processed')

        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

    pass

def unregister():
    bpy.utils.unregister_module(__name__)

    pass

if __name__ == '__main__':
    register()

if __name__ == "__main__":
    register()
