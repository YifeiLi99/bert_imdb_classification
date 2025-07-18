from datasets import load_dataset
from collections import Counter
import matplotlib.pyplot as plt

# ✅ 1. 下载 IMDB 数据集
dataset = load_dataset("imdb")

print("\n✅ 数据集加载完成!")
print(f"训练集样本数: {len(dataset['train'])}")
print(f"测试集样本数: {len(dataset['test'])}")
print(f"无标签数据样本数: {len(dataset['unsupervised'])}")\n")

# ✅ 2. 查看一个样本
sample = dataset["train"][0]
print("样例样本:\n", sample)

# ✅ 3. 统计训练集类别分布
train_labels = [example['label'] for example in dataset['train']]
label_counter = Counter(train_labels)
print("\n训练集类别分布:", label_counter)

# ✅ 4. 绘制类别分布直方图
plt.figure(figsize=(4,4))
plt.bar(['Negative (0)', 'Positive (1)'], [label_counter[0], label_counter[1]], color=['red', 'green'])
plt.title("IMDB Train Set Sentiment Distribution")
plt.ylabel("样本数")
plt.show()

# ✅ 5. （可选）保存为CSV
save_csv = False  # 改为 True 可导出CSV
if save_csv:
    print("\n保存为CSV中...")
    dataset["train"].to_csv("./data/train.csv", index=False)
    dataset["test"].to_csv("./data/test.csv", index=False)
    print("✅ CSV保存完成: ./data/train.csv & ./data/test.csv")
