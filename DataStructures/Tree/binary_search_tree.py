from DataStructures.Tree import bst_node 
from DataStructures.List import single_linked_list as lt

def new_map ():
    
    return {"root": None}

def insert_node(root, key, value):
    if root is None:
        return {"key": key, "value": value, "left": None, "right": None}

    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    return root

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst
    

def default_compare (key, element):
    if key == bst_node.get_key(element):
        return 0
    elif key > bst_node.get_key(element):
        return 1
    return -1

def get_node(root,key):
    
    if root is None:
        return None
    if bst_node.get_key(root) == key:
        return root
    elif bst_node.get_key(root) < key:
        return get_node(root["right"], key)
    elif bst_node.get_key(root) > key:
        return get_node(root["left"], key)


def get (my_bst, key):
    if my_bst["root"] is None:
        return None
    else:
        node = get_node(my_bst["root"], key)
        if node is None:
            return None
        else: 
            return bst_node.get_value(node)
        

def size_node(root):
    if root is None:
        return 0
    else:
        return 1 + size_node(root["left"]) + size_node(root["right"])
        
def size (my_bst):
    if my_bst["root"] is None:
        return 0
    else:
        return size_node(my_bst["root"])
    
def get_min_node(root):
    if root is None:
        return None
    else:
        current = root
        while current["left"] is not None:
            current = current["left"]
        return current["key"]
    
def get_min(my_bst):
    if my_bst["root"] is None:
        return None
    else:
        return get_min_node(my_bst["root"])

def get_max_node(root):
    if root is None:
        return None
    else:
        current = root
        while current["right"] is not None:
            current = current["right"]
        return current["key"]
    

def get_max(my_bst):
    if my_bst["root"] is None:
        return None
    else:
        return get_max_node(my_bst["root"])
    
def delete_min_tree(root):
    if root is None:
        return None
    elif root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    return root

def delete_min(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root["right"]
    root["right"] = delete_max_tree(root["right"])
    return root    

def delete_max(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def contains(my_bst,key):
    if get(my_bst,key) is None:
        return False
    else:
        return True


def is_empty(my_bst):
    if my_bst["root"] is None:
        return True
    else:
        return False


def key_set_tree(root, linked_list):
    
    if root is not None:
        key_set_tree(root["left"], linked_list)

        new_node = {"info": root["key"], "next": None}
        if linked_list["first"] is None:
            linked_list["first"] = new_node
            linked_list["last"] = new_node
        else:
            linked_list["last"]["next"] = new_node
            linked_list["last"] = new_node
        linked_list["size"] += 1

        key_set_tree(root["right"], linked_list)


def key_set(my_bst):
    
    linked_list = {"first": None, "last": None, "size": 0}
    key_set_tree(my_bst["root"], linked_list)
    return linked_list




def value_set_tree(root, linked_list):
    
    if root is not None:
        value_set_tree(root["left"], linked_list)

        new_node = {"info": root["value"], "next": None}
        if linked_list["first"] is None:
            linked_list["first"] = new_node
            linked_list["last"] = new_node
        else:
            linked_list["last"]["next"] = new_node
            linked_list["last"] = new_node
        linked_list["size"] += 1

        value_set_tree(root["right"], linked_list)


def value_set(my_bst):
    
    linked_list = {"first": None, "last": None, "size": 0}
    value_set_tree(my_bst["root"], linked_list)
    return linked_list


def height_tree(root):
    if root is None:
        return 0 
    else:
        left_height = height_tree(root["left"])
        right_height = height_tree(root["right"])
        return 1 + max(left_height, right_height)

def height (my_bst):
    if my_bst["root"] is None:
        return 0
    else:
        return height_tree(my_bst["root"])


def keys_range(root,key_initial, key_final, all_keys):
    if  key_initial > key_final or lt.size(all_keys) == 0:
        return lt.new_list()
    else:
        keys_in_range = lt.new_list()
        for i in range (0,lt.size(all_keys)):
            key = lt.get_element(all_keys, i)
            if key_initial <= key <= key_final:
                lt.add_last(keys_in_range, key)
        return keys_in_range

def keys(my_bst,key_initial, key_final):
    if my_bst["root"] is None:
        return lt.new_list()
    else:
        all_keys = key_set(my_bst)
        return keys_range(my_bst["root"],key_initial, key_final, all_keys)
    
def values_range(my_bst,key_initial, key_final, all_keys):
    if  key_initial > key_final or lt.size(all_keys) == 0:
        return lt.new_list()
    else:
        values_in_range = lt.new_list()
        for i in range (0,lt.size(all_keys)):
            key = lt.get_element(all_keys, i)
            if key_initial <= key <= key_final:
                values = get(my_bst, key)
                lt.add_last(values_in_range, values)
        return values_in_range


def values(my_bst,key_initial, key_final):
    if my_bst["root"] is None:
        return lt.new_list()
    else:
        
        all_keys = key_set(my_bst)
        return values_range(my_bst,key_initial, key_final, all_keys)
    
    