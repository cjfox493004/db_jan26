from sqlmodel import Session
from models import Facullty, engine

f1 = Facullty(firstname = "Chris", lastname = "ManSandwitch")
f2 = Facullty(firstname = "Mahesh", lastname = "Maddumalla")
f3 = Facullty(firstname = "Chuck", lastname = "Redmond")


with Session(engine) as session:
    session.add(f1)
    session.add(f2)
    session.add(f3)
    session.commit()