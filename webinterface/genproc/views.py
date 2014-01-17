# encoding: utf8

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Genproc,
    )

# Максимальное количество возвращаемых записей
LIMIT = 100

@view_config(route_name='id', renderer='json')
def genpoc_by_id(request):

    dbsession = DBSession()

    id = request.matchdict['id']
    row = dbsession.query(Genproc).filter_by(id=id).one()

    result = {
        'id': row.id,
        'name': row.name,
        'orgn': row.orgn,
        'inn': row.inn,
         'addrloc_jur': row.addrloc_jur,
        'addrloc_ip': row.addrloc_ip,
        'addr_act': row.addr_act,
        'addr_obj': row.addr_obj,
        'goal': row.goal,
        'osn_datestart':row.osn_datestart,
        'osn_dateend': row.osn_dateend,
        'osn_datestart2': row.osn_datestart2,
        'osn_other': row.osn_other,
        'check_month': row.check_month,
        'check_days': row.check_days,
        'check_hours': row.check_hours,
        'check_form': row.check_form,
        'check_org': row.check_org
    }

    return result


@view_config(route_name='substr', renderer='json')
def substr(request):

    dbsession = DBSession()

    substr = request.matchdict['substr'].encode('utf-8')
    print substr
    like_str = "%{0}%".format(substr)
    print like_str
    rows = dbsession.query(Genproc).filter(Genproc.name.ilike(like_str)).limit(LIMIT)
    result = []
    for row in rows:
        result.append({'id': row.id, 'name': row.name, 'orgn': row.orgn, 'inn': row.inn})

    return result
