from com.mhire.app.database.db_manager.db_manager import DBManager

class CRUD:
  def __init__(self, database ="mongo", connection_name="default"):
        
        self.connection_name = connection_name
        # self.uri = uri
        # self.token = token
        
        if database.lower() == 'mongo':
          # self.client = MilvusManager(connection_name=connection_name, milvus_token=token, milvus_uri=uri)
          self.client = DBManager(connection_name=connection_name)
        
        elif database.lower() == 'pinecone':
          pass
        elif database.lower() == 'faiss':
          pass
  
  def create(self, collection_name: str, keys_for_embedding, data_for_embedding):
        result = self.client.insert_data(collection_name, keys_for_embedding, data_for_embedding)
        return result

  def read(self, query, search_fields, collection_name: str):
    results = self.client.search_and_retrieve(collection_name=collection_name, query=query, search_fields=search_fields)
    return results
  
  
  def update(self, collection_name: str, field_name, field_value, new_field_value):
    result = self.client.update_entry(collection_name, field_name, field_value, new_field_value)
    return result

  def delete(self, collection_name,  field_name, field_value):
    result = self.client.delete_entry(collection_name,  field_name, field_value)
    return result
