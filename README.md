# byaar
bypass file-type attachment restrictions of GMail

## Why?

GMail does not allows certain file-types as attachments (e.x. .zip, .bz etc.)

This tool removes that restriction.

## Usage

suppose you have to send file_1, file_2, file_3,...,file_n as attachment but their file-types are blocked.

execute
```
$ python3 byaar.py --conceal file_1 file_2 file_3...file_n
```

All files(file_1...file_n) will be concealed in a cats.jpeg file in present directory

you can send this cats.jpeg file as attachment

upon receiving your file

recipient can execute

```
$ python3 byaar.py --reveal cats.jpeg
```

All files(file_1..file_n) will be revealed/extracted in a cats folder in present directory

NOTE:

THIS IS NOT A PRIVACY TOOL.

FILES ARE NOT ENCRYPTED.

ANYONE CAN VIEW YOUR FILES IF THEY HAVE THIS TOOL OR KNOW HOW IT WORKS.


ALWAYS KEEP BACKUP OF FILES CONCEALED WITH THIS TOOL.

IT MAY CORRUPT FILES SOMETIMES.

```
python3 byaar.py [OPTION]... [FILE]...

Mandatory arguments:

    -c    --conceal    conceal files provided in cats.jpeg file
    
    -r    --reveal     reveal the cats.jpeg file to cats folder
    
Exit status:

     0    if OK,
     
     1    if bad/invalid command-line arguments given.
```

## How it works under the hood?
attachments --archive-the-attachments--> attachments.zip --replace-ZIP-signature-with-X--> temp_file --change-filename-to-cats.jpeg--> cats.jpeg

>ZIP signature is special 8 bytes of data(0x4b50) which identifies a file as ZIP.
>
>X is random data. it is stored as first 8 bytes of cats.jpeg

cats.jpeg --change-X-to-ZIP-signature--> temp_file --extract-temp_file-to-cats-folder--> cats folder with attachments
