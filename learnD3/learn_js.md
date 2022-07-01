## 解答题

-   描述js所有声明变量的方式和优缺点
    -   ECMASscipt2015 作用域不同
    -   let     block field
    -   const   block field 不过声明变量时得赋值
    -   var     globla-like field
-   描述闭包
    -   闭包可以保存一种状态，存储函数，变量等等，可以放在当前的上下文中, 可以使用
    -   函数嵌套函数

    -   函数内部可以引用函数外部的参数和变量

    -   参数和变量不会被垃圾回收机制回收
        -   闭包是指有权访问另一个函数作用域中的变量的函数。JavaScript高级程序设计（第3版）中
    -   [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming))
-   说明所有js类型转换成的布尔值是？

| 数据类型 | 转换成true | 转换成false |
| :------| ------: | :------: |
| Boolean | true | false |
| String | 非空字符串 | ""(空字符串) |
| Number | 非零整数（包括无穷值） | 0、NaN |
| Object | 任意对象 | null |
| Undefined | N/A(不存在) | undefined |

>JavaScript高级程序设计（第3版）中

-   数组的浅拷贝方法？
    -   In JavaScript, all standard built-in object-copy operations (spread syntax, 
    -   Array.prototype.concat(),
    -    Array.prototype.slice(), 
    -    Array.from(), 

    -    create shallow copies rather than deep copies.


-   对象的浅拷贝方法？
    -    Object.assign(), 
    -    Object.create()) 

>[浅拷贝](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)

-   宏任务和微任务

    与task-queue有关，每个task 都有个生命
    好像有个调度算法，


    -   run the oldest task in macrotask queue,then remove it.
    -   run all available tasks in microtask queue,then remove them.
    -   next round:run next task in macrotask queue(jump step 2)

宏任务包括键盘事件、鼠标事件、定时器事件、网络事件、Html解析、改变Url etc。宏任务代表一些离散和独立的工作。

微任务是更新应用程序状态的较小任务，应该在浏览器继续执行其他任务（例如重新渲染 UI）之前执行。微任务包括承诺回调和 DOM 突变更改。微任务使我们能够在重新渲染 UI 之前执行某些操作，从而避免可能显示不一致的应用程序状态的不必要的 UI 渲染。

>[宏任务和微任务](https://promisesaplus.com/#notes)
>[task-queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue)
>[query about task](https://stackoverflow.com/questions/25915634/difference-between-microtask-and-macrotask-within-an-event-loop-context)

-   基本类型和引用类型的值？
JavaScript types
The set of types in the JavaScript language consists of primitive values and objects.

-   Primitive values (immutable datum represented directly at the lowest level of the language)
    -   Boolean type
    -   Null type
    -   Undefined type
    -   Number type
    -   BigInt type
    -   String type
    -   Symbol type
Objects (collections of properties)
    -   Object 
    -    Array 
    -     Function 等
    -    class?