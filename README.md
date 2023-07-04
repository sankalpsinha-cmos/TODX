# TODX: Train your Own Detector toolboX

## Introduction
TODX is a no-code image classification and object detection framework. It is built on **PyTorch Lightning** a lightweight wrapper for PyTorch.

## System Architecture
![Alt Text](./assets/architecture_diagram.png)


## Supported Models
Out of the box the framework supports the following models.

#### Classification models
| Model   | Status      |
|---------|-------------|
|  LeNet  | in progress, not yet supported |


#### Object Detection models
| Model   | Status      |
|---------|-------------|
| YOLO-v1 | in progress, not yet supported |



## Supported Datasets
Out of the box the framework supports the following datasets.

#### Classification Datasets
| Dataset | Status      |
|---------|-------------|
|  MNIST  | in progress, not yet supported |


#### Object Detection Datasets
| Dataset | Status      |
|---------|-------------|
| PASCAL-VOC | in progress, not yet supported |


## Roadmap
1. Build the image classification pipeline, with support for LeNet and MNIST.
2. Build the object detection pipeline, with support for YoLo and Pascal-VOC.
3. Build the monitoring dashboard for training.
4. Build support for user accounts.
5. Build the inference pipeline for image classification, where the user can upload an image and use a model he/she trained previously to inference on the image.
6. Build the inference pipeline for object detection, where the user can upload an image and use a model he/she trained previously to inference on the image.
7. Build a labeller, where users can make custom datasets.
8. Deploy on cloud (to be determined)

## License
The use of TODX is limited to <span style="color:red">academic purposes only, and any commercial use is explicitly forbidden.</span>.
