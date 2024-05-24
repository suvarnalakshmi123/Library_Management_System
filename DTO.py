from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class UserDTO(BaseModel):
    id: int
    username: str
    email: str
    role: str
    last_login: datetime

class PatronDTO(UserDTO):
    member_since: datetime
    address: str
    phone_number: int
    active_status: bool
    fine_amount: Decimal
    created_at: datetime

class BookDTO(BaseModel):
    title: str
    author: str
    ISBN: int
    quantity: int 
    inventory: int
    borrowed_books: int
    return_books: int
    category: str
    renew_a_book: bool
    fine_amount: float
    price_of_the_book: float
 
    
    