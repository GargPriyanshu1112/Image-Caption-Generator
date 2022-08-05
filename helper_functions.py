def load_doc(filepath, mode):
    # Open the file as read only
    file = open(filepath, mode)
    # Read the file
    content = file.read()
    # Close the file
    file.close()
    
    return content




def get_all_captions(filepath):
    all_captions = [] 
    
    # Read the contents of the file
    content = load_doc(filepath, 'r')
    
    content = content.split('\n')
    
    for line in content:
        img_name, img_caption = line.split('\t')
        all_captions.append(img_caption)
    
    return all_captions     




import random
import matplotlib.pyplot as plt
import os
IMAGES_DIR = os.path.join("Data", "images")


def get_sample(mappings):
    # Get random image and its captions
    image_name, captions_list = random.choice(list(mappings.items()))

    # Display the image and its captions
    print(f"\nIMAGE:   {image_name}")
    image_path = os.path.join(IMAGES_DIR, image_name)
    image = plt.imread(image_path)
    plt.imshow(image)
    plt.axis(False)
    plt.show()
    
    print(f"\nCAPTIONS:\n")
    for idx, caption in enumerate(captions_list):
        print(f"{idx+1}.  {caption}")

        