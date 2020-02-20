/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/2/20 0:00:38                            */
/*==============================================================*/


alter table coupons_types
   drop primary key;

drop table if exists coupons_types;

alter table d_boss
   drop primary key;

drop table if exists d_boss;

drop table if exists d_fans;

drop table if exists d_member;

alter table d_order_form
   drop primary key;

drop table if exists d_order_form;

drop table if exists d_performance;

drop table if exists d_shop;

drop table if exists d_worker_order;

alter table gl_boss
   drop primary key;

drop table if exists gl_boss;

drop table if exists gl_jurisdiction;

alter table member_info
   drop primary key;

drop table if exists member_info;

drop table if exists member_level;

drop table if exists member_score;

drop table if exists pro_classify;

drop table if exists pro_details;

drop table if exists pro_tags;

alter table products
   drop primary key;

drop table if exists products;

alter table serv_appearance
   drop primary key;

drop table if exists serv_appearance;

alter table serv_costmize
   drop primary key;

drop table if exists serv_costmize;

drop table if exists serv_shopping_company;

drop table if exists serv_store_query;

drop table if exists serv_wardrobe;

alter table service
   drop primary key;

drop table if exists service;

drop table if exists t_adress;

drop table if exists t_carts;

alter table t_order
   drop primary key;

drop table if exists t_order;

drop table if exists t_orderdetails;

alter table t_ship
   drop primary key;

drop table if exists t_ship;

alter table user
   drop primary key;

drop table if exists user;

alter table user_collect_store
   drop primary key;

drop table if exists user_collect_store;

alter table user_coupon
   drop primary key;

drop table if exists user_coupon;

drop table if exists user_message;

alter table user_order
   drop primary key;

drop table if exists user_order;

alter table user_recharge
   drop primary key;

drop table if exists user_recharge;

drop table if exists user_track;

alter table user_transaction
   drop primary key;

drop table if exists user_transaction;

/*==============================================================*/
/* Table: coupons_types                                         */
/*==============================================================*/
create table coupons_types    优惠券种类表
(
   coupon_id            integer not null,
   coupon_1             varchar(50),
   coupon_2             varchar(50),
   coupon_3             varchar(50)
);

alter table coupons_types
   add primary key (coupon_id);

/*==============================================================*/
/* Table: d_boss                                                */
/*==============================================================*/
create table d_boss    # 导购
(
   d_id                 INTEGER not null auto_increment,
   user_id              integer,
   dz_name              VARCHAR(50) not null,
   is_no                bool not null
);

alter table d_boss
   add primary key (d_id);

/*==============================================================*/
/* Table: d_fans                                                */
/*==============================================================*/
create table d_fans   # 导购粉丝表
(
   d_id                 INTEGER,
   fans_id              INTEGER not null,
   fans_name            VARCHAR(50) not null,
   fans_num             INTEGER not null
);

/*==============================================================*/
/* Table: d_member                                              */
/*==============================================================*/
create table d_member   # 导购会员
(
   d_id                 INTEGER,
   user_id              INTEGER not null,
   user_name            VARCHAR(50) not null,
   user_number          INTEGER not null
);

/*==============================================================*/
/* Table: d_order_form                                          */
/*==============================================================*/
create table d_order_form   # 导购订单
(
   d_id                 INTEGER not null,
   pro_id               varchar(70),
   order_id             integer not null,
   d_data               TIME not null,
   d_class              VARCHAR(50) not null,
   details              VARCHAR(256) not null,
   price                float not null,
   tracking_number      VARCHAR(100) not null,
   z_state              bool not null,
   f_state              bool not null,
   f_jiaoyi             bool not null
);

alter table d_order_form
   add primary key (order_id);

/*==============================================================*/
/* Table: d_performance                                         */
/*==============================================================*/
create table d_performance  #导购业绩
(
   d_id                 INTEGER,
   order_id             integer,
   d_number             INTEGER not null,
   d_xiaoshou           float not null,
   d_tuihuo             float not null,
   d_tuihuolv           varchar(10) not null
);

/*==============================================================*/
/* Table: d_shop                                                */
/*==============================================================*/
create table d_shop   #
(
   pro_id               varchar(70),
   d_id                 INTEGER
);

/*==============================================================*/
/* Table: d_worker_order                                        */
/*==============================================================*/
create table d_worker_order  # 导购工单
(
   d_id                 INTEGER,
   pro_id               varchar(70),
   job_number           integer not null,
   g_data               time not null,
   g_color              VARCHAR(20),
   b_size               integer not null,
   g_class              varchar(20) not null default '0',
   g_type               VARCHAR(100) not null default '0',
   appl                 VARCHAR(100) not null default '0',
   bar_code             VARCHAR(100) not null,
   degree               VARCHAR(20) not null default '1',
   details              VARCHAR(256) not null default '0',
   tracking_number      VARCHAR(100) not null,
   order_number         VARCHAR(100) not null default '1',
   state                VARCHAR(20)
);

