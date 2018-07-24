# instance-segmentation
deep learning based instance segmentation sample application

## reference

https://github.com/matterport/Mask_RCNN

https://github.com/Eclipsess/Mask-Rcnn-openCV

https://github.com/waleedka/coco


## set python virtual env
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip

sudo pip3 install virtualenv

mkdir $(workdir)
cd $(workdir)

virtualenv --no-site-packages envmask
source envmask/bin/activate

```

## install python packages
```bash
sudo apt install python3-tk

pip3 install Cython
pip3 install numpy scipy matplotlib
pip3 install pycocotools
pip3 install tensorflow
pip3 install scikit-image
pip3 install keras
pip3 install IPython
pip3 install opencv-python
```