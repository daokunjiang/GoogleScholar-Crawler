def name_contraction(arg):
    name_list = arg.split(',')
    name_return = ''
    for i in name_list:
        each_name = i.split()
        if i == name_list[-1]:
            last_name = each_name[-1]
        else:
            last_name = each_name[-1] + ', '
        for i in range(0,len(each_name)-1):
            if each_name[i].isupper():
                name_return += each_name[i] + ' '
            elif each_name[i].find('-') != -1:
                tt = each_name[i].split('-')
                for ii in tt:
                    name_return += ii[0]
                name_return += ' '
            else:
                name_return += each_name[i][0] + ' '
        name_return += last_name
    print(name_return)
    return name_return

z1 = 'Geng Qian, Long-Huan Zeng, Yu-Qi Liu, Feng Cao, Yun-Dai Chen, Mei-Li Zheng, Xin-Chun Yang, Xi-Ping Xu, Yong Huo'
# G Qian, LH Zeng, YQ Liu, F Cao, YD Chen, ML Zheng, XC Yang, XP Xu,

# WJ Yan, CY Zhang, X Yang, ZN Liu, XZ Wang, XY Sun, YX Wang, ...
z2 = 'WJ Yan, CY Zhang, X Yang, ZN Liu, XZ Wang, XY Sun, YX Wang, SG Zheng'

x_ex = 'L Chang, X Ye, Y Qiu, G Ma, Y Jin, H Chen, D Lv, W Yu, X Yang, T Wang, ...'
x = 'Lei Chang, Xiaoxiao Ye, Yajing Qiu, Gang Ma, Yunbo Jin, Hui Chen, Dongze Lv, Wenxin Yu, Xi Yang, Tianyou Wang, Xiaoxi Lin'

# Z Shen, T Li, D Chen, S Jia, X Yang, L Liang, J Chai, X Cheng, X Yang, ...
y1 = 'Zhiyuan Shen, Tianyi Li, Da Chen, Sen Jia, Xiangming Yang, Liang Liang, Juan Chai, Xiaobing Cheng, Xinjie Yang, Moyi Sun'
# N Gao, W Lin, X Chen, K Huang, S Li, J Li, H Chen, X Yang, L Ji, ...
y2 = 'Na Gao, Wei Lin, Xue Chen, Kai Huang, Shuping Li, Jinchai Li, Hangyang Chen, Xu Yang, Li Ji, T Yu Edward, Junyong Kang'
# R Chen, J Wang, B Jiang, X Wan, H Liu, H Liu, X Yang, X Wu, Q Zou, ...
y3 = 'Rui Chen, Junyu Wang, Bing Jiang, Xin Wan, Hongwei Liu, Huan Liu, Xiaosheng Yang, Xiaobing Wu, Qin Zou, Wenren Yang'

name_contraction(y3)