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
        <li>Cover Image: Image used to hide the code image</li>
        <li>Stego Image: Cover image with the code image embedded</li>
        </ul>
    </div>
</div>





<h2>Weighted RGB Merge</h2>

<div class="description">We can create a stego image from 3 images, by using one channel from each image. In this case each of the 3 images acts as cover image and code image at
the same time.</div>


<img src="images/a.jpg" width="150"><img src="images/b.jpg" width="150"><img src="images/c.jpg" width="150">
<br>
<img src="images/results/1.png" width="450">


<div class="description">
    This method is obviously not very smart if your goal is to hide an image within another image. You might even be able to discern the different images visually.
    Another downside is that we can only recover one channel from each image, essentially losing the color color information.
    You can somewhat make it not as obvious by adding weights to each channel of the stego image.
</div>