# byaar
bypass file-type attachment restrictions of GMail

## Why?

GMail does not allows certain file-types as attachments (e.x. .zip, .bz etc.)

This tool removes that restriction.

## How?
attachments --archive-the-attachments--> attachments.zip --replace-ZIP-signature-with-X--> temp_file --change-filename-to-cats.jpeg--> cats.jpeg

>ZIP signature is special 8 bytes of data(0x4b50) which identifies a file as ZIP.
>
>X is random data. it is stored as first 8 bytes of cats.jpeg

cats.jpeg --change-X-to-ZIP-signature--> temp_file --extract-temp_file-to-cats-folder--> cats folder with attachments

## Usage
```
python3 byaar.py [OPTION]... [FILE]...

Mandatory arguments:

    -c    --conceal    conceal files provided in cats.jpeg file
    
    -r    --reveal     reveal the cats.jpeg file to cats folder
    
Exit status:

     0    if OK,
     
     1    if bad/invalid command-line arguments given.
```
