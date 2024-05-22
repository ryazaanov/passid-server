from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class UserSchema(Base):
    __tablename__ = 'users'
    user_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String)
    birth_date = Column(DateTime)

    admins = relationship("AdminSchema", back_populates="user")
    passes = relationship("PassSchema", back_populates="user")
    access_logs = relationship("AccessLogSchema", back_populates="user")
    pass_requests = relationship("PassRequestSchema", back_populates="user")

class AdminSchema(Base):
    __tablename__ = 'admins'
    admin_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    position = Column(String, nullable=False)
    role = Column(String, nullable=False)

    user = relationship("UserSchema", back_populates="admins")

class AccessZoneSchema(Base):
    __tablename__ = 'access_zones'
    zone_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    zone_name = Column(String, nullable=False)
    description = Column(String)

class PassSchema(Base):
    __tablename__ = 'passes'
    pass_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    zone_id = Column(UUID(as_uuid=True), ForeignKey('access_zones.zone_id'), nullable=False)
    pass_type = Column(String, nullable=False)
    issue_date = Column(DateTime, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    access_level = Column(Integer, nullable=False)

    user = relationship("UserSchema", back_populates="passes")
    zone = relationship("AccessZoneSchema")

class AccessLogSchema(Base):
    __tablename__ = 'access_logs'
    log_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    pass_id = Column(UUID(as_uuid=True), ForeignKey('passes.pass_id'), nullable=False)
    access_datetime = Column(DateTime, nullable=False)
    access_type = Column(String, nullable=False)

    user = relationship("UserSchema", back_populates="access_logs")
    pass_obj = relationship("PassSchema")

class PassRequestSchema(Base):
    __tablename__ = 'pass_requests'
    request_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    request_date = Column(DateTime, nullable=False)
    request_status = Column(String, nullable=False, default="pending")
    approved = Column(Boolean, default=False)
    admin_id = Column(UUID(as_uuid=True), ForeignKey('admins.admin_id'), nullable=True)

    user = relationship("UserSchema", back_populates="pass_requests")
    admin = relationship("AdminSchema")
