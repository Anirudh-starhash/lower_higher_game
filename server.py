from flask import Flask
from flask import request
from flask import redirect
app=Flask(__name__)
import random

final_answer=random.randint(0,9);


initial='<h1 style="text-align:center">Guess a number between 0 and 9</hi>\
            <div style="width:480px;display:flex;align-items:center; justify-content:center; text-align:center; padding:50px; ">\
                <iframe frameBorder="0" height="270"\
                    src="https://giphy.com/embed/4pqm16XH2rQopZrdFU/video"\
                        width="480">\
                </iframe>\
            </div> \
            <form method="POST" style="display:flex; justify-content:space-around; text-align:center; padding:50px;" action="/lower_higher" >\
                <label for="guess" style="color:red;">Guess your Number</label>\
                <input type="text" name="guess" width:200px>\
                <button type="submit"  style="background-color:aqua; color:blue; height:50px; width:100px">Submit</button>\
            </form>'
            
correct_answer=f'<h1 style="text-align:center">Yo! you got is correct! and ur answer is {final_answer}</hi>'\
            '<div style="width:480px;display:flex;align-items:center; justify-content:center; text-align:center; padding:50px; ">\
               <iframe src="https://giphy.com/embed/9vmL0jnZYNl8c6n4b2" width="480" height="480" style=""\
                   frameBorder="0" class="giphy-embed" allowFullScreen>\
                </iframe>\
            </div>'
            
too_low='<h1 style="text-align:center">Too low guess again</hi>\
            <div style="width:480px;display:flex;align-items:center; justify-content:center; text-align:center; padding:10px; ">\
               <iframe src="https://giphy.com/embed/d7zlVzxPEcqay0NeNw" \
                   width="380" height="480" style="" \
                   frameBorder="0" class="giphy-embed" allowFullScreen>\
               </iframe>\
            </div>\
            <form method="POST" style="display:flex; justify-content:space-around; text-align:center; padding:50px;" action="/lower_higher" >\
                <label for="guess" style="color:red;">Guess Again</label>\
                <input type="text" name="guess" width:200px>\
                <button type="submit"  style="background-color:aqua; color:blue; height:50px; width:100px">Submit</button>\
            </form>'
            
            
too_high='<h1 style="text-align:center">Too high guess again</hi>\
            <div style="width:480px;display:flex;align-items:center; justify-content:center; text-align:center; padding:50px; ">\
                <iframe src="https://giphy.com/embed/3og0IuWMpDm2PdTL8s"\
                    width="480" height="307" style="" frameBorder="0" class="giphy-embed" \
                        allowFullScreen>\
                    </iframe>\
            </div>\
            <form method="POST" style="display:flex; justify-content:space-around; text-align:center; padding:50px;" action="/lower_higher" >\
                <label for="guess" style="color:red;">Guess Again</label>\
                <input type="text" name="guess" width:200px>\
                <button type="submit"  style="background-color:aqua; color:blue; height:50px; width:100px">Submit</button>\
            </form>'
            

message=initial

@app.route("/")
def start():
    return message

@app.route("/lower_higher",methods=['POST'])

def play():
    if request.method=="POST":
        answer=request.form.get("guess")
        global message
        
        if final_answer==int(answer):
           message=correct_answer
        elif final_answer>int(answer):
            message=too_low
        else:
            message=too_high
            
        return redirect("/")
            
        
if __name__=="__main__":
    app.run(debug=True) 