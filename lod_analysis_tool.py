import unreal as ue
import math
import csv
import sys
import subprocess
import datetime
import json
from PySide2 import QtUiTools, QtWidgets, QtGui
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt

import os

current_file_path = os.path.dirname(__file__)
drive = os.path.splitdrive(current_file_path)[0]

jsonfile = open(current_file_path + "//config//config.json", 'r')
config = json.load(jsonfile)

currentDateTime = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

class PreferencesUI(QtWidgets.QWidget):

    window = None

    def __init__(self, parent=None):
        """
        Import UI and connect components
        """
        super(PreferencesUI, self).__init__(parent)

        # load the created UI widget
        self.widgetPath = current_file_path + "\\"
        self.widget = QtUiTools.QUiLoader().load(
            self.widgetPath + "preferences.ui"
        )  # path to PyQt .ui file
        
        self.preferencesWidget = None

        # attach the widget to the instance of this class (aka self)
        self.widget.setParent(self)
        self.btn_save = self.widget.findChild(QtWidgets.QPushButton, "saveButton")
        self.preferences_textEdit_triArea = self.widget.findChild(QtWidgets.QLineEdit, "txt_triArea")
        self.preferences_textEdit_triAngle = self.widget.findChild(QtWidgets.QLineEdit, "txt_triAngle")
        self.preferences_textEdit_allowedMicro = self.widget.findChild(QtWidgets.QLineEdit, "txt_allowedMicro")
        self.preferences_textEdit_allowedThin = self.widget.findChild(QtWidgets.QLineEdit, "txt_allowedThin")
        self.preferences_textEdit_allowedTolerance = self.widget.findChild(QtWidgets.QLineEdit, "txt_allowedTolerance")
        
        self.btn_save.clicked.connect(self.savePreferences)
        
        self.preferences_textEdit_triArea.setText(str(config["microTrianglesAreaTreshold"]))
        self.preferences_textEdit_triAngle.setText(str(config["thinTrianglesAngleTreshold"]))
        self.preferences_textEdit_allowedMicro.setText(str(config["allowedMicrotrianglesPercentage"]))
        self.preferences_textEdit_allowedThin.setText(str(config["allowedThintrianglesPercentage"]))
        self.preferences_textEdit_allowedTolerance.setText(str(config["allowedTolerancePercentage"]))
        
    def savePreferences(self):
        config["microTrianglesAreaTreshold"] = int(self.preferences_textEdit_triArea.text())
        config["thinTrianglesAngleTreshold"] = int(self.preferences_textEdit_triAngle.text())
        config["allowedMicrotrianglesPercentage"] = int(self.preferences_textEdit_allowedMicro.text())
        config["allowedThintrianglesPercentage"] = int(self.preferences_textEdit_allowedThin.text())
        config["allowedTolerancePercentage"] = int(self.preferences_textEdit_allowedTolerance.text())
        
        with open(current_file_path + "//config//config.json", 'w') as file:
            json.dump(config, file, indent=4)
        
        QtWidgets.QMessageBox.information(self.window, "Success!", "Preferences saved!.")
        
        
    
        
def openPrefWindow():
    """
    Create tool window.
    """
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QtWidgets.QApplication.allWindows():
            if "preferences" in win.objectName():  # update this name to match name below
                win.destroy()
    else:
        QtWidgets.QApplication(sys.argv)

    # load UI into QApp instance
    UnrealUITemplate.window = PreferencesUI()
    UnrealUITemplate.window.show()
    # update this with something unique to your tool
    UnrealUITemplate.window.setObjectName("Preferences")
    UnrealUITemplate.window.setWindowTitle("Preferences")
    ue.parent_external_window_to_slate(UnrealUITemplate.window.winId())

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
        
        self.preferencesWidget = None

        # attach the widget to the instance of this class (aka self)
        self.widget.setParent(self)

        # find interactive elements of UI
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, "btn_close")
        self.test_text = self.widget.findChild(QtWidgets.QTextEdit, "textEdit")

        self.btn_run = self.widget.findChild(QtWidgets.QPushButton, "runButton")
        self.btn_folderRun = self.widget.findChild(QtWidgets.QPushButton, "runFolderButton")
        self.btn_export = self.widget.findChild(QtWidgets.QPushButton, "exportButton")
        self.btn_preferences = self.widget.findChild(QtWidgets.QAction, "actionPreferences")
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
        self.belowTresholdColor = QColor(0, 255, 0)
        self.maximunTresholdColor = QColor(255, 255, 0)
        self.overTresholdColor = QColor(255, 0, 0)
        
        self.newData = []

        self.btn_run.clicked.connect(lambda: self.Run(False))
        self.btn_folderRun.clicked.connect(lambda: self.Run(True))
        self.btn_export.clicked.connect(lambda: self.ExportData(self.data, current_file_path, self.newData, self.isLastAnalysisFolder))
        self.btn_preferences.triggered.connect(self.OpenPreferencesGUI)
    
    def OpenPreferencesGUI(self):
        openPrefWindow()

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
    
    def SetTextColor(self, countToCheck: float, toleranceCount: float, allowedCount: float):
        tempColor = self.belowTresholdColor
        if countToCheck - toleranceCount > allowedCount:
            tempColor = self.overTresholdColor
        elif countToCheck - toleranceCount < allowedCount:
            tempColor = self.belowTresholdColor
        else:
            tempColor = self.maximunTresholdColor
        return tempColor    
    
    
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

                    
                    if triangle_area < config["microTrianglesAreaTreshold"]:
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
                    
                    for angle in angles:
                        if angle < config["thinTrianglesAngleTreshold"]:
                            thin_angle_count += 1

                    if thin_angle_count > 0:
                        thin_triangles_count += 1
                        thintriangles.append(i)
                
                allowedLodToleranceNumber = num_triangles_lod / 100 * config["allowedTolerancePercentage"]
                allowedMicrotrianglesNumber = num_triangles_lod / 100 * config["allowedMicrotrianglesPercentage"]
                allowedThintrianglesNumber = num_triangles_lod / 100 * config["allowedThintrianglesPercentage"]
                
                microTrianglesTextColor = self.SetTextColor(micro_triangles_count, allowedLodToleranceNumber, allowedMicrotrianglesNumber)
                thinTrianglesTextColor = self.SetTextColor(thin_triangles_count, allowedLodToleranceNumber, allowedThintrianglesNumber)     
                
                values = [asset_name,k, num_triangles_lod, vertex_density, lod_screen_sizes[k], micro_triangles_count, thin_triangles_count]
                table_items = []  
                
                for i, value in enumerate(values):
                    item = QtWidgets.QTableWidgetItem(value)
                    if i == 3:
                        value = round(vertex_density, 3)
                    if i == 4:
                        value = f"{round(value, 4)*100}%"
                    SetItemInTable(self, item, i, value, row)
                    table_items.append(item)
                    
                table_items[5].setForeground(QColor(microTrianglesTextColor))
                table_items[6].setForeground(QColor(thinTrianglesTextColor))
                
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


def openMainWindow():
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


openMainWindow()
