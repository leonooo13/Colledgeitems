import tkinter as tk
import socket
import struct
def sniffer(s,n):
    # todo 捕获数据包
    ans=[]
    for _ in range(n):
        data=s.recvfrom(65536)[0]
        # 数据总长度
        lenth=len(data)
        # IP头
        ip_header=struct.unpack('!BBHHHBBH4s4s',data[0:20])
        #将十六进制的源ip地址转换成十进制的源IP    
        s_addr = socket.inet_ntoa(ip_header[-2])
        #将十六进制的目的IP转换为十进制的目的IP
        d_addr = socket.inet_ntoa(ip_header[-1])
        #提取版本及头长度
        v_h = '{:0>8}'.format(str(bin(ip_header[0]))[2:])
        version = int('0b'+v_h[0:4],2)
        #提取数据包的区分服务位
        deff = hex(ip_header[1])
        #获取数据包总长度
        total_len = ip_header[2]
        #获取数据包的标识
        data_id = ip_header[3]
        #获取标志位
        flag = ip_header[4]
        #获取数据包的TTL值
        ttl = ip_header[5]
        #获取上层协议
        proto = ip_header[6]
        #获取头校验和
        head_checksum = hex(ip_header[7])
        msg=data[40:]
        try:
            msg=msg.decode()
        except:
            msg=msg
        ans_dic={"lenth":lenth,"soure_ip":s_addr,"dest_ip":d_addr,"version":version,"mark":deff,"datalen":total_len,"dataid":data_id,"flag":flag,"TTL":ttl,"proto":proto,"head_checksum":head_checksum,"msg":msg}
        ans.append(ans_dic)
    return ans
def show_page(content):
    mainpage=tk.Tk()
    mainpage.title("CaptureData")
    mainpage.geometry("800x600")
    lenth="数据长度："+str(content["lenth"])
    soure_ip="源IP："+str(content["soure_ip"])
    dest_ip="目的IP："+str(content["dest_ip"])
    version="IP包版本："+str(content["version"])
    mark="ip包的区分服务标记是："+str(content["mark"])
    datalen="数据长度："+str(content["datalen"])
    dataid="数据包id："+str(content["dataid"])
    flag="数据包标志位："+str(content["flag"])
    ttl="TTL："+str(content["TTL"])
    proto="上层协议的编号是："+str(content["proto"])
    head_checksum="IP头校验和"+str(content["head_checksum"])
    msg="数据包内容："+str(content["msg"])
    
    text0=tk.Text(mainpage,height=2,font=1)
    text0.insert("end",lenth)
    text0.pack()

    text1=tk.Text(mainpage,height=2,font=1)
    text1.insert("end",soure_ip)
    text1.pack()

    textv1=tk.Text(mainpage,height=2,font=1)
    textv1.insert("end",dest_ip)
    textv1.pack()

    text2=tk.Text(mainpage,height=2,font=1)
    text2.insert("end",version)
    text2.pack()

    text3=tk.Text(mainpage,height=2,font=1)
    text3.insert("end",mark)
    text3.pack()

    text4=tk.Text(mainpage,height=2,font=1)
    text4.insert("end",datalen)
    text4.pack()

    text5=tk.Text(mainpage,height=2,font=1)
    text5.insert("end",dataid)
    text5.pack()    

    text6=tk.Text(mainpage,height=2,font=1)
    text6.insert("end",flag)
    text6.pack()

    text7=tk.Text(mainpage,height=2,font=1)
    text7.insert("end",ttl)
    text7.pack()

    text8=tk.Text(mainpage,height=2,font=1)
    text8.insert("end",proto)
    text8.pack()

    text9=tk.Text(mainpage,height=2,font=1)
    text9.insert("end",head_checksum)
    text9.pack()

    text10=tk.Text(mainpage,height=2,font=1)
    text10.insert("end",msg)
    text10.pack()
    button1=tk.Button(mainpage,text="下一页")
    button1.pack(pady=10)
 
    mainpage.mainloop()
def create_page(contents,n):
    for i in range(n):
        show_page(content=contents[i])

if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    host=socket.gethostbyname(socket.gethostname())
    s.bind((host,0))
    # 设置套接字选项
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    # 设置混杂模式
    s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
    # 闯入参数，捕获多个包
    c=sniffer(s,1)
    print(c)
    window=tk.Tk()
    window.title("NetWork Sniffer")
    window.geometry("400x300")
    lable=tk.Label(window,text="欢迎使用网络嗅探器",font=(12))
    lable.pack(pady=50)
    button1=tk.Button(window,text="开始使用",command=lambda:create_page(c,1))
    button1.pack(pady=50)
    window.mainloop()
