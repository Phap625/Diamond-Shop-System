class Transaction(Base):
    __tablename__ = 'Transactions'
    
    TransactionID = Column(Integer, primary_key=True, autoincrement=True)
    OrderID = Column(Integer, ForeignKey('Orders.OrderID', ondelete='CASCADE'), nullable=False)
    PaymentMethod = Column(Enum('Cash', 'Credit Card', 'Bank Transfer', name='payment_method'), nullable=False)
    Amount = Column(DECIMAL(15, 2), nullable=False)
    TransactionDate = Column(TIMESTAMP, default=datetime.utcnow)
engine = create_engine('sqlite:///diamonds.db', echo=True)
Base.metadata.create_all(engine)
