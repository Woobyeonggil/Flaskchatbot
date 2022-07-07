from flask import Flask, render_template ,request ,jsonify
import json #챗봇에서 json형태로 날아옴

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #render_template 함수가 templates로 찾아감


@app.route('/chatbot',methods=('POST','GET'))
def chatbot():
    req= request.get_json(force=True)
    print(req)
    #return jsonify(fulfillmentText= '챗봇 접속 성공')
        #{ 'fullfillmentText': '챗봇접속성공'}
    return jsonify(fulfillment_messages=[{
        "payload":{
            "richContent" : [
                [
                    {
                        "type": "image" ,
                        "rawUrl":"http://daontd.com/wp-content/uploads/2022/01/%EC%9D%B4%EB%AF%B8%EC%A7%80-008.jpg"},

                ],
                [
                    {"type": 'info',
                       "tytle": '피자메뉴',
                       "subtitle": "도미노피자주소",
                       "actionLink":"https://web.dominos.co.kr/event/viewHtml?seq=1598&gubun=E0200&gclid=Cj0KCQjw5ZSWBhCVARIsALERCvyBMDYkOAG1iasBTcfQeRjRYzc3ZTUTpe8VJT0rsL7TXIQhNTUSbm4aAp_XEALw_wcB"}
]

            ]
        }
    }
    ])

if __name__=='__main__':
    app.run('0.0.0.0',port=5001, debug=True)

