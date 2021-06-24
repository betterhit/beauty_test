import os
from code.beauty_inerface import test_face
import tkinter as tk
from get_img import numdict
path1 = r'C:\\Users\\fuhang\\Desktop\\beauty'
path2 = r'C:\\Users\\fuhang\\Desktop\\huya'
path3 = r'C:\\Users\\fuhang\\Desktop\\douyu'
image_list1 = os.listdir(path1)
image_list2 = os.listdir(path2)
image_list3 = os.listdir(path3)
#通过os库遍历文件路径
win = tk.Tk()
win.title("颜值检测")
win.geometry("500x300")
score_dict = {}
'''
for img in image_list1:
    try:
        img_path = path1 +'\\'+img
        name = "优美"+img.split('.')[0]

        face_result = test_face(img_path)
        score_dict[name] = face_result
    except Exception as e:
        print(f"正在检测{name}：|检测失败！！！！")
    else:
        print(f"正在检测{name}：|颜值检测的分数为{face_result}")
print("优美图库检测完成！！！！")
'''
for img in image_list2:
    try:
        img_path = path2 +'\\'+img
        name = img.split('.')[0]

        face_result = test_face(img_path)
        score_dict[name] = face_result
    except Exception as e:
        print(f"正在检测{name}：|检测失败！！！！")
    else:
        print(f"正在检测{name}：|颜值检测的分数为{face_result}")
print("虎牙图库检测完成！！！！")

for img in image_list3:
    try:
        img_path = path3 +'\\'+img
        name = img.split('.')[0]

        face_result = test_face(img_path)
        score_dict[name] = face_result
    except Exception as e:
        print(f"正在检测{name}：|检测失败！！！！")
    else:
        print(f"正在检测{name}：|颜值检测的分数为{face_result}")
print("斗鱼图库检测完成！！！！")

i=1
change_score = sorted(score_dict.items(),key=lambda x:x[1],reverse=True)

#降序排序
for a,b in enumerate(change_score):
   try:
       var = 't'+str(i)
       s ='颜值名次：第{}名,颜值分数：{},主播昵称：{},人气值：{}'.format(i,change_score[a][1],change_score[a][0],numdict[change_score[a][0]])
       var = tk.Label(win, text=s).grid(row=i, column=0,sticky='w')
       #循环设置标签并设置为左对齐
   except Exception as e:
       print("暂无此人！")
   else:
       i+=1

win.mainloop()