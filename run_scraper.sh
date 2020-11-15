if [ ! -f '.auth' ]; then
    echo ".auth file not found! Please follow steps to make one."
    exit 1
fi
source .auth
python3 scraper.py