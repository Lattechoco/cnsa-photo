from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import form

app = Flask(__name__, static_folder='./static/', static_url_path='/static')

# Start Page
@app.route('/')
def start():
    #Code#
    # Delete Old Pic
    try:
        for i in range(8):
            os.remove('PHOTO/static/image/img_'+str(i+1)+'.webp')
    except:
        print("no more pic")
        
    return render_template('start.html')

# Frame Select Page
@app.route('/frame')
def frame():
    #Code#
    return render_template('frame.html')

@app.route('/submit', methods=['POST'])
def save():
    global quantity 
    quantity = request.form.get('quantity')
    print(quantity)
    
    global style
    style = request.form.get('f_color')
    print(style)
    return redirect(url_for('pay'))

# Payment Page
@app.route('/pay')
def pay():
    #Code#
    # return render_template('payment.html')
    return redirect(url_for('cam'))

# Taking Pic Page
@app.route('/cam')
def cam():
    return render_template('cam.html')

# Pic Select Pafe
@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/selected', methods=['POST'])
def selected():
    selected_list = request.get_json()  # AJAX에서 전송된 데이터를 받음
    print(selected_list)  # 선택된 항목 리스트를 Flask 서버의 콘솔에 출력

    # selected = request.form.getlist('test')
    # print(selected)
    # # print(selected[0],selected[1],selected[2],selected[3])
    # # print(style, quantity)
    if(len(selected_list)>=4):
        global s_l
        s_l = list(selected_list)
    return render_template('printing.html')

@app.route('/printing')
def printing():
    form.paste(s_l[0],s_l[1],s_l[2],s_l[3], style, quantity)
    return render_template('printing.html')
if __name__ == '__main__':
    app.run(debug=True)
    
    
#--IN MAC--#
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --kiosk --app http://127.0.0.1:5000