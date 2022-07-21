import os
import zipfile as zp


def backup(folder):
    folder = os.path.abspath(folder)
    print(f'folder = {folder}')
    offset = 1
    while offset < 2:
        zip_name = os.path.basename(folder) + '_' + str(offset) + '.zip'
        print(f'Given zip file name: {zip_name}')

        # checking if the backup zip file already exists
        if os.path.exists(zip_name):
            print(f'os.path for the zip_name {zip_name} already exists. So break.')
            offset = 2
            break

        print('Since the backup zip file does not exists, successfully created file %s' % zip_name)
        # creating a backup zip file.
        backup_zip = zp.ZipFile(zip_name, 'w')
        # adding all the folders and subfolders to the zip file.
        for folder_name, subfolders, filenames in os.walk(folder):
            backup_zip.write(folder_name)
        backup_zip.close()
        print("done")


backup('Fractal Sessions')
