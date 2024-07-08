## Installation Guide

Welcome! This repository contains the source material for the **anywidget**
tutorial to be presented at SciPy 2024. We will be using **JupyterLab** for all
tutorial materials.

### Quick Start

> [!WARNING]
> You should reinstall this just before the conference as we might have made some changes by then.

1. **Clone the Repository**:

```bash
git clone https://github.com/manzt/scipy-2024-anywidget.git
cd scipy-2024-anywidget
```


2. **Set Up Environment**:

**Using Conda**:
```bash
conda env create -f environment.yml
conda activate anywidget-tutorial
```

**Using Python Virtual Environment**:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. **Launch JupyterLab**:
```bash
jupyter lab
```
