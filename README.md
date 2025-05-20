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

.
├── data/ # 放置训练图片
│ ├── 12_example.jpg
│ ├── 45_sample.png
│ └── ...
├── model/
│ └── resnet50_regression.pth # 训练好的模型文件
├── train.py # 训练脚本（你的代码）
└── README.md # 项目说明文件

yaml
复制代码

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
使用说明
将带标签的图片放入 data/ 文件夹，图片名格式需以标签数字开头，如 12_image.jpg。

运行训练脚本：

bash
复制代码
python train.py
训练完成后，模型会保存在 model/resnet50_regression.pth。

注意事项
模型文件较大，不建议上传至 Git 仓库。

标签数字会自动归一化处理。

图片只支持 .png, .jpg, .jpeg 格式。

训练过程中若遇异常图片会跳过并打印错误信息。
