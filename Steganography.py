import numpy
import cv2

class Steganography():

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

im1 = cv2.imread("images/a.jpg", cv2.IMREAD_UNCHANGED)
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)

im2 = cv2.imread("images/b.jpg", cv2.IMREAD_UNCHANGED)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)

im3 = cv2.imread("images/c.jpg", cv2.IMREAD_UNCHANGED)
im3 = cv2.cvtColor(im3, cv2.COLOR_BGR2RGB)

k = Steganography.weightedRGB(im1, im2, im3)

k = cv2.cvtColor(k, cv2.COLOR_RGB2BGR)

cv2.imwrite("images/results/1.png", k)
cv2.imshow('image', k)
cv2.waitKey(0)
cv2.destroyAllWindows()