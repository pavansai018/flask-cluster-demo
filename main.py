from flask import Flask

# template_folder points to current directory. Flask will look for '/static/'
app = Flask(__name__)
# The rest of your file here

@app.route('/')
def index():
  
 
    return 'Hello World'
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)