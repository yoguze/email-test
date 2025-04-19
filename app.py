from flask import Flask, render_template, request, redirect, flash
from email.message import EmailMessage
import smtplib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 管理者のメール設定
ADMIN_EMAIL = "numanomutsuki@gmail.com"
EMAIL_PASSWORD = "kexh dbyy bxpi vinl"

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            msg = EmailMessage()
            msg['Subject'] = f'【お問い合わせ】'
            msg['From'] = email
            msg['To'] = ADMIN_EMAIL
            msg.set_content(f"Name: {name}\nEmail: {email}\n{message}")

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(ADMIN_EMAIL, EMAIL_PASSWORD)
                smtp.send_message(msg)

            flash('送信ありがとうございます！')
        except Exception as e:
            flash(f'送信エラー: {e}')

        return redirect('/')

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)