import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt

image_url = "https://upload.wikimedia.org/wikipedia/en/2/2a/Yoasobi_banner.jpg"
image = imageio.imread(image_url)

if image.ndim == 3:
    gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
else:
    gray = image

def roberts_operator(img):
    roberts_x = img[:-1, :-1] - img[1:, 1:]
    roberts_y = img[:-1, 1:] - img[1:, :-1]
    edge_mag = np.sqrt(roberts_x**2 + roberts_y**2)
    return (edge_mag / edge_mag.max() * 255).astype(np.uint8)

roberts_edges = roberts_operator(gray)

def sobel_operator(img):
    Gx = np.array([[-1, 0, 1], 
                   [-2, 0, 2], 
                   [-1, 0, 1]])
    
    Gy = np.array([[-1, -2, -1], 
                   [0, 0, 0], 
                   [1, 2, 1]])
    
    rows, cols = img.shape
    sobel_x = np.zeros_like(img, dtype=np.float32)
    sobel_y = np.zeros_like(img, dtype=np.float32)
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            window = img[i-1:i+2, j-1:j+2]
            sobel_x[i,j] = np.sum(Gx * window)
            sobel_y[i,j] = np.sum(Gy * window)
    
    edge_mag = np.sqrt(sobel_x**2 + sobel_y**2)
    return (edge_mag / edge_mag.max() * 255).astype(np.uint8)

sobel_edges = sobel_operator(gray)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(roberts_edges, cmap='gray')
plt.title('Roberts Edge Detection')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')

plt.tight_layout()
plt.show()
