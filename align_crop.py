import cv2
import numpy as np
import sys
def align(images):
    ratios = []
    for image in images:
        shape = image.shape
        ratios.append(shape[0]/shape[1])

    print(ratios)
    target_ratio = np.mean(ratios)
    crop_images = []
    for i in range(0,len(ratios)):
        image = images[i]
        shape = image.shape
        if ratios[i]>target_ratio:
            height = int(shape[1]*target_ratio)
            t = (shape[0] - height)//2
            b = t+height
            crop_images.append(image[t:b,:,:])

        else:
            width = int(shape[0]/target_ratio)
            l = (shape[1]-width)//2
            r = l+width
            crop_images.append(image[:,l:r,:])
      
    return crop_images
 
 

def main():
    images=[]
    for image_name in sys.argv[1:]:
        images.append(cv2.imread(image_name))
    crop_images = align(images)
    for i in range(len(crop_images)):
        name = sys.argv[i+1]
        name = '.'.join(name.split('.')[:-1])+'_crop.png'
        print(name)
        cv2.imwrite(name,crop_images[i])

if __name__ == '__main__':
    main()
