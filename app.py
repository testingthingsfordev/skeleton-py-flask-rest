from api.api import create_api

api = create_api()

if __name__ == '__main__':
    api.app.run(host="0.0.0.0", debug=True)
