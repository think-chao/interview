# InceptionV3

标签（空格分隔）： BaseNet

---

##一、Factorizing Convolutions
目的，减少参数
###1. 用两个3*3的卷积代替5*5的卷积
:   如果使用5*5的卷积，参数量为25，两个3*3的参数量只有18

:   ![3*3代替5*5](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v3-1.png)![对比](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/duibi.jpg)

###2. 分解为非对称卷积
![非对称卷积](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v3-3.png)
![非对称卷积](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v3-4.png)

###3. Efficient Grid Size Reduction
:   传统的减小feature map大小的方法是做Pooling，为了避免遇到表达能力的瓶颈，提出：先池化再作Inception卷积，或者先作Inception卷积再作池化。但是方法一（左图）先作pooling（池化）会导致特征表示遇到瓶颈（特征缺失），方法二（右图）是正常的缩小，但计算量很大。为了同时保持特征表示且降低计算量，将网络结构改为下图，使用两个并行化的模块来降低计算量（卷积、池化并行执行，再进行合并）
![并行](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v3-7.png)

**Less expensive and still efficient network is achieved by this efficient grid size reduction**

##二、2. Auxiliary Classifier

在这里只有一个复制分类器被使用，在v1中辅助分类器是为了得到更深的网络，帮助梯度的传播，在V3中辅助分类器的作用是作为正则化来使用
![辅助分类器](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v3-6.png)

##三、 Label Smoothing Regulization
Label Smoothing Regularization（LSR）是一种通过在输出y中添加噪声，实现对模型进行约束，降低模型过拟合（overfitting）程度的一种约束方法。一般分类模型通常采用one-hot编码对结果进行标注，但是这样可能会产生两个问题
1. 过拟合：训练集往往是不可能涵盖所有情况的，特别是在样本量少的时候，如果我的训练数据集中某一类出现的次数稍微多一点，随着训练的进行，模型就会使得那一类的概率越来越大，就使得别的出现的少的类的概率消失了，这样是不对的
2. 模型过于自信
Label Smoothing就是为了防止最大的逻辑单元与其他的单元的差距越来越大
new_labels = (1 — ε) * one_hot_labels + ε / K

## 四、总的结构
![总体结构](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v3.png)


    






