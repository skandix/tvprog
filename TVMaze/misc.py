import json

class misc:
    def __init__(self):
        ...
        
    def __str__(self):
        ...
        
    def __repr__(self):
        ...

    def env(self):
        # want to load in dotenv files and such.
        ... 

    def load_json(self, fp):
        """
        load_json [summary]

        Args:
            fp ([type]): [description]

        Returns:
            [type]: [description]
        """
        return json.load(fp)

    def store_json(self, fp):
        return json.dump(fp, ensure_ascii=True, indent=4)