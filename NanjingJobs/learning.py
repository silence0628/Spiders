#coding:utf-8
"""
    BeautifulSoup方法学习
"""

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')


print(soup.find(name='ul'))
print('*'*40)
print(soup.find_all(name='ul'))
print('*'*40)
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))
