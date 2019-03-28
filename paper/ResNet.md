# ResNet

标签（空格分隔）： BaseNet

---
## **Insights**
:   传统的卷积网络或者全连接网络在信息传递的过程中或多或少会存在信息丢失的情况，随着网络的加深，会出现**训练集**准确率下降的问题,可以推断出不是由于过拟合的原因，针对这一问题作者提出了一种全新的网络。

## **background**
:   理论上只具有一层隐藏层的前馈网络足以表达任意函数，但是这会造成巨大的餐数量，网络也很可能会overfit，因此大家有一个共识就是网络需要更深。但是光光简单的堆叠卷积层并不能work，因为存在梯度消失的问题，网络难以继续学习

##**introduction**
:   resNet的一个核心idea是identity shortcut connection
![residual block](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/residual%20block.jpg)
    作者发现按照这种方式不会造成网络performance随着layer的变深而下降，因为identity mapping的存在，网络可以保持在一个不做任何更新的起点。
    事实上作者不是第一个做了这个常识的人，highway networks就引入了门控快捷链接，因此resnet可以看做是highway network的子集，理论上应该不会比resnet差，所以可以表明更通畅的梯度highway比更大的解空间更加重要。
    为了减少参数，作者还提出来一个改进的结构;
    
![减少参数](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/res1.jpg)

##**question**##
:   
:   identity mapping和residual mapping的通道数不一样怎么相加
![通道不一致](https://raw.githubusercontent.com/think-chao/interview/master/paper/images/res2.png)

>   y = F(x) + Wx

:    通过参数W来控制维度





