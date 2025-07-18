# 📌 BERT IMDB 情感分类项目

本项目基于 BERT 模型实现 IMDB 电影评论情感分类任务，完整覆盖数据下载、预处理、模型训练、推理部署与可视化分析流程，适合作为 NLP 方向简历项目。

---

## 📂 项目结构

```
bert_imdb_classification
│   config.py              # 配置信息
│   train.py               # 模型训练主流程
│   predict.py             # 推理脚本
│   README.md              # 项目说明
└───data                   # 存放IMDB数据集
└───models                 # 存放训练好的模型
└───logs                   # 训练日志文件
└───notebooks              # 可选：数据探索/可视化
```

---

## 🚀 项目亮点

- ✅ 使用 `bert-base-uncased` 作为主干网络
- ✅ 自动下载 HuggingFace 官方 IMDB 数据集
- ✅ 训练过程中实时输出准确率和 F1-score
- ✅ 推理脚本可对任意一句影评进行预测
- ✅ 完整训练日志记录
- ✅ 可选 Gradio 部署（后续拓展）

---

## 💡 技术栈

- Python 3.10
- PyTorch 2.x
- Huggingface Transformers
- Datasets
- scikit-learn
- tqdm、matplotlib

---

## ⚙️ 使用说明

### 1. 克隆项目

```bash
git clone https://github.com/你的github账号/bert_imdb_classification.git
cd bert_imdb_classification
```

### 2. 安装依赖

```bash
conda create -n bertimdb python=3.10 -y
conda activate bertimdb
pip install -r requirements.txt
```

### 3. 训练模型

```bash
python train.py
```

### 4. 推理示例

```bash
python predict.py --text "This movie was fantastic!"
```

---

## 📝 数据来源

- IMDB Dataset on Huggingface

---

## 📊 性能指标

| 指标          | 数值（示例） |
| ----------- | ------ |
| 准确率 Accuracy | 94%    |
| F1-score    | 93%    |

> 训练完成后可更新实际结果

---

## 📎 TODO

-

