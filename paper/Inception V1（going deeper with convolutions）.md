# Inception V1（going deeper with convolutions）

标签（空格分隔）： BaseNet

---

## 一、Insight
:    一般来说，提升网络性能的方法就是增加网络的深度和宽度，但是巨大的参数量容易导致过拟合，并且增加计算量。文章认为上述缺点的解决方法可以将全连接甚至是卷积转化为稀疏连接。
:	早些时候，为了提升学习能力，传统的网络用了随机稀疏连接，但是由于计算机对非均匀稀疏数据的计算差，所以AlexNet又开启了全连接。
:    Inception就是想用密集成分来近似局部稀疏结构。
:	作者首先提出了以下结构：
![初版](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v1-1.png)
:    采用不同大小的卷积核意味着不同的感受野，之所以选择135作为卷积核的大小，主要是方便之后的拼接，确定stride为1之后，只要将padding设为0,1,2就可以得到相同维度的特征。
:    但是这里使用了5*5的卷积，会带来巨大的计算量，于是考虑用1*1的卷积进行降维，这样计算量减少4倍。改进后如下图:
![最终版本](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v1-2.png)
    最终网络结构如下：
	该结构采用了模块化的结构，方便添加和修改；网络最后用average Pooling代替全连接；为了避免梯度消失，增加了2个辅助的softmax用于传播梯度，同时也作为辅助分类器，辅助分类器的最终结果以较小的权重添加到了最后的分类结果中，在测试的时候这两个辅助分类器被去掉。
![总体框架](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/v1.jpg).


    
    