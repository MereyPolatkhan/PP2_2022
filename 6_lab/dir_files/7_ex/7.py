import os
import shutil

with open('content_1.txt', 'w') as f1:
    f1.writelines(['our\n', 'Assistant_PP_2\n', 'Bagdauletova_Danara_is_TOP'])

shutil.copyfile('content_1.txt', 'copied_data.txt')