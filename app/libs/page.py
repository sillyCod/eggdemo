from flask_sqlalchemy import BaseQuery


def paginate(query: BaseQuery, page_num: int = 1, page_size: int = 10):
    query_slice = query.paginate(int(page_num), int(page_size))
    result = dict()
    result.update(data=query_slice.items, has_previous=query_slice.has_prev, has_next=query_slice.has_next)
    return result
