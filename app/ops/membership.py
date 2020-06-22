# -*- coding: utf-8 -*-
# time: 2020/6/18 下午4:43
from app.models.eggs import MembershipCard


def get_membership_list():
    MembershipCard.query.filter_by(open_id=open_id).all()