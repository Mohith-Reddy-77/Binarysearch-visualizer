from flask import Flask, render_template, request

app = Flask(__name__)

def binary_search_algorithm(array, target):
    indexlist = []
    i=[]
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        indexlist.append(mid)  
        i.append(array[left:right+1])
        if array[mid] == target:
            return mid, indexlist, i
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, indexlist, i

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    array_str = request.form['array']
    target = int(request.form['target'])

    array = [int(num.strip()) for num in array_str.split(',')]

    index, indexlist, i = binary_search_algorithm(array, target)

    data = {
        'array': array,
        'target': target,
        'indexlist': indexlist,
        'mid': index,  
        'newarray': i,
        'len': len(indexlist)  
    }

    return render_template('index.html', data=data)
