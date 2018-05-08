from collections import namedtuple

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean

from muse_writer.data import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    summary = Column(Text)

    date_created = Column(DateTime)
    date_edited = Column(DateTime, nullable=True)

    documents = relationship('Document')

    def documents_tree(self):
        root = []
        parents = {}
        for doc in sorted(self.documents, key=lambda d: len(d.path)):
            node = Node(document=doc, children=[])
            parents["%s/%d" % (doc.path if doc.path != '/' else '', doc.id)] = node
            if doc.path == '/':
                root.append(node)
            else:
                parent = parents[doc.path]
                parent.children.append(node)

        return root


Node = namedtuple('ProjectNode',
                  ['document', 'children'])


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    name = Column(String(256))
    path = Column(String(256))
    sort = Column(Integer)
    type = Column(String(256))
    data = Column(Text)
