from tkinter import *
import time
import requests
import json

def get_response(msg):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    dat = {
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": "yourapikey",
            "userId": 19990706
        }
    }
    dat = json.dumps(dat)
    r = requests.post(api, data=dat).json()

    #以下为r的内容
    #{'emotion': {'userEmotion': {'emotionId': 10300, 'd': 0, 'p': 0, 'a': 0},
    #              'robotEmotion': {'emotionId': 0, 'd': 0, 'p': 0, 'a': 0}},
    #  'intent': {'code': 10004, 'actionName': '', 'intentName': ''},
    # 'results': [{'resultType': 'text', 'values': {'text': '别兴奋别兴奋，很高兴认识你！'}, 'groupType': 1}]}

    mesage = r['results'][0]['values']['text']
#     print(r['results'][0]['values']['text'])
    return mesage

def main():

    def sendMsg():#发送消息
        strMsg = "我:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        txtMsgList.insert(END, strMsg, 'greencolor')
        send = txtMsg.get('0.0', END) # 输入发送的信息
        txtMsgList.insert(END, send) # 显示
        txtMsg.delete('0.0', END)
        returnMsg(send)
    def returnMsg(send):
        returnback = get_response(send)
        strMsg = "姬小野:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        txtMsgList.insert(END, strMsg, 'greencolor')
        txtMsgList.insert(END, returnback)
        txtMsgList.insert(END, '\n')
        txtMsg.delete('0.0', END)

    def cancelMsg():#取消信息
        txtMsg.delete('0.0', END)

    def sendMsgEvent(event):#发送消息事件
        if event.keysym =='Up':
            sendMsg()
    #创建窗口
    app = Tk()
    app.title('图灵机器人姬小野')

    #创建frame容器
    frmLT = Frame(width = 600, height = 360, bg = 'white')
    frmLC = Frame(width = 600, height = 160, bg = 'white')
    frmLB = Frame(width = 600, height = 30)
    frmRT = Frame(width = 300, height = 600)

    #创建控件
    txtMsgList = Text(frmLT)
    txtMsgList.tag_config('greencolor',foreground = '#008C00')#创建tag
    txtMsg = Text(frmLC)
    txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
    btnSend = Button(frmLB, text = '发送', width = 8, command = sendMsg)
    btnCancel =Button(frmLB, text = '取消', width = 8, command = cancelMsg)
    imgInfo = PhotoImage(file = "background.png")
    lblImage = Label(frmRT, image = imgInfo)
    lblImage.image = imgInfo

    #窗口布局
    frmLT.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 3)
    frmLC.grid(row = 1, column = 0, columnspan = 2, padx = 1, pady = 3)
    frmLB.grid(row = 2, column = 0, columnspan = 2)
    frmRT.grid(row = 0, column = 2, rowspan = 3, padx =2, pady = 3)

    #固定大小
    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    frmRT.grid_propagate(0)

    btnSend.grid(row = 2, column = 0)
    btnCancel.grid(row = 2, column = 1)
    lblImage.grid()
    txtMsgList.grid()
    txtMsg.grid()

    #主事件循环
    app.mainloop()

if  __name__ == "__main__":
    main()
