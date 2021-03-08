#!/usr/bin/python

#mime_type=

import extfs
import sys
import os.path
import subprocess
import struct
import time
import magic
from math import log

def usage():
   print("usage " + sys.argv[0] + " <image file> <offset> <inode number> \n"\
     "Displays file for an inode from an image file")
   exit(1)

def main():
  if len(sys.argv) < 3: 
     usage()

  # read first sector
  if not os.path.isfile(sys.argv[1]):
     print("File " + sys.argv[1] + " cannot be openned for reading")
     exit(1)
  emd = extfs.ExtMetadata(sys.argv[1], sys.argv[2])
  # get inode location
  inodeLoc = extfs.getInodeLoc(sys.argv[3], emd.superblock.inodesPerGroup)
  offset = emd.bgdList[inodeLoc[0]].inodeTable * emd.superblock.blockSize + \
    inodeLoc[1] * emd.superblock.inodeSize 
  with open(str(sys.argv[1]), 'rb') as f:
    f.seek(offset + int(sys.argv[2]) * 512)
    data = str(f.read(emd.superblock.inodeSize))
  inode = extfs.Inode(data, emd.superblock.inodeSize)
  datablock = extfs.getBlockList(inode, sys.argv[1], sys.argv[2], \
    emd.superblock.blockSize)
  data = ""
  if inode.fileType == "Directory":
    #print directory contents
    for db in datablock:
      data += extfs.getDataBlock(sys.argv[1], long(sys.argv[2]), \
        db, emd.superblock.blockSize)
    dir_data = extfs.getDirectory(data)
    for fname in dir_data:
        fname.prettyPrint()
  #if directory do this
    #if file do this
  if inode.fileType == "Regular File":
    #file_data_buffer = extfs.
    for db in datablock:
      data += extfs.getDataBlock(sys.argv[1], long(sys.argv[2]), \
        db, emd.superblock.blockSize)
    mime_type = magic.from_buffer(data)
    sys.stdout.write(mime_type)
    #sys.stdout.write(extfs.getDataBlock(sys.argv[1], long(sys.argv[2]), \
      #db, emd.superblock.blockSize)) 


if __name__ == "__main__":
   main()