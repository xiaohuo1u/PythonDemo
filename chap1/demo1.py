import vtk
import cv2

# ply体积测量
# vtkReader=vtk.vtkPolyDataReader()

vtkReader = vtk.vtkPLYReader()

vtkReader.SetFileName("E:\\1111.jpg")

vtkReader.Update()

polydata = vtkReader.GetOutput()

mass = vtk.vtkMassProperties()

mass.SetInputData(polydata)

print("表面积:", mass.GetSurfaceArea())
print("体积:", mass.GetVolume())
