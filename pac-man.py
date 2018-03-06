import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def pac_man(original_image, color):
    """ Places a frame around a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with frame, where
    0 < frame_width < 1
    is the frame width as a portion of the shorter dimension of original_image
    """
    #set the width of the frame
    width, height = original_image.size 
    ###
    #create a mask
    ###
    
    #start with alpha=0 mask
    r, g, b = color
    pac_man_mask = PIL.Image.new('RGBA', (width, height), (255,255,0,255))
    drawing_layer = PIL.ImageDraw.Draw(pac_man_mask)
    
    #draw 4 rectangles to make the frame
    drawing_layer.pieslice((0,0,width,height),30,330,fill=(r,g,b,0))
    
    # Make the new image, starting with all transparent
    result = original_image.copy()
    result.paste(pac_man_mask, (0,0), mask=pac_man_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def pac_man_all_images(directory=None, color=(255,0,0)):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images_
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print n
        filename, filetype = file_list[n].split('.')
        
        # Round the corners with default percent of radius
        new_image = pac_man(image_list[n],color) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    