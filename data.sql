CREATE DATABASE DiamondStore;
USE DiamondStore;
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    PhoneNumber VARCHAR(15),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Diamonds (
    DiamondID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Carat DECIMAL(5, 2) NOT NULL, 
    Color VARCHAR(10), 
    Clarity VARCHAR(10), 
    CutQuality VARCHAR(50), 
    Price DECIMAL(10, 2) NOT NULL, 
    Stock INT DEFAULT 0, 
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Earrings (
    EarringID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL, -- Tên bông tai
    Style VARCHAR(50),          -- Kiểu dáng (hạt nhỏ, chùm, v.v.)
    MetalType VARCHAR(50),      -- Loại kim loại
    DiamondID INT,              -- Liên kết với bảng Diamonds
    Price DECIMAL(10, 2) NOT NULL,
    Stock INT DEFAULT 0,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (DiamondID) REFERENCES Diamonds(DiamondID) ON DELETE SET NULL
);
CREATE TABLE Necklaces (
    NecklaceID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL, -- Tên dây chuyền
    MetalType VARCHAR(50),      -- Loại kim loại
    Length DECIMAL(5, 2),       -- Độ dài dây chuyền (cm)
    DiamondID INT,              -- Liên kết với bảng Diamonds
    Price DECIMAL(10, 2) NOT NULL,
    Stock INT DEFAULT 0,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (DiamondID) REFERENCES Diamonds(DiamondID) ON DELETE SET NULL
);
CREATE TABLE Rings (
    RingID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL, -- Tên nhẫn
    MetalType VARCHAR(50),      -- Loại kim loại (vàng, bạch kim, bạc, v.v.)
    Size DECIMAL(4, 1),         -- Kích thước nhẫn (đơn vị: mm)
    DiamondID INT,              -- Liên kết với bảng Diamonds
    Price DECIMAL(10, 2) NOT NULL,
    Stock INT DEFAULT 0,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (DiamondID) REFERENCES Diamonds(DiamondID) ON DELETE SET NULL
);
CREATE TABLE LooseDiamonds (
    LooseDiamondID INT AUTO_INCREMENT PRIMARY KEY,
    DiamondID INT NOT NULL,    -- Liên kết với bảng Diamonds
    Certification VARCHAR(50), -- Chứng nhận (GIA, IGI, v.v.)
    Description TEXT,
    FOREIGN KEY (DiamondID) REFERENCES Diamonds(DiamondID) ON DELETE CASCADE
);
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) DEFAULT 'Pending', -- Trạng thái đơn hàng
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT NOT NULL,
    DiamondID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (DiamondID) REFERENCES Diamonds(DiamondID) ON DELETE CASCADE
);
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT NOT NULL,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50), -- Phương thức thanh toán
    Status VARCHAR(50) DEFAULT 'Completed', -- Trạng thái thanh toán
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);

