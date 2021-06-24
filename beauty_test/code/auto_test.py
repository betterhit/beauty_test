import base64
import json
import requests
import tkinter as tk
from tkinter import filedialog,ttk
def openfile():
    file_path = filedialog.askopenfilename()
    fpath.set(file_path)
def auto_test():
    class autobeauty:
            def __init__(self,img):
                self.ak = "****"
                self.sk = "****"
                self.img_src = img
                self.headers = {
                    "Content-Type": "application/json; charset=UTF-8"
                }
            def test_face(self):

                headers =  { "Content-Type": "application/json; charset=UTF-8"}
                host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' +self.ak + '&client_secret=' + self.sk
                resp = requests.get(url=host,headers=headers)
                json_resp = json.loads(resp.text)
                access_token = json_resp['access_token']
                with open(self.img_src,'rb') as f:
                    new_img = base64.b64encode(f.read())
                resp_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"+"?access_token=" + access_token
                post_data = {
                    "image":new_img,
                    "image_type":"BASE64",
                    "face_field":"age,beauty",
                    "face_type":"LIVE"
                }
                response = requests.post(url=resp_url, data=post_data, headers=headers)
                json_result = json.loads(response.text)
                t1 = tk.Label(win, text=json_result['result']['face_num']).grid(row=4, column=1)
                t2 = tk.Label(win, text=json_result['result']['face_list'][0]['age']).grid(row=8, column=1)
                t3 = tk.Label(win, text=json_result['result']['face_list'][0]['beauty']).grid(row=12, column=1)


    if __name__ == '__main__':
        img_src = fpath.get()
        a = autobeauty(img_src)
        a.test_face()

win = tk.Tk()
win.title("颜值检测系统")
win.geometry("500x300")
fpath=tk.StringVar()

l = tk.Label(win, text='基于百度aip的颜值检测', bg='yellow', font=('加粗,居中对齐',20),fg='red',justify='center')
l.grid(row=1,column=0)
ttk.Button(win,text='打开图片',command=openfile).grid(row=2,column=0)
ttk.Entry(win,textvariable=fpath).grid(row=2,column=1)
l1 = tk.Label(win, text='人脸数：',font=('黑体',15))
l1.grid(row=4,column=0)
l2 = tk.Label(win, text='人物年龄：',font=('黑体',15))
l2.grid(row=8,column=0)
l3 = tk.Label(win, text='人物颜值评分：',font=('黑体',15))
l3.grid(row = 12,column=0)
b=tk.Button(win,text="点我检测",width=15,height=2,command=auto_test,activebackground='yellow',font=('黑体',15))
b.grid(row=16,column=0)


win.mainloop()
