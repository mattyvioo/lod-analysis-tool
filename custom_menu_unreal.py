import unreal
import os

current_file_path = os.path.dirname(__file__)
drive = os.path.splitdrive(current_file_path)[0]


@unreal.uclass()
class MyEntryScript(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override=True)
    def execute(self, context):
        unreal.PythonScriptLibrary.execute_python_command(
            current_file_path + "\\lod_analysis_tool.py"
        )


def main():
    menus = unreal.ToolMenus.get()

    # Find the 'edit' menu, this should not fail,
    # but if we're looking for a menu we're unsure about 'if not'
    # works as nullptr check,
    edit = menus.find_menu("LevelEditor.MainMenu.Edit")
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    if not edit:
        print("Failed to find the 'Edit' menu")

    my_menu = main_menu.add_sub_menu("My.Menu", "Python", "My Menu", "Python Tools")

    script_object = MyEntryScript()
    script_object.init_entry(
        "My.Menu", "Python", "My Menu", "Lod Analysis Tool", "Lod Analysis Tool"
    )

    entry = unreal.ToolMenuEntry(
        name="Lod Analysis Tool",
        type=unreal.MultiBlockType.MENU_ENTRY,
        script_object=script_object,
    )

    entry.set_label("Lod Analysis Tool")
    my_menu.add_menu_entry("Items", entry)

    menus.refresh_all_widgets()


if __name__ == "__main__":
    main()
