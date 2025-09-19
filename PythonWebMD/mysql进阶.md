# mysql进阶

```
# 创建部门表
create table dept
(
    id   tinyint primary key auto_increment not null,
    name varchar(255)
);

# 创建员工表
create table emp
(
    id      tinyint primary key auto_increment not null,
    name    varchar(255),
    dept_id tinyint
);

insert into emp
values (0, '曹冲', 1),
       (0, '曹丕', 1),
       (0, '曹植', 1),
       (0, '曹操', 1),
       (0, '张角', 2),
       (0, '张宝', 2),
       (0, '张梁', 2),
       (0, '刘备', 3),
       (0, '关羽', 3),
       (0, '张飞', 3),
       (0, '孙权', 0);

insert into dept
values (0, '人力资源部'),
       (0, '财务部'),
       (0, '后勤部'),
       (0, '法务部');


select *
from emp e
         join dept d;

# 多表关联的sql 分为四步： 1.确定要连接的表；2.确定要查询的字段 3.确定连接方式 4.确定关联条件
# 内连接 -- from 表1 [inner]join 表2 on 连接条件 where 过滤条件
# 内连接是应用最广泛的一种连接查询，其本质就是根据条件筛选出有意义的数据

select e.name, d.name
from emp e
         join dept d on e.dept_id = d.id;
# 等值连接 条件是等量关系 ,=符号，表示相等关系
select *
from dept as d
         inner join emp as e on e.dept_id = d.id;

# 查询部门id 大于2的员工、部门信息
select d.id, e.name, d.name
from dept d
         inner join emp e on e.dept_id = d.id
where d.id > 2;

# 非等值连接 条件是非等量关系， between.. and ..关键字 表示某个范围
create table salary
(
    id    tinyint primary key auto_increment not null,
    losat tinyint,
    hisat tinyint
);
insert into salary
values (0, 700, 1200),
       (0, 1201, 1400),
       (0, 1401, 2000),
       (0, 2001, 3000),
       (0, 3001, 99999);
alter table salary
    modify hisat int;

select *
from salary;
alter table emp
    add sal int not null;

update emp
set emp.sal = null;

update emp
set sal = CASE id
              when 5 then 2450
              when 6 then 800
              when 7 then 5000
              when 8 then 2975
              when 9 then 1250
              when 10 then 2850
              when 11 then 2000
    end
where id in (5, 6, 7, 8, 9, 10, 11);
;

# 查询员工表中的最低工资和最高工资 查询工资等级
select * from emp e inner join salary s on e.sal between s.losat and s.hisat;

# 查询员工工资大于3000的工资等级
select e.name, e.sal , s.id from emp e inner join salary s on e.sal
between s.losat and s.hisat
where e.sal>3000;

# 自连接
# 一张表看作两张表，自己连接自己
# from 表1 as a [连接形式] join 表1 as b on a.xx字段 = b.xx字段

alter table emp add leader_id tinyint;
update emp set leader_id =
    case id when 1 then 5 when 2 then 4
        when 3 then 11
        when 4 then 4
        when 5 then 3
        when 6 then 2
        when 7 then 2
        when 8 then 7
        when 9 then 7
        when 10 then 7
        when 11 then 5

        end where id in (1,2,3,4,5,6,7,8,9,10,11);

# 每个员工对应的上级领导
# select e1.name, e2.name from emp e1 inner join emp e2 on e1.leader_id = e2.id;
# select * from emp e1 inner join emp e2 on e1.dept_id = e2.id where e1.dept_id > 2;

# 外连接查询

#  在内连接查询时，返回的查询结果集中仅仅是符合查询条件和连接的行
# 有的时候需要包含没有关联的行中的数据，即返回的查询结果集中不仅需要包含符合连接条件的行，还需要包含左表(左连接或c)
# 右表(右连接或右外连接)或者两个连接表(全外连接)中的所有行

# 左外连接 ： 返回包括左表中的所有记录和右表中连接字段相等的记录
# 左连接 left 关键字 from 表1 left join 表2 on 连接条件 where 过滤条件
#  左连接 left 关键字 前面的表为主表
# 查询所有员工的部门

select * from emp;
select * from dept;

select e.id as id, e.name as name, e.sal as sal, d.name as dept_name from emp e left join dept d on e.dept_id = d.id;



# 右外连接: 返回包括右表中的所有记录和左表中连接字段相等的记录
# 右连接 right 关键字
#  右连接 right 关键字 后面的表为主表

# 查询部门所对应的员工
select * from emp e right join dept d on e.dept_id = d.id;
```

