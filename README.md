# byaar
bypass file-type attachment restrictions of GMail

## Why?

GMail does not allows certain file-types as attachments (e.x. .zip, .bz etc.)

This tool archives files in .zip format and removes ZIP signature(0x4b50 or "PK") from its binary data, to bypass this restriction.

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
