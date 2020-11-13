import cv2
import sys
import numpy as np


def anonymize(source, destination, visualize=False, thickness=-1, output_dims=(800, 800, 3), num_circles=(20,20), ):
    """
    Anonymize an image.

    Args:
        source ([type]): [description]
        destination ([type]): [description]
        visualize (bool, optional): [description]. Defaults to False.
        thickness (int, optional): [description]. Defaults to -1.
        output_dims (tuple, optional): [description]. Defaults to (800, 800, 3).
        num_circles (tuple, optional): [description]. Defaults to (20,20).
    """    

    im = cv2.imread(source)
    height, width, _ = im.shape

    x_samples_source = np.linspace(0, width-1, num_circles[0]).astype(int)
    y_samples_source = np.linspace(0, height-1, num_circles[1]).astype(int)    

    radius = int(min(output_dims[0] / num_circles[0] / 2, output_dims[1] / num_circles[1] / 2))
    canvas = np.ones(output_dims, np.uint8) * 255

    x_samples_canvas = np.linspace(radius, output_dims[0]-1-radius, num_circles[0]).astype(int)
    y_samples_canvas = np.linspace(radius, output_dims[1]-1-radius, num_circles[1]).astype(int)

    colors = [im[y,x].tolist() for x in x_samples_source for y in y_samples_source]
    positions = [(x, y) for x in x_samples_canvas for y in y_samples_canvas]
    for i in range(len(positions)):
        cv2.circle(canvas, positions[i], radius, colors[i], thickness)

    cv2.imwrite(destination, canvas)

    if visualize:
        cv2.imshow("preview", canvas)
        cv2.waitKey(0)



if __name__ == "__main__":
    args = sys.argv[1:]

    assert 1 <= len(args) <= 2 
    args = sys.argv[1:]

    source = args[0]
    destination = args[0] if len(args) == 1 else args[1]

    anonymize(source, destination, visualize=False, thickness=40)
