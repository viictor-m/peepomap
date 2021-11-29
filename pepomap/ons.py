"""ONS CMAP."""

from matplotlib.colors import LinearSegmentedColormap


_colors = [
    [1.0, 1.0, 1.0],
    [0.8823529411764706, 1.0, 1.0],
    [0.7058823529411765, 0.9411764705882353, 0.9803921568627451],
    [0.5882352941176471, 0.8235294117647058, 0.9803921568627451],
    [0.1568627450980392, 0.5098039215686274, 0.9411764705882353],
    [0.0784313725490196, 0.39215686274509803, 0.8235294117647058],
    [0.403921568627451, 0.996078431372549, 0.5215686274509804],
    [0.09411764705882353, 0.8431372549019608, 0.023529411764705882],
    [0.11764705882352941, 0.7058823529411765, 0.11764705882352941],
    [1.0, 0.9098039215686274, 0.47058823529411764],
    [1.0, 0.7529411764705882, 0.23529411764705882],
    [1.0, 0.3764705882352941, 0.0],
    [0.8823529411764706, 0.0784313725490196, 0.0],
    [0.984313725490196, 0.3686274509803922, 0.4196078431372549],
    [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],
]

cmap = LinearSegmentedColormap.from_list("ons", _colors)
cmap_r = LinearSegmentedColormap.from_list("ons", _colors[::-1])