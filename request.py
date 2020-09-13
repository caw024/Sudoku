import requests

def main():
    res = requests.get("http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&?level=3")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    print(res.json())

main()