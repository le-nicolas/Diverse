import numpy as np
from skimage import data, color, segmentation as seg
from skimage.util import img_as_float
from skimage.measure import regionprops
from scipy import sparse
from matplotlib import pyplot as plt
from PIL import Image
from skimage import io

def build_rag(labels, image):
    regions = regionprops(labels, intensity_image=image)
    num_labels = labels.max() + 1
    rag = sparse.lil_matrix((num_labels, num_labels), dtype=bool)
    
    # Calculate mean color of each region
    mean_colors = np.zeros((num_labels, image.shape[-1]))
    for region in regions:
        mean_colors[region.label] = np.mean(image[region.coords[:, 0], region.coords[:, 1]], axis=0)
        
    # Iterate through each pixel's neighbors and update RAG
    for y in range(labels.shape[0]):
        for x in range(labels.shape[1]):
            current_label = labels[y, x]
            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < labels.shape[1] and 0 <= ny < labels.shape[0]:
                    neighbor_label = labels[ny, nx]
                    if current_label != neighbor_label:
                        rag[current_label, neighbor_label] = True
                        rag[neighbor_label, current_label] = True
                        
    return rag, mean_colors

def rag_segmentation(labels, rag, mean_colors):
    new_labels = np.zeros_like(labels)
    for y in range(labels.shape[0]):
        for x in range(labels.shape[1]):
            current_label = labels[y, x]
            neighbors = labels[max(0, y - 1):min(labels.shape[0], y + 2),
                               max(0, x - 1):min(labels.shape[1], x + 2)]
            neighbor_labels = np.unique(neighbors)
            neighbor_labels = neighbor_labels[neighbor_labels != current_label]
            if len(neighbor_labels) > 0:
                similarity_scores = [np.linalg.norm(mean_colors[current_label] - mean_colors[n]) for n in neighbor_labels]
                new_labels[y, x] = neighbor_labels[np.argmin(similarity_scores)]
            else:
                new_labels[y, x] = current_label
                
    return new_labels

path = r'C:\Users\User\DE\cat.jpg'  # Using raw string literal
img = img_as_float(io.imread(path))

labels1 = seg.slic(img, compactness=50, n_segments=5000, start_label=1)
out1 = color.label2rgb(labels1, img, kind='avg', bg_label=0)
out1 = Image.fromarray((out1 * 255).astype(np.uint8), 'RGB')
out1.save(r'C:\Users\User\DE\output1.jpg')  # Using raw string literal

rag, mean_colors = build_rag(labels1, img)
labels2 = rag_segmentation(labels1, rag, mean_colors)
out2 = color.label2rgb(labels2, img, kind='avg', bg_label=0)
out2 = Image.fromarray((out2 * 255).astype(np.uint8), 'RGB')
out2.save(r'C:\Users\User\DE\output2.jpg')  # Using raw string literal

fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(6, 8))
ax[0].imshow(out1)
ax[1].imshow(out2)
for a in ax:
    a.axis('off')
plt.tight_layout()
plt.show()