/*==============================================================*/
/* Table: gl_boss                                               */
/*==============================================================*/
create table gl_boss   # 管理员分类表
(
   dl_id                integer not null,
   dl_name              INTEGER not null,
   phone                INTEGER not null,
   email                varchar(50),
   name                 VARCHAR(50) not null,
   operation            bool not null
);

alter table gl_boss
   add primary key (dl_id);

/*==============================================================*/
/* Table: gl_jurisdiction                                       */
/*==============================================================*/
create table gl_jurisdiction   #管理员权限表
(
   dl_id                integer,
   qx_id                INTEGER not null,
   qx_name              VARCHAR(50) not null
);

/*==============================================================*/
/* Table: member_info                                           */
/*==============================================================*/
create table member_info   # 会员信息表
(
   member_id            integer not null auto_increment,
   user_id              integer,
   member_name          varchar(50),
   member_level         varchar(50),
   member_score         varchar(50),
   member_balance       varchar(50),
   member_authority     varchar(50)
);

alter table member_info
   add primary key (member_id);

/*==============================================================*/
/* Table: member_level                                          */
/*==============================================================*/
create table member_level   # 会员等级表
(
   member_id            integer,
   member_name1         varchar(50),
   member_name2         varchar(50),
   member_name3         varchar(50),
   member_name          varchar(50)
);

/*==============================================================*/
/* Table: member_score                                          */
/*==============================================================*/
create table member_score   # 会员积分表
(
   member_id            integer,
   member_score         varchar(70),
   member_name          varchar(70)
);

/*==============================================================*/
/* Table: pro_classify                                          */
/*==============================================================*/
create table pro_classify   # 商品分类表
(
   pro_id               varchar(70),
   category             varchar(50) not null,
   famili               varchar(50) not null,
   brand                varchar(50) not null
);

/*==============================================================*/
/* Table: pro_details                                           */
/*==============================================================*/
create table pro_details    # 商品详情表
(
   pro_id               varchar(70),
   design               varchar(50),
   col_type             varchar(50),
   sleev_type           varchar(50),
   edition_type         varchar(50),
   sleev_length         varchar(50),
   cloth_length         varchar(50),
   commute              varchar(50),
   thickness            varchar(50),
   elastic              varchar(50),
   clothes_placket      varchar(50),
   adapt_age            varchar(70),
   sex                  varchar(50),
   TTM                  varchar(70),
   material             varchar(200)
);

/*==============================================================*/
/* Table: pro_tags                                              */
/*==============================================================*/
create table pro_tags    # 商品标签表
(
   pro_id               varchar(70),
   promotion            varchar(50)
);

/*==============================================================*/
/* Table: products                                              */
/*==============================================================*/
create table products      # 商品表
(
   pro_id               varchar(70) not null,
   name                 varchar(70) not null,
   color                varchar(70) not null,
   size                 varchar(70) not null,
   year                 varchar(70) not null,
   price                float not null,
   pro_price            float not null
);

alter table products
   add primary key (pro_id);

/*==============================================================*/
/* Table: serv_appearance                                       */
/*==============================================================*/
create table serv_appearance   # 形象顾问表
(
   user_id              varchar(70) not null,
   servic_id            int not null auto_increment,
   pro_id               varchar(70),
   service_id           integer,
   style                varchar(70) not null,
   user_size           varchar(20) not null
);

alter table serv_appearance
   add primary key (servic_id);

/*==============================================================*/
/* Table: serv_costmize                                         */
/*==============================================================*/
create table serv_costmize    # 上门定制表
(
   service_id           varbinary(70) not null,
   ser_service_id       integer,
   uer_id               varbinary(20) not null,
   height               float not null,
   B                    float,
   UBL                  float,
   W                    float,
   MHL                  float,
   H                    float,
   S                    float,
   BBW                  float,
   SL                   float,
   AH                   float,
   HL                   float,
   N                    float,
   TL                   float,
   TW                   float,
   TS                   float,
   STS                  float
);

alter table serv_costmize
   add primary key (service_id);

/*==============================================================*/
/* Table: serv_shopping_company                                 */
/*==============================================================*/
create table serv_shopping_company    # 陪同购物
(
   service_id           integer,
   city                 varchar(70) not null,
   clerk_id             varchar(70) not null,
   clerk_name           varchar(70) not null,
   clerk_img            varchar(255) not null,
   clerk_sex            varchar(70) not null,
   slogen               varchar(70) not null
);

/*==============================================================*/
/* Table: serv_store_query                                      */
/*==============================================================*/
create table serv_store_query  # 店铺查询表
(
   service_id           integer,
   server_name          varchar(70) not null
);

