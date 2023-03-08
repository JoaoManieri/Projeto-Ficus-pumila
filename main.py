import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from getWords import getWords


def setData(db):

    data = getdata(db)

    doc_ref = db.collection(u'HotTopcs').document(u'HotTopcs1')
    doc_ref.set(data)

    # for record in data:
    #     doc_ref = db.collection(u'HotTopcs').document(u'HotTopcs1')
    #     doc_ref.set(record)


def getdata(db):

    collections_ref = db.collection(u'Discussion').where(
        u'type', u'==', 0).order_by(u'up_votes')
    docs = collections_ref.stream()

    text = ""

    for doc in docs:
        out = doc.to_dict()
        title = out.get(u'discution_title')
        body = out.get(u'body_question')

        text = text + f' {title} ' + f' {body} '

    return getWords(text)


if __name__ == '__main__':
    # Use the application default credentials.
    # cred = credentials.Certificate("serviceAccountKey_teste.json")
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    setData(db)

