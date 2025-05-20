# ResNet50 Regression Image Model

这是一个基于 PyTorch 和预训练 ResNet50 模型的图像回归项目。  
模型通过图片文件名中的标签（前两位数字）进行训练，实现对标签的回归预测。

---

## 功能简介

- 从指定文件夹加载图片，图片文件名需以数字开头作为标签，如 `12_image.png`，标签为12。
- 对图片进行预处理，包括缩放、归一化。
- 使用预训练 ResNet50 修改最后一层，做回归输出（0~1之间）。
- 训练过程包含学习率调整和最佳模型保存。
- 支持 GPU 加速（若有可用设备）。

---

## 文件结构

。               
├── data/ # 放置训练图片      
│ ├── 12_example.jpg        
│ ├── 45_sample.png        
│ └── ...        
├── model/              
│ └── resnet50_regression.pth # 训练好的模型文件         
├── train.py # 训练脚本（你的代码）         
└── README.md # 项目说明文件            


---

## 依赖环境

- Python 3.7+
- PyTorch
- torchvision
- PIL (Pillow)
- numpy

可使用以下命令安装：

```bash
pip install torch torchvision pillow numpy
```

使用说明
将带标签的图片放入 data/ 文件夹，图片名格式需以标签数字开头，如 12_image.jpg。

运行训练脚本：

python train.py

训练完成后，模型会保存在 model/resnet50_regression.pth。

注意事项

模型文件较大，不建议上传至 Git 仓库。

标签数字会自动归一化处理。

图片只支持 .png, .jpg, .jpeg 格式。

训练过程中若遇异常图片会跳过并打印错误信息。


# ResNet50 图像回归模型测试脚本说明

本脚本用于加载训练好的 ResNet50 回归模型，对指定文件夹内的测试图片进行预测，并可视化展示预测结果。

---

## 功能介绍

- 自动加载训练好的模型和标签归一化范围。
- 对测试图片文件夹中的所有图片进行统一预处理。
- 逐张预测回归值（反归一化后）。
- 使用 matplotlib 动态排版展示测试图片及其预测值。
- 支持 GPU 加速（有 CUDA 环境时）。

---

## 文件说明

- `model/resnet50_regression.pth`：训练好的模型权重文件。
- `test/`：放置待测试图片的文件夹，支持 `.png`, `.jpg`, `.jpeg` 格式。
- `test_predict.py`（当前脚本）：预测并展示结果。

---

## 使用步骤

1. 确保已安装依赖：

```bash
pip install torch torchvision pillow matplotlib

```

### 将待测图片放入 test/ 文件夹。

运行测试脚本：

python test_predict.py

脚本会自动加载模型，预测所有测试图片，并弹出窗口展示预测结果。

### 注意事项

- 预测函数会自动处理异常图片并跳过。

- 预测值会基于训练时的标签范围做反归一化，确保数值直观。

- 画图窗口中最多每行显示 5 张图片，自动调整行数。

- 预测结果和图片名会打印在控制台，便于查看。
