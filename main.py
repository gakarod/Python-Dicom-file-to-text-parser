import sys
import pydicom
ds = pydicom.dcmread("bmode.dcm")
df = pydicom.dcmread("ttfm.dcm")
sys.stdout = open("dicomoutput.txt", "w")
print (ds)
sys.stdout = open("output2.txt", "w")
print (df)


