import unreal
import os

def ImportMeshAndAnimation(meshPath, animDir):
    print(f"loading files: {meshPath} and animations in {animDir}")    
    importTask = unreal.AssetImportTask()
    importTask.filename = meshPath

    fileName = os.path.basename(meshPath).split(".")[0]
    importTask.destination_path = '/Game/' + fileName
    importTask.automated = True
    importTask.save = True
    importTask.replace_existing = True

    importOption = unreal.FbxImportUI()    
    importOption.import_mesh = True
    importOption.import_as_skeletal = True

    # this setting tells unreal to import the blendshapes
    importOption.skeletal_mesh_import_data.set_editor_property('import_morph_targets', True)

    # this setting tells unreal to use frame 0 as the default pose
    importOption.skeletal_mesh_import_data.set_editor_property('use_t0_as_ref_pose', True)

    importTask.options = importOption

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([importTask])


ImportMeshAndAnimation("C:/mayaToUe/alex.fbx", "c:/mayaToUe/animations")
