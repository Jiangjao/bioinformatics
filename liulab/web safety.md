# 主要是安全防护
## CSS (Crosss-site scripting, XSS)
代码注入的一种。用户登陆并访问页面，利用网页开发时留下的漏洞，通过特殊的方法注入指令到网页，使特殊的用户加载并执行这种程序。通常这种程序是JavaScript编写的，可以获取较高的权限和内容。
    使用自带的特殊函数(render)，或者通用视图，会将所有的HTML转义，所有的自带的脚本不会执行
    如果需要执行，可以用弱函数转义...

## CSRF 跨站请求伪造和SQL注入攻击
-   Cross-site request forgery, also known as one-click attack or session riding and abbreviated as CSRF or XSRF.
-   恶意攻击者在用户不知情的情况下，使用用户的身份来操作

-   hacker schedule..
    -   创建一个请求A类的URL的Web页面，放在恶意网站B中，这个文件包含了一个创建用户的表单。这个表单加载完毕就会立即进行提交。
    -   黑客创建一个请求网站A类的URL的Web页面，放在恶意网站B中，这个文件包含了一个创建用户的表单。这个表单加载完毕就会立即进行提交。比如：获取cookie
    -   黑客把这个Web页面的URL发送至超级管理员，诱导超级管理员打开这个Web页面
    -   解决：服务端设置token
-   SQL注入漏洞：用户直接对网站数据库执行任意的SQL语句，在无需用户权限的情况下即可对数据访问、修改和删除
-   Django的ORM系统自动规避了SQL注入攻击
-   注意使用原始的SQL语句，切记避免拼接字符串
 ```Django
 <!-- 变量绑定的 -->
 <!--  -->
    name_map = {'first': 'first_name', 'last':'last_name', 'bd': 'birth_date'}
    Person.objects.raw('SELECT * FROM employee',
    translations=name_map)
 ```
## 引用
>[Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)

>[Cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery)

>[SQL injection](https://en.wikipedia.org/wiki/SQL_injection)