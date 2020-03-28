from Base import db,Puppy

db.create_all()

sam = Puppy("Sam",12)
frank = Puppy("Frank", 13)

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])
db.session.commit()

print(sam.id)
print(frank.id)
