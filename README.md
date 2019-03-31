<h1>Image Steganography</h1>


<div class ="discription">
    <div id="defintion_steganography">
        "Steganography [...] is the practice of concealing a file, message, image, or video within another file, message, image, or video."
        <a href="https://en.wikipedia.org/wiki/Steganography">Wikipedia</a>
    </div>
    <div id="txt">
        In this project I explore different algorithms for image steganography. The goal is to understand different types of approaches, their pros and cons and their applicative scenarios.
    </div>
    <div id="legends">
        <ul>
        <li> Code Image: Image to hide </li>
        <li> Cover Image: Image used to hide the code image</li>
        <li> Stego Image: Cover image with the code image embedded</li>
        </ul>
    </div>
</div>





<h2>Weighted RGB Merge</h2>

<div class="description">We can create a stego image from 3 images, by using one channel from each image. In this case each of the 3 images acts as cover image and code image at
the same time.</div>

Cover Images/Code Images: <br>
<img src="images/a.jpg" width="150"><img src="images/b.jpg" width="150"><img src="images/c.jpg" width="150"><br><br>

Stego Image: <br>
<img src="images/results/1.png" width="450"><br><br>

Reconstruction: <br>
<img src="images/results/3.png" width="150"><img src="images/results/4.png" width="150"><img src="images/results/5.png" width="150"><br><br>


<div class="description">
    This method is obviously not very smart if your goal is to hide an image within another image.
    <ul> 
    <li>We can discern the different images visually.</li>
    <li>We can only recover one channel from each image, essentially losing the color color information.</li>
    </ul>
    For the first problem, we can somewhat solve it by adding weights to each channel of the stego image: <br>
    <img src="images/results/2.png" width="450"><br>
    2 Images are now hidden inside the R and G channel with 0.1 as weight respectively making the stego image blue. It's hard to discern the hidden images visually, but the 
    stego image still looks odd.
    For the second problem, we can use the Bayer pattern. Instead of storing one whole channel of an image, we store multiple channel of an image at specific location, giving us
    the following grid: <br>
    <img src="images/bayer.png" width="450"><br>
    When we reconstruct an image, we just have to interpolate the missing colors.
     
</div>