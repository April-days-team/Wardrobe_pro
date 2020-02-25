-- 系统管理员【超级管理员，中级管理员，普通管理员,合作商管理员】
-- 合作商管理员【关联着系统管理员，】
-- 超级管理员【所有权限，包括中级管理员，普通管理员，通过中级，普通方表设置外键，关联超级管理员表】
-- 中级管理员【包括所有普通管理员权限，管理所有普通管理员】
-- 普通管理员【商品管理员[包含商品所有表]，购物车管理员[购物车表，购物车订单，购物车订单详情]，用户管理员，会员管理员,订单管理员[所有订单],导购管理员[导购订单，导购相关的],服务管理员】


# 系统管理员角色
create table sys_manager_role(
    id integer primary key auto_increment,
    name varchar(20) not null unique,
    code varchar(5)
);

insert into sys_manager_role(username,code) values
    ('超级管理员','super_admin'),
    ('中级管理员','middle_admin'),
    ('普通管理员','ordinary_admin'),
    ('合作商超级管理员','cooperation_admin');


# 创建系统管理员
create table sys_manager_user(
    id integer primary key AUTO_INCREMENT,
    username varchar(20) unique not null ,
    auth_string varchar(32) not null , -- 密码
    nick_name varchar(20),  -- 别名
    role_id integer  references sys_manager_role(id)   -- 角色ID
);

# 系统管理员角色
insert into sys_manager_user(username,auth_string,nick_name,role_id) values
    ('员旭','cdc4fb0718449da1a0eebf2ec745e76a','旭哥哥',1);


-- 不同角色自己的菜单列表
create table sys_role_menu(
    id integer primary key auto_increment,
    name varchar(20),
    parent_id integer references sys_role_menu(id), -- 自引用，父菜单
    ord int comment '菜单显示的排序',
    url varchar(50) comment '菜单的链接'
);

# 系统角色和菜单的关系表
create table trans_sys_role_menu(
    id integer primary key auto_increment,
    role_id integer references sys_manager_role(id),
    menu_id integer references sys_role_menu(id)
);

# 创建合作商管理员表
create table cooperation_admin(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    sys_id integer references sys_manager_user(id)
);

insert into cooperation_admin(name,auth_string,nick_name) values
    ('淘宝管理员','ba6a76245259d9fcc3c3b926d9afb1f2','淘淘');

-- 以上为系统管理员相关表

-- 超级管理员,关联着系统管理员
create table super_admin(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    sys_id integer references sys_manager_user(id)
);

# 超级管理员表中插入数据
insert into super_admin(name,auth_string,nick_name) values
    ('员旭','ba6a76245259d9fcc3c3b926d9afb1f2','旭哥哥');


-- 中级管理员，关联着超级管理员
create table middle_admin(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    super_id integer references super_admin(id)
);

insert into middle_admin(name,auth_string,nick_name) values
    ('员旭','ba6a76245259d9fcc3c3b926d9afb1f2','旭哥哥');


-- 普通管理员角色表
create table ordinary_admin_role(
    id integer primary key auto_increment,
    name varchar(30) not null,
    code varchar(5)
);

-- 普通管理员添加角色
insert into ordinary_admin_role(username,code) values
    ('用户管理员',1),
    ('订单管理员',2),
    ('会员管理员',3),
    ('商品管理员',4),
    ('购物车管理员',5),
    ('导购管理员',6),
    ('服务管理员',7);

# 1.用户管理员
create table user_manager(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    ordinary_id integer references ordinary_admin_role(id)
);

# 2.订单管理员
create table order_manager(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    ordinary_id integer references ordinary_admin_role(id)
);
# 3.会员管理员
create table member_manager(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    ordinary_id integer references ordinary_admin_role(id)
);
# 4.商品管理员
create table product_manager(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    ordinary_id integer references ordinary_admin_role(id)
);
# 5.购物车管理员
create table cart_manager(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    ordinary_id integer references ordinary_admin_role(id)
);
# 6.导购管理员
create table daogou_manager(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    ordinary_id integer references ordinary_admin_role(id)
);
# 7.服务管理员
create table server_manager(
    id integer primary key auto_increment,
    name varchar(30) not null,
    auth_string varchar(50),  -- 密码
    nick_name varchar(20),  -- 别名
    ordinary_id integer references ordinary_admin_role(id)
);







