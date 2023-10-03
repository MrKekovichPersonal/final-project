import eel
from backend.database.employees.methods import (create,
                                                get,
                                                get_by_id,
                                                get_like,
                                                edit,
                                                delete_many)

if __name__ == '__main__':
    eel.init('web/')
    eel.start('index.html')
