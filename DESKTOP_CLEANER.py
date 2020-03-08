import os
import shutil
import datetime


def desktop_path():

    '''identifies the users desktop path. If unavailable, the program exits.'''

    #  User's home directory path.
    users_directory_path = os.environ.get('HOME')
    desktop_directory_path = None

    #  finds desktop directory. If unavailable, program exits.
    try:
        if 'Desktop' in os.listdir(users_directory_path):
            desktop_directory_path = (os.path.join(users_directory_path, 'desktop'))
            os.chdir(desktop_directory_path)

            print("F O U N D   D E S K T O P   D I R E C T O R Y \n"
                    "// moved to the DESKTOP directory")

            #  confirming to user desktop path
            print(f'current working directorys is: {os.getcwd()}')

    #  if desktop path unavailable, program exits.
    except:
        return exit('could not find desktop path in the folder.')

    #  returns the desktop directory path.
    print('-' * 40)
    return desktop_directory_path


def desktop_images (desktop_directory_path):

    ''' Identifies the desktop images. '''

    print('> > D E S K T O P   I M A G E S')

    # list of files on the desktop will be inserted into array.
    desktop_images_list = []

    # file extensions that will be moves and cycled through in for loop.
    file_extension_for_moving = ['.jpg','.jpeg', '.gif', '.png']

    # iterating through every file that is on the desktop.
    for files in os.listdir(os.getcwd()):

        # iterating through the file extensions list [.e.,g jpg, gif, jpeg etc
        for file_extension in file_extension_for_moving:

            # if the file extension (e.g., .jpg') is in the FILE string, execute this code
            if file_extension in files:

                # displaying the file extension and its corresponding file
                print(f'ext: {file_extension}  //  file:  {files}') # printing out the file

                # added the file which should have one of the file extensions in the file_extensions_for_moving
                desktop_images_list.append(files)

    print(f'> > The total amount of desktop images to be moved:  [{len(desktop_images_list)}]')
    print("-" * 40)

    return desktop_images_list


def creating_desktop_directory(desktop_directory_path):

    '''creating the desktop directory. If directory already exists, user chooses another'''

    # create a new directory on the desktop
    while True:
        choose_directory_name = input('Choose a desktop folder name not already in use: ')

        #  if the user input directory name does not exist on desktop, create the directory.
        try:
            directory_on_desktop = os.path.join(desktop_directory_path, choose_directory_name)
            os.mkdir(directory_on_desktop)
            print(f" created desktop directory >> [ {choose_directory_name} ]")
            break

        #  if desktop name already exists, ask user for another directory name.
        except:
            print('-' * 40)
            print('> > C U R R E N T  D E S K T O P  D I R E C T O R I E S')

            # show the persons folders on the desktop.
            desktop_directory = (os.listdir(desktop_directory_path))
            for directory in desktop_directory:
                if os.path.isdir(directory):
                    print(f'_/ {directory}')
            print()
            print(f"Desktop F O L D E R [{choose_directory_name}] already exists."
                  f" Please choose another folder name . .")
    print("-" * 40)

    return directory_on_desktop


def moving_files_into_desktop_directory():

    '''moves the files with the extension found in variable file_extension_for_moving
       into the desktop the user created.'''

    for x in desktop_images_list:
        user_image_list_on_desktop = desktop_directory_path + '/' + x


        shutil.move(user_image_list_on_desktop, directory_on_desktop)


def document_inside_of_new_folder ():

    ''' creates a NEW text document inside the NEW desktop directory
        [1] - Inserts date and time (seconds ommited).
        [2] - Thanks user for program use. '''

    #  create a new file inside of the new desktop directory containing images
    with open(directory_on_desktop + '/READ_ME.txt', 'w') as read_me:
        time_and_date = datetime.datetime.now()
        now = time_and_date.strftime("I N I T I A T E D:  %A %B %Y @ %H:%M")
        read_me.write(now)
        read_me.write(("\nThank you for using D E S K T O P  I M A G E  C L E A N E R \n"
                       "the files were moved successfully."))


if __name__ == '__main__':
    desktop_directory_path = desktop_path()
    desktop_images_list = desktop_images(desktop_directory_path)
    directory_on_desktop = creating_desktop_directory(desktop_directory_path)
    moving_files_into_desktop_directory()
    document_inside_of_new_folder()
