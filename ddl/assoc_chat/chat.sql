create table chat
(
    id             int auto_increment
        primary key,
    nom            varchar(100)  null,
    sexe           varchar(100)  null,
    naissance      varchar(100)  null,
    race           varchar(100)  null,
    robe           varchar(100)  null,
    vaccin         varchar(100)  null,
    sterilisation  varchar(100)  null,
    identification varchar(100)  null,
    deparasitage   varchar(100)  null,
    commentaire    varchar(3000) null,
    photo          varchar(100)  null,
    carousel       varchar(500)  null
);

