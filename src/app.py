from config.args import get_arguments
from handler import app

if __name__ == '__main__':
    args = get_arguments() 
    app.run(debug=args.environment == "dev", host='0.0.0.0', port=args.port)
