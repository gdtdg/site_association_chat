create table message_contact
(
    id          int auto_increment
        primary key,
    nom         varchar(100)                          null,
    prenom      varchar(100)                          null,
    adresse     varchar(100)                          null,
    code_postal int                                   null,
    ville       varchar(100)                          null,
    email       varchar(100)                          null,
    telephone   varchar(100)                          null,
    objet       varchar(100)                          null,
    message     varchar(3000)                         null,
    timestamp   timestamp default current_timestamp() not null on update current_timestamp()
);

