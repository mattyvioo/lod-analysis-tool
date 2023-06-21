
# LoD Analysis Tool

A simple python tool integrated in Unreal Engine to evaluate LoDs in engine.


## Demo

[![Watch the video](https://img.youtube.com/vi/TBobQ3O0bvA/hqdefault.jpg)](https://youtu.be/TBobQ3O0bvA)


## Tech Stack

**Python** - PySide2

**QtDesigner**

**Unreal Engine Python API**


## Installation

Follow the official documentation to integrate Python in the Engine first.
https://docs.unrealengine.com/5.1/en-US/scripting-the-unreal-editor-using-python/

The **custom_menu_unreal.py**, **lod_analysis_tool.py**, **ToolGUI_ui.py** and **ToolGUI.ui** must stay in the same folder.

You can run python scripts in Unreal Engine going to Tools>Execute Python Script.

Run the custom_menu_unreal.py

A new menu on the top bar will appear, you can then launch the tool from there.

    
## Usage

- Run the tool from the custom menu.
- Select a single/multiple StaticMesh asset/s from the content browser
- Click the "Run Analysis" button
- The data will appear on screen.

If multiple assets are selected, only the first one will appear on the first half of the UI, the others will be show on the table below.

You can export data to a CSV file with the "Export Data to CSV" button.


## Screenshots

![tool-screenshot](./resources/images/tool-screenshot.png)


## Roadmap

- Add a GUI to let the user decide the settings of the tool (thresholds for Micro, Thin Triangles, and allowed Vertex Density)
- Let the user select a folder and run the analysis on it
- Color-coding the data to quickly outline if the mesh is valid or not
- Write a proper documentation


## Acknowledgements

 - [Unreal .ui Template](https://gist.github.com/isaacoster/24375ae0fb84dda7aea916077df3f5f4)
 - [Isaac Oster Youtube channel - Unreal python API tutorial](https://www.youtube.com/@IsaacOster)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

