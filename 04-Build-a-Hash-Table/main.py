class HashTable:
    collection={}

    def __init__(self):
        pass

    def hash(self, string:str):
        hash_value=sum(ord(i) for i in string)
        return hash_value

    def add(self,key: str,value):
        hash_key=self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key]={key:value}
        else:
            self.collection[hash_key][key]=value
        

    def remove(self,key:str):
        hash_key=self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]

        else:
            pass

    def lookup(self,key):
        hash_key=self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]

        else:
            return None
