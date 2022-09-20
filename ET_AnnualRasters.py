#-------------------------------------------------------------------------------
# Name:        Annual ET totals
# Purpose:     Creates rasters of annual ET totals
#
# Author:      yreygada, Yunuen Reygadas
#
# Created:     09/08/2022
# Copyright:   (c) yreygada 2022
#-------------------------------------------------------------------------------
################################################################################
#Import modules
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True
################################################################################
# SET BEFORE RUNNING THE SCRIPT
startYear= 2021
endYear= 2021
path =  'D:/Yunuen/6PostDoc/Data/ET/Rasters' #This is the directory in which you have the ET rasters
studyArea= 'D:/Yunuen/6PostDoc/Data/Transfer/Layers/Extended_sa.shp' # This is the study area polygon in .shp format
cellSize = 'D:/Yunuen/6PostDoc/Data/ET/Rasters/m200301_modisSSEBopETv5_actual_mm.tif' # This is any of the ET rasters
################################################################################`
###################### The script starts here ##################################
# Set parameters
arcpy.env.workspace = path
arcpy.env.mask = studyArea
arcpy.env.cellSize = cellSize
arcpy.env.snapRaster = cellSize

# Create a list of years
years = list(range (startYear, endYear+1,1))
print(years)

### Create monthly raster lists
janlist=list()
feblist=list()
marlist=list()
aprlist=list()
maylist=list()
junlist=list()
jullist=list()
auglist=list()
seplist=list()
octlist=list()
novlist=list()
declist=list()

for year in years:
    janlist.append(path +'//'+"m"+str(year)+"01_modisSSEBopETv5_actual_mm.tif")
    feblist.append(path +'//'+"m"+str(year)+"02_modisSSEBopETv5_actual_mm.tif")
    marlist.append(path +'//'+"m"+str(year)+"03_modisSSEBopETv5_actual_mm.tif")
    aprlist.append(path +'//'+"m"+str(year)+"04_modisSSEBopETv5_actual_mm.tif")
    maylist.append(path +'//'+"m"+str(year)+"05_modisSSEBopETv5_actual_mm.tif")
    junlist.append(path +'//'+"m"+str(year)+"06_modisSSEBopETv5_actual_mm.tif")
    jullist.append(path +'//'+"m"+str(year)+"07_modisSSEBopETv5_actual_mm.tif")
    auglist.append(path +'//'+"m"+str(year)+"08_modisSSEBopETv5_actual_mm.tif")
    seplist.append(path +'//'+"m"+str(year)+"09_modisSSEBopETv5_actual_mm.tif")
    octlist.append(path +'//'+"m"+str(year)+"10_modisSSEBopETv5_actual_mm.tif")
    novlist.append(path +'//'+"m"+str(year)+"11_modisSSEBopETv5_actual_mm.tif")
    declist.append(path +'//'+"m"+str(year)+"12_modisSSEBopETv5_actual_mm.tif")

# Calculate Annual ET Sum
counter = startYear
for ls in zip(janlist,feblist,marlist,aprlist,maylist,junlist,jullist,auglist,seplist,octlist,novlist,declist):
##for composite in monthlyCom:
    print (ls)
    compositeSUM = CellStatistics(ls, "SUM", "DATA")
    compositeSUM.save("ETTEST_"+str(counter)+".tif")
    counter =counter+1
    print("***calculated***")
