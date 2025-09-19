# 查询集QuerySet

- Django的ORM中存在查询集的概念

- 查询集，也称为查询结果集，QuerySet, 表示从数据库中获取的对象集合

- 当调用如下过滤器方法时，Django会返回查询集(而不是简单的列表)

  - all()

    - 返回所有的数据

  - filter()

    - 返回满足条件的数据

  - exclude()

    - 返回满足条件之外的数据

  - order_by()

    - 返回对结果进行排序

      

- 判断某一个查询集中是否有数据

  - exists()

  - 

    ```
    people.exists()
    ```

    

- 两大特性
  - 惰性执行
    - 结合迭代、序列化
    - if
  - 缓存

- 限制查询集

  - 可以对查询集进行取下标或者是切片操作，等同于sql中的limit和offset子句
  - 注意：不支持负数 索引
  - books = BookInfo.objects.all()[0:2]

- 分页
  - 

  - ```
    # 查询数据- 
    book = BookInfo.objects.all()
    # 导入分页类
    from django.core.paginator import Paginator(分页类)
    # 创建分页实例
    paginator=Paginator(books,2)
    # 获取指定页码的数据
    page_skus = paginator.page(1) 
    # 获取分页数据
    total_page =paginator.num_pages 
    ```

  - https://docs.djangoproject.com/en/1.11/topics/pagination/
    