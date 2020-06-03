# Data prediction and plotting

The objective for this topic is to predict the third-semester pointers on the basis of the first and second-semester pointers values. And to create a method which can predict the near future data (one or two values) to its possible amount of accuracy by using the minimal amount of data.

## What’s In This Document
- [Setup Instructions](#setup-instructions)
- [Getting Started](#getting-started)
- [Create an .exe file](#create-an-.exe-file)
- [License](#license)


## Setup Instructions

The python modules/libraries required to run this code on **Windows Machine**:

```bash
$ pip install xlrd
$ pip install collections
$ pip install plotly
```

Or Install Plotly in Virtual Environment by the following instructions<br />

**Create your virtualenv**
```bash
$ mkdir ~/.virtualenvs
$ cd ~/.virtualenvs
$ python -m venv plotly3.3
```
**Activate the virtualenv**
```bash
$ source ~/.virtualenvs/plotly2.7/bin/activate
(plotly2.7) $
```
**Install plotly locally to virtualenv**
```bash
(plotly2.7) $ pip install plotly==3.3
```
**Deactivate to exit**
```bash
(plotly2.7) $ deactivate
$ 
```

## Getting Started

```bash
$ git clone https://github.com/Dhyeythumar/Data-prediction-and-plotting.git
$ cd data_prediction&plotting
$ python data_prediction.py
```
The project is running :smiley: <br />

## Create an .exe file

To create a build file you need to install cx_Freeze. <br />

**Install cx_Freeze**
```bash
$ pip install cx_Freeze
```
**Create build file**
```bash
$ cd data_prediction&plotting
$ python setup.py build
```
Successfully created a build file :package:

## License

This project is licensed under the GNU GPLv3 - see the [LICENSE](/LICENSE) file for details.<br />
<br/>
- To see the [More Details](/data_prediction&plotting/README.md) on project.
