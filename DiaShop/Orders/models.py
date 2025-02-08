class Order(Base):
    __tablename__ = 'Orders'
    
    OrderID = Column(Integer, primary_key=True, autoincrement=True)
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID', ondelete='CASCADE'), nullable=False)
    OrderDate = Column(TIMESTAMP, default=datetime.utcnow)
    TotalPrice = Column(DECIMAL(15, 2), nullable=False)
    Status = Column(Enum('Pending', 'Completed', 'Canceled', name='order_status'), default='Pending')
