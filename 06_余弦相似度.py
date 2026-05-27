import numpy as np
#实现点积的函数
def get_dot(vec_a,vec_b):
    if(len(vec_a)!=len(vec_b)):
        print("两个向量的维度必须相同")
        return

    dot_value=0
    for a,b in zip(vec_a,vec_b):
        dot_value+=a*b
    return dot_value
#实现模长的函数
def get_norm(vec):
    sum=0
    for a in vec:
        sum+=a*a
    sum=np.sqrt(sum)
    return sum
#实现余弦相似度的函数
def cosine_similarity(vec_a,vec_b):
    result=get_dot(vec_a,vec_b)/(get_norm(vec_a)*get_norm(vec_b))
    return result
if __name__ == '__main__':#只有运行这个文件的时候才会执行一下代码
    vec_a=[0.5,0.5]
    vec_b=[0.7,0.7]
    vec_c=[0.5,0.7]
    vec_d=[-0.6,-0.6]
    #将向量也可以看作有序数组
    print('ab', cosine_similarity(vec_a,vec_b))
    print('ac', cosine_similarity(vec_a,vec_c))
    print('ad', cosine_similarity(vec_a,vec_d))