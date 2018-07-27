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

## notes

### set python virtual env config in VSCode for debug

1. open vscode "Settings", set below virtual env config
```
"python.venvPath": "~/.virtualenvs",
    "python.venvFolders": [
        "envseg"
    ],
"python.pythonPath": "~/.virtualenvs/envseg/bin/python"
}
```
2. reopen vscode, press "F1" or "Ctrl+Shift+P", find "Python: Select Interpreter" and select a python environment

3. in "launch.json", config python path in below
```
"pythonPath": "${config:python.pythonPath}"
```