# InceptionV2 BatchNormalization

标签（空格分隔）： BaseNet

---

## 一、inception版本的说明
一共有4个版本，初代v1就是GoogLeNet，但是网上有很多都搞混了v2和v3的区别，不管怎么样，Google在V4版本里面做了说明
>“The Inception deep convolutional architecture was introduced as GoogLeNet in (Szegedy et al. 2015a), here named Inception-v1. Later the Inception architecture was refined in various ways, first by the introduction of **batch normalization (Ioffe and Szegedy 2015) (Inception-v2)**. Later by additional **factorization ideas** in the third iteration (Szegedy et al. 2015b) which will be referred to as **Inception-v3** in this report.”

因此，当遇到BN的时候，指的是InceptionV2或者BN-Inception.

## 二、Insight
DNN难以训练的原因是在训练的时候每层的输入的分布都在变化，并且因为sigmoid的饱和区的存在。所以在训练DNN的时候，尤其要注意初始权重的过程和学习率的选择，这种现象就是**internal covariate shift**.

### 1. 解决方法
![BN](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/bn.png)
:    在训练的时候，首先估计一个mini-batch的均值和方差，然后减去均值除以标准差完成一个初始的normalize的操作，分母下面有一个极小值是为了防止标准差为0的情况。${\gamma}$和${\beta}$是两个可学习的参数，如果只做标准的normalization的话，对于sigmoid来说，输入都在0附近，那里的导数变化很小，可以认为失去了非线性的特征，而非线性就是神经网络的精髓所在，所以需要这个两个变量来调节。
## 2、好处
BN对网络中梯度的传播有非常大的好处，因为它减少了梯度对参数初始值和大小的依赖。这就允许我们可以使用更高的学习率，并且对网络是一种正则化，可以减少DropOut的使用。






