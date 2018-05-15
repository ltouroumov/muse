from json import JSONEncoder

from muse_writer.models import ProjectNode, Document


def extract(obj, *keys):
    res = {}
    for key in keys:
        res[key] = obj[key]

    return res


class DocumentTreeEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, ProjectNode):
            return {'document': o.document,
                    'children': o.children}
        elif isinstance(o, Document):
            return extract(o.__dict__, 'id', 'name', 'path', 'sort', 'type')
        else:
            return super().encode(o)


class DocumentMetaEncoder(JSONEncoder):
    def default(self, o):
        return extract(o.__dict__, 'id', 'name', 'path', 'sort', 'type')
