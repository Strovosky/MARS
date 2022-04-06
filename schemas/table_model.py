from sqlalchemy.orm import declarative_base, sessionmaker # To create the table / and create the session.
from sqlalchemy import Column, String, Integer, BigInteger, Boolean, Date # To create the table model.
from datetime import datetime # For date type.
from config.db_config import engine # To bind the engine to local_session.

Base = declarative_base()

Session = sessionmaker()
local_session = Session(bind=engine)

class MemberModelTable(Base):
    __tablename__ = "Members"
    first_name = Column(String(length=50), nullable=False, unique=False)
    last_name = Column(String(length=60), nullable=False, unique=False)
    middle_initial = Column(String(length=4))
    date_of_birth = Column(Date(), nullable=True, unique=False)
    membership_id = Column(Integer(), primary_key=True, nullable=False, unique=True, comment="It must be a 7 digit number.", autoincrement=True)
    email = Column(String(length=70), nullable=True, unique=False)
    phone = Column(Integer(), nullable=True, unique=False)
    cellphone = Column(BigInteger(), nullable=True, unique=False)
    address = Column(String(length=200), nullable=True, unique=False)
    is_active_member = Column(Boolean(), nullable=False, default=True)
    enrollement = Column(Date(), default=datetime.utcnow, nullable=False, unique=False)
    last_renewal = Column(Date(), nullable=True, unique=False, default=None, comment="When they renew, this will change.")
    membership_price_paid = Column(BigInteger(), nullable=False, unique=False, comment="I'll write this manually.")
    page = Column(String(length=200), nullable=True, unique=False)

# To create the table.
Base.metadata.create_all(engine)

