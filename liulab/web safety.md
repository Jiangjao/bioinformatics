# 主要是安全防护
## CSS (Crosss-site scripting, XSS)
代码注入的一种。用户登陆并访问页面，利用网页开发时留下的漏洞，通过特殊的方法注入指令到网页，使特殊的用户加载并执行这种程序。通常这种程序是JavaScript编写的，可以获取较高的权限和内容。
    使用自带的特殊函数(render)，或者通用视图，会将所有的HTML转义，所有的自带的脚本不会执行
    如果需要执行，可以用弱函数转义...

## CSRF 跨站请求伪造和SQL注入攻击

## 引用
>[Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)