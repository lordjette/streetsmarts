from sqlalchemy import Column, create_engine, func, Integer, type_coerce
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

# :fire::fire::fire: MAHIRAP :fire::fire::fire:

class A(Base): # ⏰ 
    __tablename__ = "a"

    id = Column(Integer, primary_key=True)
    data = Column(JSONB)


e = create_engine("postgresql://scott:tiger@localhost/test", echo=True)
Base.metadata.drop_all(e)
Base.metadata.create_all(e)

s = Session(e)

data = {
    "preference": {
        "android": {
            "software_update": "true",
            "system_maintenance": "true"
        },
        "ios": {
            "software_update": "true",
            "system_maintenance": "true"
        }
    }
}

a1 = A(data=data)  # ⏰ 
s.add(a1)
s.commit()

s.query(A).update(
    {
        A.data: func.jsonb_set(
            A.data,
            "{preference,android}",
            type_coerce(
                {"software_update": "false", "system_maintenance": "false"},
                JSONB,
            ),
        )
    },
    synchronize_session="fetch",
)


assert a1.data["preference"]["android"] == {
    "software_update": "false",
    "system_maintenance": "false",

}

