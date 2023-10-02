from __future__ import annotations
from typing import Type
from abc import ABC, abstractmethod

class Document:
    def __init__(self):
        self.header: Header = None
        self.body: Body = None
        self.footer: Footer = None
        self.content: Content = None
        self.doc_type: DocumentType = None

    def __str__(self) -> str:
        return f"Header: {self.header}\nBody: {self.body}\nFooter: {self.footer}\nContent: {self.content}\nDocument Type: {self.doc_type}"

class Header:
    def __init__(self):
        self.text: str = None
    
    def __str__(self) -> str:
        return self.text

class Body:
    def __init__(self):
        self.text: str = None
    
    def __str__(self) -> str:
        return self.text
class Footer:
    def __init__(self):
        self.text: str = None
    
    def __str__(self) -> str:
        return self.text

class Content:
    def __init__(self):
        self.text: str = None

    def __str__(self) -> str:
        return self.text
    
class DocumentType:
    def __init__(self):
        self.text: str = None
    
    def __str__(self) -> str:
        return self.text

class Builder(ABC):
    @abstractmethod
    def build_header(self) -> Header: pass
    @abstractmethod
    def build_body(self) -> Body: pass
    @abstractmethod
    def build_footer(self) -> Footer: pass
    @abstractmethod
    def build_content(self) -> Content: pass
    @abstractmethod
    def build_type(self) -> DocumentType: pass

class DocumentBuilder(Builder):
    def build_header(self) -> Header:
        header = Header()
        header.text = "This is the header"
        return header

    def build_body(self) -> Body:
        body = Body()
        body.text = "This is the body"
        return body

    def build_footer(self) -> Footer:
        footer = Footer()
        footer.text = "This is the footer"
        return footer

    def build_content(self) -> Content:
        content = Content()
        content.text = "This is the content"
        return content
    
    def build_type(self) -> DocumentType:
        doc_type = DocumentType()
        doc_type.text = "This is the type"
        return doc_type

class Director:
    def __init__(self):
        self.__builder = None
    def set_builder(self, builder: Type[Builder]):
        self.__builder = builder
    def build_document(self) -> Document:
        document = Document()
        document.header = self.__builder.build_header()
        document.body = self.__builder.build_body()
        document.footer = self.__builder.build_footer()
        document.content = self.__builder.build_content()
        document.doc_type = self.__builder.build_type()
        return document

def main():
    builder = DocumentBuilder()
    director = Director()
    director.set_builder(builder)
    document = director.build_document()
    # Printing the document's attributes for demonstration
    print(document.__dict__) 
    print(document)

if __name__ == "__main__":
    main()
