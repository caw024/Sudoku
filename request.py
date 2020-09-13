import requests

def main():
    res = requests.get("http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&?level=3")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    print(res.json())

    puzzle = [['_']*9 for _ in range(9)]
    
    for l in res.json()['squares']:
        puzzle[l['x']][l['y']] = l['value']
    
    print(puzzle)

main()