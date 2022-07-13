## 解答题 02
-   描述js所有声明变量的方式和优缺点
-   描述闭包
-   说明所有js类型转换成的布尔值是？
-   数组的浅拷贝方法有
-   对象的浅拷贝方法有
-   宏任务和微任务

见
>[learn_js](./learn_js.md)

update:
-   基本类型和引用类型的值

## 其他小练习
```javascript
// 补充getColor函数内容，调用getColor函数获取返回随机十六进制颜色
function getColor () {
    let color
    //
    color = "#"
    // get random colorbase(16-base)
    for(let i = 0; i < 6; i ++) {
        // 获取0-15并通过toString转16进制
        color += Math.floor(Math.random()*16).toString(16);
    }
    // let colorBase01 = Math.floor(Math.random()*255).toString(16)
    // let colorBase02 = Math.floor(Math.random()*255).toString(16)
    // let colorBase03 = Math.floor(Math.random()*255).toString(16)
    // color += colorBase01 + colorBase02 + colorBase03
    // console.log(color)
    return color
}
let colorValue = getColor();
```