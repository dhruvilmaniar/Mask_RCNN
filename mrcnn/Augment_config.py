

import imgaug.augmenters as iaa


AUGMENTATIONS = iaa.Sequential([

    iaa.LinearContrast((0.75, 1.75)),
    iaa.CropAndPad(percent=(-0.25, 0.25)),
    
    
    iaa.Sometimes(
        0.6,
        iaa.Fliplr(0.5),
        iaa.Flipud(0.5),
    ),

    iaa.Sometimes(
        0.3,
        iaa.Multiply((0.6, 1.4)),
    ),

    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        translate_percent={"x": (-0.3, 0.5), "y": (-0.4, 0.5)},
        rotate=(-65, 65),
        shear=(-8, 8)        
    )

], random_order=True)