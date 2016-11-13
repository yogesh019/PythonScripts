import os
import sys

def getAbsPath(path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
          os.path.expanduser(path)
          );   ## if '~' does not work if src and dest paths are given relative then use os.path.expanduser


#recursive helper function to move files , either use recursion or bfs in scripting
def moveHelper(extension,src,dest): 
    files=os.listdir(src)
    for f in files:                      
        abspath=os.path.join(src,f)
        if os.path.isdir(abspath):
            moveHelper(extension,abspath,dest)
        else:
            file_ext=f.split('.')[-1]
            if file_ext==extension:
                os.rename(abspath,os.path.join(dest,f))


def move(extension,src,dest):
    src=getAbsPath(src)
    dest=getAbsPath(dest)
    print(src)
    print(dest)

    if not os.path.isdir(src):
        print("Invalid source directory!")
        return
    if not os.path.isdir(dest):
        print("Invalid destination directory!")
        return

    moveHelper(extension,src,dest)


if __name__=="__main__":
    if len(sys.argv)!=4:
        print("Inavalid number of arguments supplied!!")
    else:
        move(sys.argv[1],sys.argv[2],sys.argv[3])
