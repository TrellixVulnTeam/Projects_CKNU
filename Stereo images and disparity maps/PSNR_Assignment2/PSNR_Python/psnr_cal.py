from PIL import Image
import numpy
import math

home_dir = "C:/Users/User/Documents/Cityu files/Year 3/Sem B/CS4186 Computer Vision and Image Processing/Assignments/Assignment2/"

def psnr(img1, img2):
    mse = numpy.mean( ((img1 - img2)) ** 2 )
    if mse == 0:
        return 'INF'
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def test():
    test_imgs = ["Art", "Dolls", "Reindeer"]    
    
    for index in range(3):
        gt_names = home_dir + "PSNR_Assignment2/PSNR_Python/gt/"+test_imgs[index]+"/disp1.png";
        gt_img = numpy.array(Image.open(gt_names),dtype=float);
       
        
        pred_names = home_dir + "PSNR_Assignment2/PSNR_Python/pred/" +test_imgs[index]+"/disp1.png";
        pred_img = numpy.array(Image.open(pred_names),dtype=float);
        
# When calculate the PSNR:
# 1.) The pixels in ground-truth disparity map with '0' value will be neglected.
# 2.) The left part region (1-250 columns) of view1 is not included as there is no
#   corresponding pixels in the view5.
        [h,l] = gt_img.shape
        gt_img = gt_img[:, 250:l]
        pred_img = pred_img[:, 250:l]
        pred_img[gt_img==0]= 0
    
        peaksnr = psnr(pred_img,gt_img);
        print('The Peak-SNR value is %0.4f \n' % (peaksnr));



if __name__== '__main__':
    test()   