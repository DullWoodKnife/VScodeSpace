# F和Q对象

- F对象

  - 两个属性比较

  - 例

    - ```
      查询阅读量大于等于评论量的图书
      BookInfo.objects.filter(readcount__gt=F('commentcount'))
      ```

  - 可以在F对象上使用算数运算

  - 例2

    - ```
      查询阅读量大于2倍评论量的图书
      
      BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
      ```

      

  - 例3

  - 日期

    - year\month\day\week_day\hour\minute\second

    - 查询1980年发表的图书

      - ```
        BookInfo.objects.filter(pub_date__year=1980) 
        ```

    - 查询1990年1月1日发后表的图书

      ```
      BookInfo.objects.filter(pub_date__gt='1990-1-1') 
      ```

- Q对象

  - 多个过滤器逐个调用表示逻辑与关系,同sql语句中where部分的and关键字

    - 例

      - ```
        查询阅读量大于20，并且编号小于3的图书
        >>> BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3) 
        <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
        >>> BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3).filter(commentcount__gt=200) 
        <QuerySet [<BookInfo: 射雕英雄传>]>
        
        ```

        

  - Q(属性名__运算符=值)

    - 例

      - ```
        查询阅读量大于20的图书，改写成Q对象
        >>> from django.db.models import Q                                                          
        >>> BookInfo.objects.filter(Q(readcount__gt=20))
        <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>
        
         BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3)) 
        
        ```

    - |

      - 链接
      - 逻辑或

    - &

      - 逻辑与

    - ~

      - 非not

        - ```
          查询编号不等于3的图书
          
           BookInfo.objects.filter(~Q(id=3))
          ```

  - 聚合函数和排序函数

    - 聚合函数

      - ​	使用aggregate()过滤器调用聚合函数

        - avg 平均

        - count 数量

        - max 最大

        - min 最小

        - sum 求和

          - ```
            查询图书的总阅读量
            from django.db.models import Sum
            >>> BookInfo.objects.aggregate(Sum('readcount')) 
            {'readcount__sum': 214}
            查询图书的总数
            
            >>> BookInfo.objects.count()
            4
            
            ```

            

      - count 一般不适用aggregate()过滤器

    - 排序

      - 使用order_by对结果进行排序

      - 默认升序

      - 降序

        - ```
          BookInfo.objects.all().order_by('-readcount') 
          ```

          