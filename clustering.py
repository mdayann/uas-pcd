import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import imageio.v2 as imageio

image_url = "https://upload.wikimedia.org/wikipedia/en/2/2a/Yoasobi_banner.jpg"
image = imageio.imread(image_url)

pixels = image.reshape(-1, 3)

pixels_norm = pixels / 255.0

kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(pixels_norm)

segmented_pixels = kmeans.cluster_centers_[kmeans.labels_]

segmented_image = segmented_pixels.reshape(image.shape).astype(np.float32)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('K-Means Segmentation (4 clusters)')
plt.axis('off')

plt.tight_layout()
plt.show()
