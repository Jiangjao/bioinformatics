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
    Variables that are assigned a non-primitive value are given a reference to that value. That reference points to the object’s location in memory. The variables don’t actually contain the value.
    -   按值传递(call by value)是最常用的求值策略：函数的形参是被调用时所传实参的副本。修改形参的值并不会影响实参。
    -   按引用传递(call by reference)时，函数的形参接收实参的隐式引用，而不再是副本。这意味着函数形参的值如果被修改，实参也会被修改。同时两者指向相同的值。
    -   传共享传递(call by sharing)，函数接收的是对象引用的拷贝（the copy of the reference to object）。这个引用拷贝与形参相关联，并且是它的值。这里既不是按值传递的对象副本，也不是按引用传递的隐式引用。

-   js有call by sharing的效果，传递的是可object这种类型，可sharing的，
    -   第二个是函数变量的作用域
    -   从例子推导出来的，没有验证
>[Evaluation_strategy](https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_sharing)

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
        // then concat all to color
        color += Math.floor(Math.random() * 16).toString(16);
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