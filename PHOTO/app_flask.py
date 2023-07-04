'''                                                
                                     __            
  ___     ___               _____   /\_\      ___   
 /'___\ /' _ `\            /\ '__`\ \/\ \    /'___\ 
/\ \__/ /\ \/\ \           \ \ \L\ \ \ \ \  /\ \__/ 
\ \____\ \ \_\ \_\           \ \ ,__/  \ \_\ \ \____|
 \/____/ \/_/\/_/  _______   \ \ \/    \/_/  \/____/
                  /\______\   \ \_\                
                  \/______/    \/_/                


 __  __       _     
/\ \/\ \    /' \    
\ \ \ \ \  /\_, \   
 \ \ \ \ \ \/_/\ \  
  \ \ \_/ \   \ \ \ 
   \ `\___/    \ \_|
    `\/__/      \/_/               
'''
##===== IMPORT LIBRARY =====##
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import form
##===== IMPORT LIBRARY =====##



##===== SET FLASK APP =====##
app = Flask(__name__, static_folder='./static/', static_url_path='/static')
##===== SET FLASK APP =====##



##===== URL & PAGE SETTING =====##
# Start Page
@app.route('/')
def start():
    # Delete Old Picture
    # try:
    #     for i in range(8):
    #         os.remove('PHOTO/static/image/img_'+str(i+1)+'.webp')
            
    # except:
    #     # print("no more pic")
    #     pass        
    
    return render_template('start.html')

# Frame Select Page
@app.route('/frame')
def frame():
    #Code#
    return render_template('frame.html')

# Frame Type Submit Page
@app.route('/submit', methods=['POST'])
def save():
    global quantity # Quantity To Print Picture
    quantity = request.form.get('quantity')
    
    # print(quantity) # Debugging
    
    global style # Frame Style
    style = request.form.get('f_color')
    # print(style) # Debugging
    
    return redirect(url_for('pay')) # Move to http://127.0.0.1:5000/pay

# Payment Page
@app.route('/pay')
def pay():
    global quantity
    price = int(quantity)*3000
    print(price)
    #Code#
    # Not Developed, After Arduino Job Is Done
    # return render_template('payment.html') # Release Ver.
    return redirect(url_for('cam')) # For ProtoType, Not Release Ver.

# Taking Pic Page
@app.route('/cam')
def cam():
    #Code#
    return render_template('cam.html')

# Pic Select Page
@app.route('/select')
def select():
    #Code#
    return render_template('select.html')

@app.route('/selected', methods=['POST'])
def selected():
    selected_list = request.get_json()  # Get Data From AJAX
    
    # print(selected_list)  # Debugging
    
    if(len(selected_list)>=4):
        global s_l # Selected List
        s_l = list(selected_list)
        
    return redirect(url_for('printing'))

# Pic make_pic Page
@app.route('/makepic')
def makepic():
    form.paste(s_l[0],s_l[1],s_l[2],s_l[3], style, quantity)
    #s_l[0] => first Pic Num, .... , style => Frame Style, quantity => Quantity To Print Picture
    
    return redirect(url_for('printing'))

# Printing Page
@app.route('/printing')
def printing():
    #CODE#
    t = str(form.get_path())
    path = t[len("/PHOTO"):]
    print(path)
    return render_template('printing.html', path = path)
##===== URL & PAGE SETTING =====##



##===== MAIN CODE =====##
if __name__ == '__main__':
    app.run(debug=True)
##===== MAIN CODE =====##
    
    
    
##===== MAC KIOSK CHROME =====##
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --kiosk --app http://127.0.0.1:5000
##===== MAC KIOSK CHROME =====##
