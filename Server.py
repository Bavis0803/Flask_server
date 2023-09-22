from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Biến để lưu trạng thái của checkbox, mặc định là False
checkbox_state = False
port_no = 5000
@app.route('/check_login')
def check_login():
    global checkbox_state
    # Trả về giá trị của biến checkbox_state dưới dạng chuỗi 'true' hoặc 'false'
    return str(checkbox_state).lower()

@app.route('/')
def index():
    return render_template('index.html', checkbox_state=checkbox_state)

@app.route('/update_checkbox', methods=['POST'])
def update_checkbox():
    global checkbox_state
    data = request.get_json()
    isChecked = data.get('isChecked', False)
    checkbox_state = isChecked
    return jsonify({'message': 'Checkbox updated successfully'})
app.run(port=5000)