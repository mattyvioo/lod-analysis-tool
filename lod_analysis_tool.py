import unreal as ue
import math
import csv
import sys
import subprocess
import datetime
import json
from PySide2 import QtUiTools, QtWidgets
from PySide2.QtCore import Qt

import os

current_file_path = os.path.dirname(__file__)
drive = os.path.splitdrive(current_file_path)[0]

jsonfile = open(current_file_path + "//config//config.json", 'r')
config = json.load(jsonfile)

currentDateTime = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

class UnrealUITemplate(QtWidgets.QWidget):
    """
    Create a default tool window.
    """

    # store ref to window to prevent garbage collection
    window = None

    def __init__(self, parent=None):
        """
        Import UI and connect components
        """
        super(UnrealUITemplate, self).__init__(parent)

        # load the created UI widget
        self.widgetPath = current_file_path + "\\"
        self.widget = QtUiTools.QUiLoader().load(
            self.widgetPath + "ToolGUI.ui"
        )  # path to PyQt .ui file

        # attach the widget to the instance of this class (aka self)
        self.widget.setParent(self)

        # find interactive elements of UI
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, "btn_close")
        self.test_text = self.widget.findChild(QtWidgets.QTextEdit, "textEdit")

        self.btn_run = self.widget.findChild(QtWidgets.QPushButton, "runButton")
        self.btn_folderRun = self.widget.findChild(QtWidgets.QPushButton, "runFolderButton")
        self.btn_export = self.widget.findChild(QtWidgets.QPushButton, "exportButton")
        self.txt_assetName = self.widget.findChild(
            QtWidgets.QLabel, "lbl_editAssetName"
        )
        self.txt_assetDensity = self.widget.findChild(
            QtWidgets.QLabel, "lbl_editAssetDensity"
        )
        self.txt_numberLods = self.widget.findChild(
            QtWidgets.QLabel, "lbl_editNumberLods"
        )
        self.txt_numberMats = self.widget.findChild(
            QtWidgets.QLabel, "lbl_editNumberMats"
        )
        self.tbl_lodAnalysis = self.widget.findChild(
            QtWidgets.QTableWidget, "tbl_analysis"
        )
        
        # Create the headers for the CSV export
        self.data = [
            [
                "AssetName",
                "TrianglesNumber",
                "LODIndex",
                "MicrotrianglesNumber",
                "ThinTrianglesNumber",
            ]
        ]
        
        self.asset_reg = ue.AssetRegistryHelpers.get_asset_registry()
        self.modified_paths = []
        self.assetsToFilter = []
        self.static_meshes = []
        self.isLastAnalysisFolder = False
        self.microTrianglesAreaTreshold = config["microTrianglesAreaTreshold"]
        self.thinTrianglesAngleTreshold = config["thinTrianglesAngleTreshold"]
        
        self.newData = []

        self.btn_run.clicked.connect(lambda: self.Run(False))
        self.btn_folderRun.clicked.connect(lambda: self.Run(True))
        self.btn_export.clicked.connect(lambda: self.ExportData(self.data, current_file_path, self.newData, self.isLastAnalysisFolder))
        

    def open_csv(self, file_path: str):
        if sys.platform.startswith('darwin'):  # macOS
            subprocess.call(('open', file_path))
        elif sys.platform.startswith('win32'):  # Windows
            subprocess.call(('start', file_path), shell=True)
        elif sys.platform.startswith('linux'):  # Linux
            subprocess.call(('xdg-open', file_path))
        else:
            print("Unsupported operating system.")
    
    
    def ProcessPaths(self, originalPathsArray: list, modifiedPathArray: list):
        for path in originalPathsArray:
            original_string = path
            modified_string = original_string.replace("/All/", "/", 1)
            modifiedPathArray.append(modified_string)
            
    def GetStaticMeshesInAssets(self, assetsList: list, staticMeshesList: list):    
        for i in range(len(assetsList)):
            for asset in assetsList[i]:
                if asset.get_editor_property("asset_class_path").get_editor_property("asset_name") == "StaticMesh":
                    staticMeshesList.append(asset.get_asset())   
                    
    def showQuestionBox(self, csvPath):
        reply = QtWidgets.QMessageBox.question(self.window, "Open CSV File?", "Do you want to open the newly created CSV file?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.open_csv(csvPath)
        
    def ExportData(self, data, path: str, new_data: list, isFolderExport: bool):
        
        currentDateTime = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        
        current_path = path + "\\data-" + currentDateTime
        
        if isFolderExport:
            for modifiedPath in self.modified_paths:
                current_path = current_path + modifiedPath.replace("/", "-")
        
        current_path = current_path + ".csv"
            
        ue.log("Data exported")
        
        with open(current_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
            
        with open(current_path, "a", newline="") as file:
                    # Create a CSV writer object
                    writer = csv.writer(file)

                    # Write the new data to the CSV file
                    writer.writerows(new_data)
        QtWidgets.QMessageBox.information(self.window, "Success!", "Data exported succesfully.")
        self.showQuestionBox(current_path)
        
    
    
    def ShowWarningMessageBox(self):
        QtWidgets.QMessageBox.warning(self.window, "Warning", "Multiple assets selected. Only the fist one will be shown in the UI, the rest of the data will be shown in the table below.")
        
    def Run(self, isFolderAnalysis):
        
        self.newData = []
        
        self.tbl_lodAnalysis.setRowCount(0)
        editor_utility_library = ue.EditorUtilityLibrary

        def SetItemInTable(self, item: QtWidgets.QTableWidgetItem, indexInTable: int, data: list, row: int):
            item.setText(str(data))
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.tbl_lodAnalysis.setItem(row, indexInTable, item)

        def calculate_angle(a: float, b: float, c: float) -> float:
            direction_a = ue.Vector.direction_unit_to(a, b)
            direction_b = ue.Vector.direction_unit_to(b, c)
            dot_product = ue.Vector.dot(direction_a, direction_b)
            return 180 - ue.MathLibrary.radians_to_degrees(
                ue.MathLibrary.acos(dot_product)
            )
            
        assets = []
        self.static_meshes = []
        self.modified_paths = []

        if isFolderAnalysis == False:
            assets = editor_utility_library.get_selected_assets()
            self.isLastAnalysisFolder = False
        elif isFolderAnalysis == True:
            paths = ue.EditorUtilityLibrary.get_selected_folder_paths()    
            self.ProcessPaths(paths, self.modified_paths)
            assets.append(self.asset_reg.get_assets_by_paths(self.modified_paths, True))
            self.GetStaticMeshesInAssets(assets, self.static_meshes)
            assets = []
            for mesh in self.static_meshes:
                assets.append(ue.StaticMesh.get_default_object().cast(mesh))
            self.isLastAnalysisFolder = True
                
        print(assets)
            
        if len(assets) > 1:
            self.ShowWarningMessageBox()
            
        for asset in assets:
            lod_count = ue.StaticMesh.get_num_lods(asset)
            asset_name = asset.get_name()
            lod_screen_sizes = ue.StaticMeshEditorSubsystem.get_default_object().get_lod_screen_sizes(asset)
            asset_bounds_x = asset.get_bounds().box_extent.x
            asset_bounds_y = asset.get_bounds().box_extent.y
            asset_bounds_z = asset.get_bounds().box_extent.z
            asset_bounds_diameter = math.sqrt(
                pow(asset_bounds_x, 2) + pow(asset_bounds_y, 2) + pow(asset_bounds_z, 2)
            )
            self.txt_assetName.setText(asset_name)
            self.txt_numberMats.setText(
                str(ue.Array.__len__(asset.get_editor_property("static_materials")))
            )
            self.txt_numberLods.setText(str(lod_count))
            
            item_data = []

            for k in range(lod_count):
                sm_description = ue.StaticMesh.get_static_mesh_description(asset, k)
                vertex_density = (
                    sm_description.get_vertex_count() / asset_bounds_diameter
                )
                num_triangles_lod = ue.StaticMesh.get_num_triangles(asset, k)
                micro_triangles_count = 0
                thin_triangles_count = 0
                thin_triangles_count = 0
                microtriangles = []
                thintriangles = []

                row = self.tbl_lodAnalysis.rowCount()
                self.tbl_lodAnalysis.insertRow(row)                

                # Iterating over each triangle to catch micro and thin ones
                for i in range(num_triangles_lod):
                    triangle_vertices = sm_description.get_triangle_vertices(
                        ue.TriangleID(i)
                    )

                    first_vertex_position = sm_description.get_vertex_position(
                        triangle_vertices[3]
                    )
                    second_vertex_position = sm_description.get_vertex_position(
                        triangle_vertices[4]
                    )
                    third_vertex_position = sm_description.get_vertex_position(
                        triangle_vertices[5]
                    )

                    triangle_vertices = [
                        first_vertex_position,
                        second_vertex_position,
                        third_vertex_position,
                    ]

                    first_edge_legth = ue.Vector.distance(
                        first_vertex_position, second_vertex_position
                    )
                    second_edge_length = ue.Vector.distance(
                        second_vertex_position, third_vertex_position
                    )
                    third_edge_lenght = ue.Vector.distance(
                        third_vertex_position, first_vertex_position
                    )

                    triangle_semi_perimeter = (
                        first_edge_legth + second_edge_length + third_edge_lenght
                    ) / 2
                    triangle_area = math.sqrt(
                        triangle_semi_perimeter
                        * (triangle_semi_perimeter - first_edge_legth)
                        * (triangle_semi_perimeter - second_edge_length)
                        * (triangle_semi_perimeter - third_edge_lenght)
                    )

                    
                    # TODO: THIS NEEDS TO BE USER-SETTABLE
                    if triangle_area < self.microTrianglesAreaTreshold:
                        micro_triangles_count += 1
                        microtriangles.append(i)

                    angles = [
                        calculate_angle(
                            first_vertex_position,
                            second_vertex_position,
                            third_vertex_position,
                        ),
                        calculate_angle(
                            second_vertex_position,
                            third_vertex_position,
                            first_vertex_position,
                        ),
                        calculate_angle(
                            third_vertex_position,
                            first_vertex_position,
                            second_vertex_position,
                        ),
                    ]

                    thin_angle_count = 0
                    
                    # TODO: THIS NEEDS TO BE USER-SETTABLE
                    for angle in angles:
                        if angle < self.thinTrianglesAngleTreshold:
                            thin_angle_count += 1

                    if thin_angle_count > 0:
                        thin_triangles_count += 1
                        thintriangles.append(i)
                
                
                # Populating the table        
                item1 = QtWidgets.QTableWidgetItem(asset_name)
                SetItemInTable(self, item1, 0, asset_name, row)

                item2 = QtWidgets.QTableWidgetItem(k)
                SetItemInTable(self, item2, 1, k, row)

                item3 = QtWidgets.QTableWidgetItem(num_triangles_lod)
                SetItemInTable(self, item3, 2, num_triangles_lod, row)
                
                item4 = QtWidgets.QTableWidgetItem(vertex_density)
                SetItemInTable(self, item4, 3, round(vertex_density, 3), row)
                
                item5 = QtWidgets.QTableWidgetItem(lod_screen_sizes[k])
                SetItemInTable(self, item5, 4, f"{round(lod_screen_sizes[k], 4)*100}%", row)

                item6 = QtWidgets.QTableWidgetItem(str(micro_triangles_count))
                SetItemInTable(self, item6, 5, micro_triangles_count, row)

                item7 = QtWidgets.QTableWidgetItem(thin_triangles_count)
                SetItemInTable(self, item7, 6, thin_triangles_count, row)
                
                table_items = [item1, item2, item3, item4, item5, item6, item7]
                
                for item in table_items:
                    item.setTextAlignment(3)

                # Prepare data for the CSV Export
                current_new_data = [
                    
                        asset_name,
                        num_triangles_lod,
                        k,
                        micro_triangles_count,
                        thin_triangles_count,
                    
                ]
                
                item_data.append(current_new_data)
                
                self.tbl_lodAnalysis.show()
                self.tbl_lodAnalysis.update()
                
            for data in item_data:
                self.newData.append(data)

            self.btn_export.setEnabled(True)
            

            
                
        

    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
        """
        self.widget.resize(self.width(), self.height())

    def closewindow(self):
        """
        Close the window.
        """
        self.destroy()


def openWindow():
    """
    Create tool window.
    """
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QtWidgets.QApplication.allWindows():
            if "toolWindow" in win.objectName():  # update this name to match name below
                win.destroy()
    else:
        QtWidgets.QApplication(sys.argv)

    # load UI into QApp instance
    UnrealUITemplate.window = UnrealUITemplate()
    UnrealUITemplate.window.show()
    # update this with something unique to your tool
    UnrealUITemplate.window.setObjectName("LodAnalysisTool")
    UnrealUITemplate.window.setWindowTitle("Lod Analysis Tool v0.2")
    ue.parent_external_window_to_slate(UnrealUITemplate.window.winId())


openWindow()
