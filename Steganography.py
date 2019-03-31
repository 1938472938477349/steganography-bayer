import numpy
import cv2

class Steganography():

    @staticmethod
    def RGB2BayerBG(img):
        """
        Convert image to bayer BG pattern
        :param img:
        :return:
        """
        blank_image = numpy.zeros((img.shape[0], img.shape[1], 1), numpy.uint8)
        blank_image = img[:,:,1] # green
        blank_image[0::2, 0::2] = img[0::2, 0::2, 0] # red
        blank_image[1::2, 1::2] = img[1::2, 1::2, 2] # blue
        return blank_image

    @staticmethod
    def weightedRGB(img1, img2, img3, w1=1, w2=1, w3=1):
        """
        construct an image from r channel of img1, g of img2 and b of img3 with respective weight
        :param img1: First image
        :param img2: Second image
        :param img3: Third image
        :param w1: Weight for first image
        :param w2: Weight for second image
        :param w3: Weight for third image
        :return: Image in RGB
        """
        im1 = Steganography.RGB2BayerBG(img1)
        im2 = Steganography.RGB2BayerBG(img2)
        im3 = Steganography.RGB2BayerBG(img3)


        h = max(im1.shape[0],im2.shape[0],im3.shape[0])
        w = max(im1.shape[1], im2.shape[1], im3.shape[1])
        blank_image = numpy.zeros((h, w, 3), numpy.uint8)

        for i in range(0, h):
            for j in range(0, w):
                if i < im1.shape[0] and j < im1.shape[1]:
                    blank_image[i,j,0] =im1[i,j]* w1
                if i < im2.shape[0] and j < im2.shape[1]:
                    blank_image[i,j,1] =im2[i,j]* w2
                if i < im3.shape[0] and j < im3.shape[1]:
                    blank_image[i,j,2] =im3[i,j]* w3
        return blank_image


    @staticmethod
    def re_weightedRGB(img):
        """
        reconstruct 3 images from a RGB merged image
        :param img: Stego image
        :return: 3 images with 1 channel respectively
        """
        img_1 = img[:, :, 0]
        img_2 = img[:, :, 1]
        img_3 = img[:, :, 2]
        return cv2.cvtColor(img_1, cv2.COLOR_BAYER_BG2BGR),cv2.cvtColor(img_2, cv2.COLOR_BAYER_BG2BGR),cv2.cvtColor(img_3, cv2.COLOR_BAYER_BG2BGR)




# im1 = cv2.imread("images/results/stegoImage_bayer.png", cv2.IMREAD_UNCHANGED)
# im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
# k,l,m = Steganography.re_weightedRGB(im1)
#
# cv2.imwrite("images/results/recovered_a_bayer.png", k)
# cv2.imwrite("images/results/recovered_b_bayer.png", l)
# cv2.imwrite("images/results/recovered_c_bayer.png", m)
# cv2.imshow('image', k)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


im1 = cv2.imread("images/weightedRGB/input/a.jpg", cv2.IMREAD_UNCHANGED)
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)

im2 = cv2.imread("images/weightedRGB/input/b.jpg", cv2.IMREAD_UNCHANGED)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)

im3 = cv2.imread("images/weightedRGB/input/c.jpg", cv2.IMREAD_UNCHANGED)
im3 = cv2.cvtColor(im3, cv2.COLOR_BGR2RGB)


k = Steganography.weightedRGB(im1, im2, im3, 0.1, 0.1, 1)

k = cv2.cvtColor(k, cv2.COLOR_RGB2BGR)

cv2.imwrite("images/weightedRGB/results/stegoImage_bayer_weighted.png", k)
cv2.imshow('image', k)
cv2.waitKey(0)
cv2.destroyAllWindows()