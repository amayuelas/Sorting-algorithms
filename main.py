from bubbleSort import *

def main():
    """
    It creates an example list of businesses with different id's and
    its rate in recommendation system. It will call BubbleSort and print the result
    """
    business1 = {'id':1, 'rating':3}
    business2 = {'id':2, 'rating':1}
    business3 = {'id':3, 'rating':5}
    business4 = {'id':4, 'rating':5}
    business5 = {'id':5, 'rating':1}

    businesses = [business1, business2, business3, business4, business5]

    print bubbleSort(businesses)

if __name__ == '__main__':
    main()