/*==============================================================*/
/* Table: serv_wardrobe                                         */
/*==============================================================*/
create table serv_wardrobe   # 衣橱整理表
(
   service_id           integer,
   name                 varchar(70) not null
);

/*==============================================================*/
/* Table: service                                               */
/*==============================================================*/
create table service     #服务表
(
   service_id           integer not null auto_increment,
   user_id              integer,
   name                 varchar(50) not null,
   service_time         time not null,
   clerk                varchar(20) not null,
   server               varchar(20)
);

alter table service
   add primary key (service_id);

/*==============================================================*/
/* Table: t_adress                                              */
/*==============================================================*/
create table t_adress      # 收货地址表
(
   order_id             integer,
   t_o_order_id         integer,
   user_name            varchar(32),
   user_phone           varchar(32),
   user_adress          varchar(256),
   adress_label         integer,
   is_default           integer,
   delete_adress        integer
);

/*==============================================================*/
/* Table: t_carts                                               */
/*==============================================================*/
create table t_carts      # 购物车表
(
   user_id              integer,
   pro_id               varchar(70),
   goods_number         int,
   goods_price          float,
   goods_total          float,
   goods_name           varchar(256),
   create_time          datetime,
   failure_time         datetime,
   updatae_time         datetime,
   select_all           int,
   coupon               int
);

/*==============================================================*/
/* Table: t_order                                               */
/*==============================================================*/
create table t_order    # 订单表
(
   order_id             integer not null auto_increment,
   user_id              integer,
   is_pay               int,
   pay_time             datetime,
   is_ship              int,
   ship_time            datetime,
   is_receipt           int,
   receipt_time         datetime,
   ship_number          varchar(50),
   status               int,
   create_time          datetime,
   updata_time          datetime
);

alter table t_order
   add primary key (order_id);

/*==============================================================*/
/* Table: t_orderdetails                                        */
/*==============================================================*/
create table t_orderdetails    # 订单详情表
(
   user_id              integer,
   order_id             integer,
   goods_names          varchar(256) not null,
   goods_price          float not null,
   adress               varchar(256) not null,
   price                float not null,
   coupon               float,
   total_price          float not null,
   freght_price         float not null,
   store_id             int,
   is_done              int not null
);

/*==============================================================*/
/* Table: t_ship                                                */
/*==============================================================*/
create table t_ship      #物流表
(
   order_id             integer not null,
   user_id              integer,
   t_ship               varchar(50),
   ship_status          int,
   collect_time         datetime,
   sign_for_status      int,
   sign_for_time        datetime,
   well_recieve_status  int
);

alter table t_ship
   add primary key (order_id);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user      # 用户表
(
   user_id              integer not null auto_increment,
   username             varchar(50) not null,
   user_password        varchar(30) not null,
   user_email           varchar(50) not null,
   user_balabce         varchar(100) not null,
   is_activate          smallint not null,
   user_images          varchar(50),
   user_level           integer not null,
   vip_datetime         varchar(20),
   lasttime             varchar(20)
);

alter table user
   add primary key (user_id);

/*==============================================================*/
/* Table: user_collect_store                                    */
/*==============================================================*/
create table user_collect_store    # 用户收藏店铺
(
   store_id             integer not null,
   user_id              integer,
   store_name           varchar(50),
   store_news           varchar(50)
);

alter table user_collect_store
   add primary key (store_id);

/*==============================================================*/
/* Table: user_coupon                                           */
/*==============================================================*/
create table user_coupon        # 用户优惠券
(
   coupon_types         integer not null,
   coupon_id            integer,
   user_id              integer,
   coupan_nums          integer,
   coupan_name          varchar(70)
);

alter table user_coupon
   add primary key (coupon_types);

/*==============================================================*/
/* Table: user_message                                          */
/*==============================================================*/
create table user_message    # 用户留言反馈表
(
   user_id              integer,
   user_message         varchar(100),
   cart_id              int not null,
   user_message_time    timestamp,
   cart_name            varchar(50),
   good_level           varchar(50)
);

/*==============================================================*/
/* Table: user_order                                            */
/*==============================================================*/
create table user_order   # 用户订单
(
   order_id             int not null auto_increment,
   user_id              integer,
   order_detail         varchar(70) not null,
   order_time           timestamp,
   send_time            timestamp,
   receive_time         timestamp,
   send_address         varchar(50)
);

alter table user_order
   add primary key (order_id);

/*==============================================================*/
/* Table: user_recharge                                         */
/*==============================================================*/
create table user_recharge     # 用户充值记录
(
   ID                   integer not null auto_increment,
   user_id              integer,
   type_id              varchar(70) not null,
   time                 varchar(20)
);

