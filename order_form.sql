alter table pro_classify
    add constraint FK_1 foreign key(pro_id) references products(pro_id);
