CREATE DATABASE CuaHangKimCuong2;
USE CuaHangKimCuong2;
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20) UNIQUE NOT NULL,
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalPrice DECIMAL(15,2) NOT NULL,
    Status ENUM('Pending', 'Completed', 'Canceled') DEFAULT 'Pending',
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT NOT NULL,
    DiamondID INT NOT NULL,
    Quantity INT NOT NULL,
    Price DECIMAL(15,2) NOT NULL, -- Giá tại thời điểm mua
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (DiamondID) REFERENCES Diamonds(DiamondID) ON DELETE CASCADE
);
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255),
    Phone VARCHAR(20) UNIQUE NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Address TEXT
);
CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,
    SupplierID INT NOT NULL,
    DiamondID INT NOT NULL,
    Quantity INT NOT NULL,
    PurchasePrice DECIMAL(15,2) NOT NULL, -- Giá nhập
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE,
    FOREIGN KEY (DiamondID) REFERENCES Diamonds(DiamondID) ON DELETE CASCADE
);
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) UNIQUE NOT NULL,
    Position VARCHAR(50), -- Chức vụ (Bán hàng, Quản lý, Kế toán...)
    Salary DECIMAL(15,2), -- Lương
    HireDate DATE NOT NULL
);
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT NOT NULL,
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL,
    Amount DECIMAL(15,2) NOT NULL,
TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);
INSERT INTO Diamonds (Name, Carat, Cut, Color, Clarity, Price, Stock, Certificate, Description, ImageURL)
VALUES
('Brilliant Round Diamond', 1.0, 'Excellent', 'D', 'VVS1', 15000.00, 5, 'GIA', 'Viên kim cương tròn hoàn hảo với độ trong cao.', 'https://example.com/diamond1.jpg'),
('Princess Cut Diamond', 1.2, 'Very Good', 'E', 'VS1', 12000.00, 3, 'IGI', 'Kim cương cắt princess lấp lánh.', 'https://example.com/diamond2.jpg'),
('Oval Shape Diamond', 0.9, 'Excellent', 'F', 'IF', 14000.00, 4, 'GIA', 'Hình oval với độ sáng xuất sắc.', 'https://example.com/diamond3.jpg'),
('Emerald Cut Diamond', 1.5, 'Good', 'G', 'VS2', 11000.00, 2, 'HRD', 'Phong cách quý phái với giác cắt emerald.', 'https://example.com/diamond4.jpg'),
('Cushion Cut Diamond', 1.0, 'Excellent', 'D', 'IF', 16000.00, 6, 'GIA', 'Cushion cut mang vẻ đẹp cổ điển.', 'https://example.com/diamond5.jpg');
customers
