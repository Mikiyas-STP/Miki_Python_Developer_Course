from sqlalchemy import Column, Integer, String

class BlogPost(Base):
    __tablename__ = "posts" 

    # Define the columns
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)