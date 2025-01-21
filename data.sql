CREATE DATABASE CuaHangKimCuong;
USE CuaHangKimCuong;
CREATE TABLE Guest (
    GuestID INT AUTO_INCREMENT PRIMARY KEY,
    SessionID VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(150) UNIQUE NOT NULL,
    FullName VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Email VARCHAR(100),
    Address VARCHAR(200),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    GuestID INT,
    FOREIGN KEY (GuestID) REFERENCES Guest(GuestID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
CREATE TABLE Sale (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Position VARCHAR(50),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100),
    HireDate DATE,
    Salary FLOAT
);

CREATE TABLE DeliveryStaff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100),
    HireDate DATE,
    Salary FLOAT
);
CREATE TABLE Category (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL,
    Description TEXT
);
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    CategoryID INT,
    Description TEXT,
    Weight FLOAT, -- Đơn vị carat
    Price FLOAT NOT NULL,
    Stock INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
CREATE TABLE Item (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    Price FLOAT NOT NULL,
    TotalPrice FLOAT GENERATED ALWAYS AS (Quantity * Price) STORED,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE ShoppingCart (
    CartID INT AUTO_INCREMENT PRIMARY KEY,
    GuestID INT,
    CustomerID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (GuestID) REFERENCES Guest(GuestID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
CREATE TABLE OrderStatus (
    StatusID INT AUTO_INCREMENT PRIMARY KEY,
    StatusName VARCHAR(50) NOT NULL,
    Description TEXT
);
CREATE TABLE `Order` (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    StaffID INT,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    DeliveryDate DATE,
    TotalAmount FLOAT,
    StatusID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES Sale(EmployeeID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (StatusID) REFERENCES OrderStatus(StatusID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
ALTER TABLE ShoppingCart
ADD OrderID INT,
ADD FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID)
    ON DELETE SET NULL
    ON UPDATE CASCADE;


ALTER TABLE Customer
ADD COLUMN Password VARCHAR(255);

