import os
import time
import glob
from pathlib import Path
from grid import Grid
from clCalendar import CLCalendar
class FileIO:
    @classmethod
    def writeDataTo(self, reprData, fileName) -> None:
        filePath = Path.cwd() / "SavedData" / (fileName + ".cSheet")
        with open(filePath, "w") as cSheet:
            cSheet.write(reprData)

    @classmethod
    def readDataFrom(self, fileName) -> str:
        outReprData = ""
        filePath = Path.cwd() / "SavedData" / (fileName + ".cSheet")
        if not(filePath.is_file()):
            raise ValueError("filePath does not exist or is not a file.")
        with open(filePath, "r") as cSheet:
            for line in cSheet:
                outReprData += line
        return outReprData
    
    @classmethod
    def _pathFormatter(self, filePath) -> str:
        return repr(filePath)[15:-2]

    @classmethod
    def getFileNames(self) -> list:
        outFileNames = []
        filePath = (Path.cwd() / "SavedData" / "*.cSheet")
        filePath = str(filePath)
        for name in glob.glob(filePath):
            outFileNames.append(str(os.path.basename(name))[:-7])
        return outFileNames

    @classmethod
    def getFileDates(self) -> list:
        outFileDates = []
        filePath = (Path.cwd() / "SavedData" / "*.cSheet")
        filePath = str(filePath)
        for name in glob.glob(filePath):
            outFileDates.append(time.ctime(os.path.getmtime(name)))
        return outFileDates

    @classmethod
    def deleteFile(self, fileName) -> None:
        try:
            filePath = Path.cwd() / "SavedData" / (fileName + ".cSheet")
            os.remove(filePath)
        except:
            print("Invalid selectedFileName.")
        
if __name__ == "__main__":
##    print(repr(Path.cwd() / "SavedData" / "*.cSheet"))
##    
##    output = FileIO._pathFormatter(Path.cwd() / "SavedData" / "*.cSheet")
##    print(output)
####    gObj = Grid.fromRepr("1/1,1/2\nA,B\nTest note...\nNone,X\nX,None")
####    FileIO.writeDataTo(repr(gObj), "test")
####    print(FileIO.readDataFrom("test"))
##    print(FileIO.getFileNames())

    print("File Names:\n")
    print(FileIO.getFileNames())
    print("\nFile Dates:\n")
    print(FileIO.getFileDates())
