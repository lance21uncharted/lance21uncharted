# import os
# import shutil
# import pathlib

# main_file="sloot.py"
# #directory paths
# source="D:/MANCYMORE"

# audio_folder="D:/MANCYMORE/audio"

# images_folder="D:/MANCYMORE/images"

# programming_folder="D:/MANCYMORE/programming"

# text_folder="D:/MANCYMORE/text"

# video_folder="D:/MANCYMORE/video"

# files = os.listdir(source)

# #file formats list
# audio_file_formats=['mp3','wav']
# doc_file_formats=['doc','docx']
# text_file_formats=['txt', 'csv']
# video_file_formates=['mp4','mkv']
# programming_file_formats=['py','js','css', 'html']

# for file in files:
#     get_file_index=files.index(main_file)
#     del files[get_file_index]
#     file_ext= file.split('.')[-1]

#     if file_ext in audio_file_formats:
#         shutil.move(file,audio_folder)

#     if file_ext in doc_file_formats:
#         shutil.move(file,text_folder)

#     if file_ext in text_file_formats:
#         shutil.move(file,text_folder)

#     if file_ext in video_file_formates:
#         shutil.move(file,video_folder)

#     if file_ext in programming_file_formats:
#         shutil.move(file,programming_folder)


import pathlib as p
import os

Path = ""
files = None
ext = set()
path1 = "D:/MANCYMORE/sloot.py"
basename = os.path.basename(path1)


def GetExtintions():
    for i in files:
        ext.add(i.suffix.replace(".", ""))


def CreateFolder():
    for i in ext:

        try:
            os.mkdir(str(Path / i))
        except:
            pass


def MoveFiles():
    for i in files:

        if i.is_file():
            print(Path / i.suffix.replace(".", "") / i.name)
        os.rename(str(i), Path / i.suffix.replace(".", "") / i.name)


def main():
    global files, Path
    Path = p.Path(input("Enter Path: "))
    files = list(Path.glob("*"))

    GetExtintions()
    CreateFolder()
    MoveFiles()


if __name__ == "__main__":
    main()
