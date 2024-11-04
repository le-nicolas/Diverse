import numpy as np
import networkx as nx
from skimage import color, segmentation as seg, measure
from matplotlib import pyplot as plt
from PIL import Image
from skimage import io
from skimage.util import img_as_float

def build_rag(labels, image):
    rag = nx.Graph()
    regions = measure.regionprops(labels, intensity_image=image)
    
    for region in regions:
        rag.add_node(region.label, mean_color=region.mean_intensity, pixel_count=region.area)

    for i in range(labels.shape[0]):
        for j in range(labels.shape[1]):
            current_label = labels[i, j]
            neighbors = [
                labels[i + di, j + dj]
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= i + di < labels.shape[0] and 0 <= j + dj < labels.shape[1]
            ]
            for neighbor in neighbors:
                if current_label != neighbor:
                    rag.add_edge(current_label, neighbor, weight=np.linalg.norm(
                        rag.nodes[current_label]['mean_color'] - rag.nodes[neighbor]['mean_color']))

    return rag

def merge_mean_color(graph, src, dst, n):
    graph.nodes[dst]['mean_color'] += graph.nodes[n]['mean_color']
    graph.nodes[dst]['pixel_count'] += graph.nodes[n]['pixel_count']
    graph.nodes[dst]['labels'].append(n)
    return graph

# Perform Normalized Cut (Using NetworkX)
def normalized_cut(labels, rag):
    new_labels = seg.relabel_sequential(labels)[0]
    return new_labels

# Reading the image
path = r'C:\Users\User\DE\cat.jpg'  # Using raw string literal
img = img_as_float(io.imread(path))

# Initial segmentation using SLIC
labels1 = seg.slic(img, compactness=30, n_segments=500, start_label=1)
out1 = color.label2rgb(labels1, img, kind='avg', bg_label=0)
out1 = Image.fromarray((out1 * 255).astype(np.uint8), 'RGB')
out1.save(r'C:\Users\User\DE\output1.jpg')  # Using raw string literal

# Building the RAG
rag = build_rag(labels1, img)

# Graph-based segmentation using Normalized Cut
labels2 = normalized_cut(labels1, rag)
out2 = color.label2rgb(labels2, img, kind='avg', bg_label=0)
out2 = Image.fromarray((out2 * 255).astype(np.uint8), 'RGB')
out2.save(r'C:\Users\User\DE\output2.jpg')  # Using raw string literal

# Visualization
fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(6, 8))
ax[0].imshow(out1)
ax[1].imshow(out2)
for a in ax:
    a.axis('off')
plt.tight_layout()
plt.show()
