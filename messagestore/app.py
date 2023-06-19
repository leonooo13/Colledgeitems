from flask import Flask,render_template,request
from chatdb import get_post,add_post,del_cnt
import time
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def show_msg():
    if request.method=='POST':
        msg=request.form['msg']
        # print(time.localtime())
        t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(str(t))
        msg_date=(str(msg),str(t))
        # print(msg_date)
        add_post(msg_date)
    # for content,date in get_post():
    #     print(content,date)
    msg_date=get_post()
    print(msg_date)
    return render_template('chat.html',msg_date=msg_date)

if __name__=='__main__':
    app.run()