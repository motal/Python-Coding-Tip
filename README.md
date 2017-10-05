# Python Coding Tip

## 1. Basic

#### What is Python?
```python
import this
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

#### Data types
- int, float, str, obj

#### Data structures
- list, tuple, set, dict
###### dict
```python
dict = {'a': 100, 'b': 200}
dict['c'] = 300
for key in dict:
    print(key, dict[key])

for value in dict.values():
    print(value)

for item in dict.items():
    print(item)
```
```
OUTPUT:
a 100
b 200
c 300
100
200
300
('a', 100)
('b', 200)
('c', 300)
```
###### set
```python
set1 = set()
set1.add('a')
set1.add('a')
set1.add('b')
print(set1)

set2 = {'a', 'b', 'c', 'd', 'e'}
set2.remove('e')
print(set2)

if 'a' in set2:
    print('YES')

print(set1.union(set2))
print(set2.intersection(set1))
print(set2.difference(set1))
```
```
OUTPUT:
{'a', 'b'}
{'a', 'd', 'b', 'c'}
YES
{'a', 'b', 'c', 'd'}
{'a', 'b'}
{'d', 'c'}
```
#### Special
How to use '*' and '**'?
```python
def get_names(*args, **kwargs):
    # args is tuple
    # kwargs is dict
    for n in args:
        print(n)
    for n in kwargs:
        print(n, kwargs[n])

#get_names('aa', 'bb', name='kim', age=33)
# same as above
get_names(*['aa', 'bb'], **{'name': 'kim', 'age': 33})
```

## 2. Standard libraries
#### collections
###### Counter - It is very useful when counting something. Instead of dictionary<obj, int>, use this.
```python
cnt = Counter()
for n in ['a','a','b','c']:
  cnt[n] += 1
print(cnt)

cnt2 = Counter('cccaab')
print(cnt2)
```
```
OUTPUT:
Counter({'a': 2, 'b': 1, 'c': 1})
Counter({'a': 2, 'b': 1, 'c': 3})
```
## 3. External libraries

## 4. Virtual environment
```
> python3 -m venv /my-venv/
> source /my-venv/bin/activate
```

## 5. Useful tools
#### iPython
- https://ipython.org/
#### httpie
- https://httpie.org/
