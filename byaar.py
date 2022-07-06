from sys import argv
from zipfile import ZIP_DEFLATED, ZipFile
from os import remove
from random import randbytes

ZIP_SIGNATURE = "PK"

CONCEALED_FILE = "./cats.jpeg"
CONCEALED_FILE_TEMP = f".{CONCEALED_FILE}.tmp"
CONCEALED_KEY = randbytes(8)

REVEALED_FOLDER = "./cats"
REVEALED_FILE_TEMP = f".{REVEALED_FOLDER}.tmp"

def main():
    f"""\
Usage: python3 byaar.py [OPTION] [FILE]...

Mandatory arguments:
    -c    --conceal    conceal files provided in {CONCEALED_FILE} file
    -r    --reveal     reveal the {CONCEALED_FILE} file to {REVEALED_FOLDER}
    
Exit status:
     0    if OK,
     1    if minor problems (e.g., cannot access file-paths),
     2    if serious trouble (e.g., cannot acceess command-line argument).
"""
    
    # validate argument
    try:
        if argv[1] in ("-c", "--conceal", "-r", "--reveal"):
            pass
    except IndexError:
        # bad command-line arguments found
        print(main.__doc__)
        return 2;

    # if -c or --conceal argument found
    # call conceal function
    # with files provided(from 2nd argument onwards) as arguments
    if (argv[1] in ("-c", "--conceal")):
        conceal(argv[2:])

    # if -r or --reveal argument found
    # call reveal function
    # with files provided(from 2nd argument onwards) as arguments
    if argv[1] in ("-r", "--reveal"):
        reveal(argv[2:])

def reveal(con_files):
    # we only conceal files in .zip file-type
    # with zip signature(b"PK") replaced with CONCEALED_KEY
    
    # lets put back the zip signature(b"PK")
    # in place of our CONCEALED_KEY,
    # to create a REVEALED_FILE of zip type
    for con_file in con_files:
        with open(con_file, "rb") as my_con_file:
            # first 8 bytes are CONCEALED_KEY
            CONCEALED_KEY = my_con_file.read(8)

            with open(REVEALED_FILE_TEMP, "wb") as my_zip_file:
                while (marker := my_con_file.read(2)):
                    if marker == CONCEALED_KEY:
                        my_zip_file.write(bytes(ZIP_SIGNATURE))
                    else:
                        my_zip_file.write(marker)
    
    # let's unzip this zip file to give back original files
    with ZipFile(REVEALED_FILE_TEMP, 'r') as my_zip_file:
        my_zip_file.extractall(REVEALED_FOLDER)
    
    remove(REVEALED_FILE_TEMP)

def conceal(og_files):
    # GMail blocks a lot of file types, including .zip file
    # make every other file-type a .zip file-type

    # zipping every file in the CONCEALED_FILE.tmp
    for og_file in og_files:
        with ZipFile(
            CONCEALED_FILE_TEMP,
            'a',
            compression=ZIP_DEFLATED,
            compresslevel=5) as my_zip:
            my_zip.write(og_file)
    
    # now let's make this zip file not a zip file
    #
    # according to:
    #   https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
    #
    #   At section- 4.2 ZIP Metadata
    #       zip signature values begin with
    #           the two byte constant marker of 0x4b50,
    #           representing the characters "PK"
    # 
    # removing this signature makes a zip file not a zip file
    # lets do exactly the same

    with open(CONCEALED_FILE_TEMP, "rb") as my_binary_tmp:
        with open(CONCEALED_FILE, 'wb') as my_binary:
            # lets put our 8 bytes CONCEALED_KEY at begining of the file
            # this way we can read first 8 bytes to get CONCEALED_KEY
            # when reconstructing the zip
            my_binary.write(CONCEALED_KEY)
            while (marker := my_binary_tmp.read(2)):
                if marker == ZIP_SIGNATURE:
                    my_binary.write(bytes(CONCEALED_KEY))
                else:
                    my_binary.write(marker)
    
    remove(CONCEALED_FILE_TEMP)

if __name__ == "__main__":
    main()
