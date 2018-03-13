import PIL
import os.path  
import PIL.ImageDraw            

def apple(original_image):
    """ Places a frame around a PIL.Image
    Change line 37 so that use_decorative_frame is False to answer Step 10.
    original_image must be a PIL.Image
    Returns a new PIL.Image with a border, where
    0 < percent_of_side < 1
    is the border width as a portion of the shorter dimension of original_image
    """
    #sets two new variables from the values of the original image
    width, height = original_image.size
    ###
    #create a mask
    ###
    
    #start with alpha=0 mask
    apple_mask = PIL.Image.new('RGBA', (width, height), (0, 0, 0, 0))
    apple_image= PIL.Image.open(os.path.join(os.getcwd(), 'apple.png'))
    apple_image = apple_image.resize((width,height))
    apple_mask = apple_mask.paste(apple_image,(0,0),mask=apple_mask)
   
    # Make the new image, starting with all transparent
    #frame_image = PIL.Image.new('RGBA', (width, height), (r, g, b, 255))
    result = original_image.copy()
    result.paste(apple_image, (0,0), mask=apple_mask)
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

def apple_all_images(directory=None):
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
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')
        print n
        # Round the corners with radius = 30% of short side
        new_image = apple(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    