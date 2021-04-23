import vtk

filename = "E:\\2222.stl"

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
reader.Update()
polydata = reader.GetOutput()

# 获取表面积和体积
mass = vtk.vtkMassProperties()
mass.SetInputData(polydata)

print("Surface = ", mass.GetSurfaceArea())
print("Volume = ", mass.GetVolume())
