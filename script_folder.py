## To rename the folders
import os

for name in os.listdir('.'):
    if os.path.isdir(os.path.join('.', name)):
        if 'problem' in name:
            new = name.split('_')[0] + '_' + name.split('_')[-1].zfill(3)
            os.rename(os.path.join('.', name), os.path.join('.', new))