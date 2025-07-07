#names = ['Christopher', 'Susan']
#scores = []
#scores.append(98)
#scores.append(99)
#print(names)
#print(scores)
#print(scores[1])

#names = ['Susan', 'Christopher']
#print(len(names))
#names.insert(0, 'Bill')
#print(names)
#names.sort()
#print(names)

#names = ['Susan', 'Christopher', 'Bill', 'Justin']
#presenters = names[1:3]
#print(names)
#print(presenters)

#print('-------------------------')

#from array import array
#scores = array('d')
#scores.append(97)
#scores.append(98)
#print(scores)
#print(scores[1])

#print('-------------------------')

#person = {'first' : 'Christopher'}
#person['last'] = 'Harrison'
#print(person)
#print(person['first'])


# def main():
#    colors = ['yellow', 'red', 'green', 'yellow','blue']
#    length = len(colors)
#    print(f'Number of elements: {length}')
#    print(colors[2])
#    colors[3] = 'purple'
#    print(colors)
#if __name__ == '__main__':
#    main()

# def main():
#    fabrics = []
#    fabrics.append('velvet')
#    fabrics.append('denim')
#    fabrics.append('gingham')
#    fabrics.insert(0, 'chiffon')
#    print(fabrics)
#    if 'gingham' in fabrics:
#        print('gingham is in the list.')
#    else:
#        print('gingham is NOT in the list.')
#    i = fabrics.index('velvet')
#    fabrics[i] = 'taffeta'
#    fabrics.pop()
#    fabrics.remove('denim')
#    n = len(fabrics)
#    print(f'The fabrics list contains {n} elements.')
#    print(fabrics)
#if __name__ == '__main__':
#    main()

# def main():
#    YEAR_PLANTED_INDEX = 0
#    HEIGHT_INDEX = 1
#    GIRTH_INDEX = 2
#    FRUIT_AMOUNT_INDEX = 3
#    apple_tree_data = [
#        [2012, 2.7, 3.6, 70.5],
#        [2012, 2.4, 3.7, 81.3],
#        [2015, 2.3, 3.6, 62.7],
#        [2016, 2.1, 2.7, 42.1]
#    ]
#    one_tree = apple_tree_data[2]
#    height = one_tree[HEIGHT_INDEX]
#    print(f"height: {height}")
#if __name__ == "__main__":
#    main()

# def main():
#    x = 17
#    y = x
#    print(f"Before changing x: x {x}  y {y}")
#    x += 1
#    print(f"After changing x:  x {x}  y {y}")
#if __name__ == "__main__":
#    main()

# def main():
#    lx = [7, -2]
#    ly = lx
#    print(f"Before changing lx: lx {lx}  ly {ly}")
#    lx.append(5)
#    print(f"After changing lx:  lx {lx}  ly {ly}")
#if __name__ == "__main__":
#    main()

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")
    modify_args(x, lx)
    print(f"After calling modify_args():  x {x}  lx {lx}")
def modify_args(n, alist):
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")
    n += 1
    alist.append(4)
    print(f"   After changing n and alist:  n {n}  alist {alist}")
if __name__ == "__main__":
    main()