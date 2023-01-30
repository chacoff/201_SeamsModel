import os
import shutil
import glob


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


def find_and_move(base, file, target):
    file_noextension = file.split('.')[0]
    result = glob.glob(f'{base}/**/{file_noextension}.bmp', recursive=True)  # a list, i take the first element
    final_target = f'{target}\\{file_noextension}.bmp'
    shutil.move(result[0], final_target)
    print(f'moved: {file_noextension}.bmp')


# list_files('C:\\Coding\\201_SeamsModel\\images')

base = 'C:\\Users\\gomezja\\PycharmProjects\\Tmb\\00_JG-SB_Validation01_2022_02_11-28'
target = 'C:\\Users\\gomezja\\PycharmProjects\\201_SeamsModel\\images\\valid\\Seams'

file1 = open('images\\valid_seams.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    l = format(line.strip())
    find_and_move(base, l, target)

