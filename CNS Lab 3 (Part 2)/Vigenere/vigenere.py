from flask import Flask, request, render_template,jsonify
app = Flask(__name__)


def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine

def encrypt(plain,key):
	plain= plain.lower()
	key= key.lower()
	n=len(key)
	k=[]
	ci=[]

	for i in plain:
	    if i != ' ':
	      ci.append(ord(i)-97)
	#print(ci)
	key = key*(len(ci)//n + 1)

	print(key)

	for i in key:
	    k.append(ord(i)-97)



	print(k)


	for i in range(len(ci)):
	    ci[i]= chr((ci[i]+k[i])%26 + 97)

	return "".join(ci)

def decrypt(cip, key):
	n=len(key)
	cip= cip.lower()
	key= key.lower()
	k=[]
	pl=[]

	for i in cip:
		if i != ' ':
			pl.append(ord(i)-97)
	#print(pl)
	key = key*(len(pl)//n + 1)

	#print(key)

	for i in key:
		k.append(ord(i)-97)



	#print(k)


	for i in range(len(pl)):
	    pl[i]= chr((pl[i]-k[i])%26 + 97)

	return "".join(pl)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    text3 = request.form['text3']
    encry = encrypt(text1,text2)
    decry= decrypt(text3,text2)

    result = {
        "Cipher text": encry, "Decrypted text": decry

    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True)