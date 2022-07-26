from flask import request

def paginate(query, per_page = 15):
    page = request.args.get('page', default = 1, type = int)
    total = query.count()
    total_pages = total//per_page
    total_pages += 1 if total%per_page != 0 else 0
    items = query.paginate(page=page, per_page=per_page).items
    return {'total': total, 'page': page ,'total_pages': total_pages, 'items': items}