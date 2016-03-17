from rec_app.models import Category

CATEGORIES_PATH = "../resources/clean_categories.txt"

def load_data(path):
    #opening file trainingData at path given
    with open(path, 'r') as trainingData:
        #iterating over each line in trainingData
        for line in trainingData:
            t=t+1
            line.rstrip()
            line = map(int, line.split())
            end = line[0]
            Y.append(end)
            X.append(line[1:])
    return t


def create_category(name):


def create_categories()