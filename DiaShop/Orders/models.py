class Order(Base):
    __tablename__ = 'Orders'
    
    OrderID = Column(Integer, primary_key=True, autoincrement=True)
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID', ondelete='CASCADE'), nullable=False)
    OrderDate = Column(TIMESTAMP, default=datetime.utcnow)
    TotalPrice = Column(DECIMAL(15, 2), nullable=False)
    Status = Column(Enum('Pending', 'Completed', 'Canceled', name='order_status'), default='Pending')
class OrderDetail(Base):
    __tablename__ = 'OrderDetails'
    
    OrderDetailID = Column(Integer, primary_key=True, autoincrement=True)
    OrderID = Column(Integer, ForeignKey('Orders.OrderID', ondelete='CASCADE'), nullable=False)
    DiamondID = Column(Integer, ForeignKey('Diamonds.DiamondID', ondelete='CASCADE'), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Price = Column(DECIMAL(15, 2), nullable=False)
