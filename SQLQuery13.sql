DROP TABLE IF EXISTS [Moons];
DROP TABLE IF EXISTS [Planets];

CREATE TABLE [Planets] (
    [ID] INT IDENTITY(1,1),
    [name] VARCHAR(255) NOT NULL,
    [diameter] FLOAT NOT NULL,
    [howfar] FLOAT NOT NULL,
    [Type] VARCHAR(50)
);

INSERT INTO [Planets] ([name], [diameter], [howfar], [Type]) VALUES 
(N'Earth', 12742, 149.6, N'Planet'),
(N'Mars', 6779, 227.9, N'Planet');

SELECT * FROM [Planets];