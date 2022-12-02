# 单元测试
单元测试（模块测试，Unit testing）,测试程序的正确程度。

## 单元测试及其与功能测试的区别
二者有个大概的区别：功能测试站在用户的角度从外部测试应用，单元测试则站在程序员的角度从内部测试应用。

本项目遵循的TDD方法使用这两种类型测试应用。
-   写功能测试，从用户的角度描述应用的新功能。
-   功能测试失败后，想办法编写代码让它通过（或者说至少让当前失败的测试通过）。
    -   使用单元测试验证效果
-   单元测试失效后，编写最少量的应用代码，刚好让单元测试通过。指导功能测试有了进展
-   然后验证功能测试。这一步可能促进我们编写新的单元测试和代码等。

从这个过程中，功能测试站在高层驱动开发，而单元测试则从底层驱动我们做啥。

## 经验
```Django
Django: OperationalError No Such Table
```
```Django
# 这里我的是Class Meta字段一定要设置好
# 否则就会报错
class Fig4C(models.Model):
    metabolite = models.TextField(blank=True, primary_key=True)
    group1 = models.FloatField(db_column='Group1', blank=True, null=True)  # Field name made lowercase.
    group2 = models.FloatField(db_column='Group2', blank=True, null=True)  # Field name made lowercase.
    group3 = models.TextField(db_column='Group3', blank=True, null=True)  # Field name made lowercase.
    group4 = models.FloatField(db_column='Group4', blank=True, null=True)  # Field name made lowercase.
    group5 = models.FloatField(db_column='Group5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        # app_label = "teatree"
        db_table = 'Fig4c'

```

### Django Meta字段 || managed

由于Django会自动根据模型类生成映射的数据库表，如果你不希望Django这么做，可以把managed的值设置为False。

默认值为True,这个选项为True时Django可以对数据库表进行 migrate或migrations、删除等操作。在这个时间Django将管理数据库中表的生命周期

如果为False的时候，不会对数据库表进行创建、删除等操作。可以用于现有表、数据库视图等，其他操作是一样的。


## Python测试相关库
-   unittest,内置库，模仿PyUnit写的，简单易用，
-   nose,测试发现，发现并运行测试
-   pytest,基于unittest的封装，写起来更方便
-   mock，替换掉网络调用或者rpc请求等


## selenium测试页面
pass

## pytest 测试页面
pass

## Javascript 测试页面
有很多工具:jsUnit、Qunit、Mocha、Chutzpath、Karma、Testacular、Jasmine等。
选择其中一个工具后，还得选择一个断言框架和报告程序，或许还要选择一个模拟技术库。
试试Qunit,它足够简单，跟Python单元测试很像，而且能很好地和jQuery配合使用。


## references

>Test-Driven Development with Python,2nd edition, by Harry Percival (O'Reilly). Copyright 2017 Harry Percival, 978-1-491-95870-4.

>[自动化测试简介](https://docs.djangoproject.com/zh-hans/4.1/intro/tutorial05/)

>[单元测试](https://zhuanlan.zhihu.com/p/29968920)

>[Test-Driven Web Development With Python, the book.](https://github.com/hjwp/Book-TDD-Web-Dev-Python)

>[编写并运行测试](https://docs.djangoproject.com/zh-hans/4.1/topics/testing/overview/)

>[ 单元测试--django单元测试 ](https://www.cnblogs.com/yycnblog/p/13836926.html)

>[编写 Django 应用单元测试 ](https://zhuanlan.zhihu.com/p/108049398)

>[Django 项目单元测试的几个套路: 统计代码覆盖率](https://zhuanlan.zhihu.com/p/44402618)

>[Django 教程 10: 测试 Django 网页应用](https://developer.mozilla.org/zh-CN/docs/learn/Server-side/Django/Testing)

>[how-should-i-test-a-database-driven-django-cms-for-404-errors](https://stackoverflow.com/questions/43876310/how-should-i-test-a-database-driven-django-cms-for-404-errors)

>[An Overview of SNP Genotyping Technologies](https://www.cd-genomics.com/an-overview-of-snp-genotyping-technologies.html)

>[selenium常见问题 ](https://blog.csdn.net/sin_404/article/details/102720066)

>[qunitjs ](https://qunitjs.com/)
