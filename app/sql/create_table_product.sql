create table Product (
	Id int NOT NULL identity,
	[Name] varchar(200),
	[Description] varchar(200)
	primary key (id)
)

create table Product (
	Id uniqueidentifier default newid(),
	[Name] varchar(200),
	[Description] varchar(200)
	primary key (id)
)