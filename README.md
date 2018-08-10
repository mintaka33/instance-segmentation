# instance-segmentation
deep learning based instance segmentation sample application

## reference

https://github.com/matterport/Mask_RCNN

https://github.com/Eclipsess/Mask-Rcnn-openCV

https://github.com/waleedka/coco


## set python virtual env
```bash
sudo apt update && sudo apt upgrade

sudo apt install python3-tk
sudo apt install python3-pip

sudo pip3 install virtualenv

mkdir ~/.virtualenvs
cd ~/.virtualenvs

virtualenv --no-site-packages envseg
source envseg/bin/activate

```

## install python packages
```bash
cd mask_rcnn_sample
pip3 install -r requirements.txt
```

## how to run
```bash
cd mask_rcnn_sample
source ~/.virtualenvs/envseg/bin/activate
python demo.py
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

## result
![image](https://github.com/mintaka33/instance-segmentation/blob/master/mask_rcnn_sample/result/mask.jpg)
