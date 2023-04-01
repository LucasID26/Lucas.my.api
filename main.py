from flask import Flask, render_template
from threading import Thread
file = "home.html"

app = Flask(__name__)


@app.route('/')
def home():
    return "OOHH HAYY"

@app.route('/profile')
def profile():
    return """
<!DOCTYPE html>
<html>
<head>
	<title>My Profile</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		body {
			background: url('https://i.pinimg.com/originals/26/82/03/268203daaaec11ae176d5b51016166a3.gif') no-repeat center center fixed;
			background-size: cover;
			margin: 0;
			padding: 0;
			height: 100vh;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
			color: white;
			font-family: Verdana, sans-serif;
			text-align: center;
		}

		.head {
			text-align: center;
			margin-top: 10px;
		}

		.head h1 {
			margin-top: 10px;
			margin-bottom: 5px;
			font-size: 26px;
		}

		.head img {
			width: 70px;
			border-radius: 50%;
			margin-top: 10px;
			margin-bottom: 5px;
		}

		.head p {
			margin-top: 0px;
			font-size: 16px;
			font-weight: bold;
		}

		.sosial-media {
			display: flex;
			flex-direction: row;
			justify-content: center;
			align-items: center;
			margin-top: 10px;
		}

		.sosial-media img {
			width: 22px;
			margin: 0 3px;
			border-radius: 50%;
		}

		.deskripsi {
			margin-top: 30px;
			text-align: center;
		}

		.deskripsi h2 {
			margin-bottom: 10px;
			font-size: 20px;
		}

		.deskripsi p {
			font-size: 14px;
		}
	</style>
</head>
<body>
	<div class="head">
		<h1>My Profile</h1>
		<img src="https://dl.yasir.pro/download/CB9TH/Abstract%20Gamer%20Head%20Free%20Esport%20Logo.png" alt="LUCAS">
		<p>LUCAS ID</p>
	</div>
	<div class="sosial-media">
		<a href="https://t.me/LucasBukanKalengSarden">
			<img src="https://w7.pngwing.com/pngs/419/837/png-transparent-telegram-icon-telegram-logo-computer-icons-telegram-blue-angle-triangle-thumbnail.png" alt="Telegram">
		</a>
		<a href="https://www.instagram.com/Yoi_267/">
			<img src="https://w7.pngwing.com/pngs/191/478/png-transparent-social-media-facebook-emoji-icon-instagram-icon-instagram-logo-text-rectangle-magenta-thumbnail.png" alt="Instagram">
		</a>
	</div>
	<div class="deskripsi">
		<h2>Deskripsi</h2>
		<p>Saya adalah seorang developer yang berfokus pada desain bot telegram. Saya tidak memiliki pengalaman dan ini sekedar hobby.</p>
	</div>
</body>
</html>


"""


def run_flask():
  app.run(host="0.0.0.0",port=8080)

def run_thread():
  Thread(target=run_flask).start()


run_thread()
#if __name__ == '__name__':
  
