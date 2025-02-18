import shapefile

# import shapely
import os
import utm


file_list = os.listdir("file")
for file in file_list:
    print(file)


#
##
###
## -2191776.1760  4695845.3812
a = [-2191776.1760, 4695845.3812]
b = utm.to_latlon(*a, 49, northern=True)  #
print(b)
