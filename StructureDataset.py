import os


def list_files(startpath):
    sourceFile = open('StructureDataset.txt', 'w')
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)), file=sourceFile)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f), file=sourceFile)
    sourceFile.close()


list_files('C:\\Coding\\201_SeamsModel\\images')