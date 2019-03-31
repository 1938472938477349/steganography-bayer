import numpy
import cv2

class Steganography():

    @staticmethod
    def weightedRGB(img1, img2, img3, w1=0.1, w2=0.1, w3=1):
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
        h = max(img1.shape[0],img2.shape[0],img3.shape[0])
        w = max(img1.shape[1], img2.shape[1], img3.shape[1])
        blank_image = numpy.zeros((h, w, 3), numpy.uint8)
        for i in range(0, h):
            for j in range(0, w):
                if i < img1.shape[0] and j < img1.shape[1]:
                    blank_image[i,j,0] =img1[i,j,0]* w1
                if i < img2.shape[0] and j < img2.shape[1]:
                    blank_image[i,j,1] =img2[i,j,1]* w2
                if i < img3.shape[0] and j < img3.shape[1]:
                    blank_image[i,j,2] =img3[i,j,2]* w3
        return blank_image


    @staticmethod
    def re_weightedRGB(img):
        """

        :param img:
        :return:
        """
        h = img.shape[0]
        w= img.shape[1]
        #img1 = numpy.zeros((h, w, 1), numpy.uint8)
        #img2 = numpy.zeros((h, w, 1), numpy.uint8)
        #img3 = numpy.zeros((h, w, 1), numpy.uint8)
        img_1 = img[:, :, 0]
        img_2 = img[:, :, 1]
        img_3 = img[:, :, 2]

        return img_1,img_2,img_3


im1 = cv2.imread("images/results/1.png", cv2.IMREAD_UNCHANGED)
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
k,l,m = Steganography.re_weightedRGB(im1)

cv2.imwrite("images/results/3.png", k)
cv2.imwrite("images/results/4.png", l)
cv2.imwrite("images/results/5.png", m)
cv2.imshow('image', k)
cv2.waitKey(0)
cv2.destroyAllWindows()


# im1 = cv2.imread("images/a.jpg", cv2.IMREAD_UNCHANGED)
# im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
#
# im2 = cv2.imread("images/b.jpg", cv2.IMREAD_UNCHANGED)
# im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
#
# im3 = cv2.imread("images/c.jpg", cv2.IMREAD_UNCHANGED)
# im3 = cv2.cvtColor(im3, cv2.COLOR_BGR2RGB)
#
#
# k = Steganography.weightedRGB(im1, im2, im3)
#
# k = cv2.cvtColor(k, cv2.COLOR_RGB2BGR)
#
# cv2.imwrite("images/results/2.png", k)
# cv2.imshow('image', k)
# cv2.waitKey(0)
# cv2.destroyAllWindows()