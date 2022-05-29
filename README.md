## 注：该版本是我修改了需要用到cuda的部分得到的一个可以运行的版本，运行配置和源项目一样，有问题请联系1070008296（qq)
对于三通道24位mask文件加入了8位转换，convert文件夹里有一些可能用到的工具文件
grabcut不太好用，边缘抖动无法处理，所以我手动扣了图又转了mask
本项目使用的人体语义解析项目为CIHP_PGN（https://github.com/Engineering-Course/CIHP_PGN）
使用的人体关键点识别为https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases cpu版本,模型为body_25
源程序readme见README_ORI
请注意运行时定义test_pairs.txt文件


改进点：通过程序实现抠图取衣物mask，优化边缘抖动，抠图还是黑色背景好，但是换背景还得抠图...
拟合效果仍然有问题，部分非正面衣物或原图衣物边缘及褶皱会给拟合结果带来奇怪的扭曲效果
纹理的保持

在convert文件夹中新增了background.py功能是背景替换，有问题请邮件联系1483484139@qq.com
