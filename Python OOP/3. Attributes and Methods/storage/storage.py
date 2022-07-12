class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += f"Document {doc.id}: {doc.file_name}; category {doc.category_id}, topic {doc.topic_id}" \
                      f", tags: {', '.join(tag for tag in doc.tags)}"
            if not doc == self.documents[-1]:
                result += "\n"
        return result

    @staticmethod
    def return_searched_object(place, id):
        searched_object = [x for x in place if x.id == id][0]
        return searched_object

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.return_searched_object(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_name: str, new_storage_folder: str):
        topic = self.return_searched_object(self.topics, topic_id)
        topic.topic = new_name
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.return_searched_object(self.documents, document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.return_searched_object(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.return_searched_object(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.return_searched_object(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.return_searched_object(self.documents, document_id)
        return document
