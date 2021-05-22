

# Mask RCNN implementaiton in Tensorflow, Keras


Fork of [Matterport Mask-RCNN](https://github.com/matterport/Mask_RCNN)


---


* Removed Redundant files (README, images used in it, License etc)
* Modified requirements.txt for defaulting tf <2.0, Keras < 2.0.8
* Modified Result Splash file names
* Modified Result Splash video name, format (.avi to .mp4)
* Added provision for image augmentations in `mrcnn/Augment_config.py`



### Dataset format:
```bash
dataset
├── train
│   ├── dog_050.jpg
│   ├── ...
│   └── via_region_data.json
└── val
    ├── dog_002.jpg
    ├── ...
    └── via_region_data.json
```
`via_region_data.json` contains annotations for all images in that folder.

No need to add masks. Only Images are required, with annotations in json file.


## Usage

1. Run : 
    ```bash
    cd ~/Mask_RCNN

    pip install -r requirements.txt
    python setup.py install
    ```

2. Add images according to this folder structure. Image name/format need not be same, but the rest (folder names, json) names should be kept same, or modified in project accordingly.

3. Modify `mrcnn/Augment_config.py` according to your need. Here is the [Github](https://github.com/aleju/imgaug) repo and here's the link to [docs](https://imgaug.readthedocs.io/).
**Do not forget that there are some augmentations written in that file currently.**

4. Replace `nail` and `Nail` from below and run:
    ```bash
    %cd ~/Mask_RCNN

    !cp ~/Mask_RCNN/samples/balloon/balloon.py ./nail.py

    !sed -i -- 's/balloon/nail/g' nail.py
    !sed -i -- 's/Balloon/Nail/g' nail.py


    !sed -i -- 's/epochs=30/epochs=20/g' nail.py
    ```
    This will copy file from `samples/balloon/balloon.py` to the base dir.
    Also, it will replace balloon and Balloon with nail and Nail, or name you give.


5. Modify `layers` ['all', 'heads'], epochs, and other useful things inside `nail.py`.

6. You might also want to look at `mrcnn/config.py` which contains some important configs of the model.**Note that, many of the items are overwritten in nail.py file.**

7. Once ready, run from base dir (replace nail with your name.):
    ```bash
    #Usage: import the module (see Jupyter notebooks for examples), or run from the command line as such:

    # Train a new model starting from pre-trained COCO weights
    python3 nail.py train --dataset=dataset/ --weights=coco

    # Resume training a model that you had trained earlier
    python3 nail.py train --dataset=dataset/ --weights=last

    # Train a new model starting from ImageNet weights
    python3 nail.py train --dataset=dataset --weights=imagenet
    ```
    **Model will be saved inside /logs/nails[date]/mask_rcnn_model.h5**

    **/logs dir is in the same dir as /root.**

    Model is saved after every epoch. However, to manually save, you can use the following keras api:
      ```bash
      model_path = os.path.join(MODEL_DIR_PATH, "mask_rcnn_shapes.h5")
      model.keras_model.save_weights(model_path)
      ```


8. For Inference, run:
    ```bash
    # Apply color splash to an image
    python3 balloon.py splash --weights=/path/to/weights/file.h5 --image=<URL or path to file>

    # Apply color splash to video using the last weights you trained
    python3 balloon.py splash --weights=last --video=<URL or path to file>

    ```

    Output will be saved in the base dir. 
    **Images are stored as png, whereas videos are stored as mp4. Modify `detect_and_color_splash` function inside nail.py for other formats.**


9. For debugging:

    `inspect_data.ipynb` visualizes the different pre-processing steps to prepare the training data.

    `inspect_model.ipynb` goes in depth into the steps performed to detect and segment objects. It provides visualizations of every step of the pipeline.

    `inspect_weights.ipynb` This notebooks inspects the weights of a trained model and looks for anomalies and odd patterns.



---


* ./samples/ contains some sample project files:
    
    * `balloon` for ballon detection
    * `coco` for detection according to coco dataset
    * `nucleus` for nucleus detection inside cell.
    * `shapes` for shapes detection.

* Also see `/samples/demo.ipynb` for more help.