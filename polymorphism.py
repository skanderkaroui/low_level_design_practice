class Document:
    def show(self):
        raise NotImplementedError("Subclass must implement abstart method")

class Pdf(Document):
    def show(self):
        return "show PDF Content"

class Word(Document):
    def show(self):
        return "show Word Content"
    

docs = [Pdf(), Word()]
for doc in docs:
    print(doc.show())

#OUTPUT:
#show PDF Content
#show Word Content


#this is an example of how polymorphism is achieved through method overriding