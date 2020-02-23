#!/usr/bin/python
# **coding:utf-8**

# reload(sys)
# sys.setdefaultencoding('utf8')
#
# table = PrettyTable(['编号','云编号','名称','IP地址'])
# table.add_row(['1','server01','服务器01','172.16.0.1'])
# table.add_row(['2','server02','服务器02','172.16.0.2'])
# table.add_row(['3','server03','服务器03','172.16.0.3'])
# table.add_row(['4','server04','服务器04','172.16.0.4'])
# table.add_row(['5','server05','服务器05','172.16.0.5'])
# table.add_row(['6','server06','服务器06','172.16.0.6'])
# table.add_row(['7','server07','服务器07','172.16.0.7'])
# table.add_row(['8','server08','服务器08','172.16.0.8'])
# table.add_row(['9','server09','服务器09','172.16.0.9'])
# print(table)


from prettytable import from_html

html_string = '''<table>
<tr>
<th>code</th>
<th>uuid</th>
<th>name</th>
<th>IP</th>
</tr>
<tr>
<td>1</td>
<td>server01</td>
<td>server-01</td>
<td>192.168.100.1</td>
</tr>
<tr>
<td>2</td>
<td>server02</td>
<td>server-02</td>
<td>192.168.100.2</td>
</tr>
</table>'''

table = from_html(html_string)

print(table[0])
