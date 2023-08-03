from flask import Flask
import argparse
import os

from BrowseFile.BrowseFile import browse_file_blueprint

app = Flask(__name__)
app.register_blueprint(browse_file_blueprint)

parser = argparse.ArgumentParser()

@app.route("/")
def index():
    return "<h1>Hello, world</h1>"

def main():
    parser.add_argument("-d", "--dir", default=os.getcwd(), help="要访问的根目录")
    args = parser.parse_args()
    print (args)
    app.config['ROOT_PATH'] = args.dir

    app.run(host="0.0.0.0", port="3399", debug=True)

if __name__ == "__main__":
    main()