alter table user_recharge
   add primary key (ID);

/*==============================================================*/
/* Table: user_track                                            */
/*==============================================================*/
create table user_track   # 用户留言足迹表
(
   user_id              integer,
   skill_time           timestamp,
   cart_name            varchar(50),
   cart_id              int not null
);

/*==============================================================*/
/* Table: user_transaction                                      */
/*==============================================================*/
create table user_transaction  #用户交易记录表
(
   pro_id               varchar(70),
   ID                   integer not null auto_increment,
   user_id              integer,
   details              varchar(100),
   number               integer not null,
   payment_types        varchar(50) not null
);

alter table user_transaction
   add primary key (ID);

alter table d_boss add constraint FK_Reference_76 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table d_fans add constraint FK_Reference_60 foreign key (d_id)
      references d_boss (d_id) on delete restrict on update restrict;

alter table d_member add constraint FK_Reference_63 foreign key (d_id)
      references d_boss (d_id) on delete restrict on update restrict;

alter table d_order_form add constraint FK_Reference_59 foreign key (d_id)
      references d_boss (d_id) on delete restrict on update restrict;

alter table d_order_form add constraint FK_Reference_77 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

alter table d_order_form add constraint FK_Reference_78 foreign key (order_id)
      references t_order (order_id) on delete restrict on update restrict;

alter table d_performance add constraint FK_Reference_62 foreign key (d_id)
      references d_boss (d_id) on delete restrict on update restrict;

alter table d_performance add constraint FK_Reference_79 foreign key (order_id)
      references d_order_form (order_id) on delete restrict on update restrict;

alter table d_shop add constraint FK_Reference_36 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

alter table d_shop add constraint FK_Reference_61 foreign key (d_id)
      references d_boss (d_id) on delete restrict on update restrict;

alter table d_worker_order add constraint FK_Reference_58 foreign key (d_id)
      references d_boss (d_id) on delete restrict on update restrict;

alter table d_worker_order add constraint FK_Reference_75 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

alter table gl_jurisdiction add constraint FK_Reference_44 foreign key (dl_id)
      references gl_boss (dl_id) on delete restrict on update restrict;

alter table member_info add constraint FK_Reference_55 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table member_level add constraint FK_Reference_74 foreign key (member_id)
      references member_info (member_id) on delete restrict on update restrict;

alter table member_score add constraint FK_Reference_56 foreign key (member_id)
      references member_info (member_id) on delete restrict on update restrict;

alter table pro_classify add constraint FK_Reference_66 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

alter table pro_details add constraint FK_Reference_67 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

alter table pro_tags add constraint FK_Reference_65 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

alter table serv_appearance add constraint FK_Reference_68 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

alter table serv_appearance add constraint FK_Reference_69 foreign key (service_id)
      references service (service_id) on delete restrict on update restrict;

alter table serv_costmize add constraint FK_Reference_70 foreign key (ser_service_id)
      references service (service_id) on delete restrict on update restrict;

alter table serv_shopping_company add constraint FK_Reference_81 foreign key (service_id)
      references service (service_id) on delete restrict on update restrict;

alter table serv_store_query add constraint FK_Reference_82 foreign key (service_id)
      references service (service_id) on delete restrict on update restrict;

alter table serv_wardrobe add constraint FK_Reference_80 foreign key (service_id)
      references service (service_id) on delete restrict on update restrict;

alter table service add constraint FK_Reference_53 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table t_adress add constraint FK_Reference_43 foreign key (order_id)
      references t_ship (order_id) on delete restrict on update restrict;

alter table t_adress add constraint FK_Reference_73 foreign key (t_o_order_id)
      references t_order (order_id) on delete restrict on update restrict;

alter table t_carts add constraint FK_Reference_51 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table t_carts add constraint FK_Reference_64 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

alter table t_order add constraint FK_Reference_50 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table t_orderdetails add constraint FK_Reference_37 foreign key (order_id)
      references t_order (order_id) on delete restrict on update restrict;

alter table t_orderdetails add constraint FK_Reference_42 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table t_ship add constraint FK_Reference_41 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table t_ship add constraint FK_Reference_72 foreign key (order_id)
      references t_order (order_id) on delete restrict on update restrict;

alter table user_collect_store add constraint FK_Reference_54 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_coupon add constraint FK_Reference_46 foreign key (coupon_id)
      references coupons_types (coupon_id) on delete restrict on update restrict;

alter table user_coupon add constraint FK_Reference_57 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_message add constraint FK_Reference_47 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_order add constraint FK_Reference_49 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_recharge add constraint FK_Reference_45 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_track add constraint FK_Reference_48 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_transaction add constraint FK_Reference_52 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_transaction add constraint FK_Reference_71 foreign key (pro_id)
      references products (pro_id) on delete restrict on update restrict;

