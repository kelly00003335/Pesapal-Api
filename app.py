
from pesapal import PesapalAPI
import uuid
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
pesapal = PesapalAPI()

@app.route('/')
def deposit_page():
    return render_template('deposit.html')

@app.route('/process_deposit', methods=['POST'])
def process_deposit():
    try:
        phone = request.form['phone']
        amount = float(request.form['amount'])
        order_id = str(uuid.uuid4())
        fname = request.form['fname']
        lname = request.form['lname']
        
        result = pesapal.initiate_payment(phone, amount, order_id, fname, lname)
        
        if result and result.get('redirect_url'):
            return redirect(result['redirect_url'])
        else:
            return jsonify({'error': 'Failed to initiate payment'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
