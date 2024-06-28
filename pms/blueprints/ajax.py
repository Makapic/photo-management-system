# -*- coding: utf-8 -*-
from flask import render_template, jsonify, Blueprint
from flask_login import current_user

from pms.models import User, Photo

ajax_bp = Blueprint('ajax', __name__)


@ajax_bp.route('/profile/<int:user_id>')
def get_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('main/profile_popup.html', user=user)


@ajax_bp.route('/collect/<int:photo_id>', methods=['POST'])
def collect(photo_id):
    if not current_user.is_authenticated:
        return jsonify(message='需要登录.'), 403
    if not current_user.confirmed:
        return jsonify(message='需要确认账号.'), 400
    if not current_user.can('COLLECT'):
        return jsonify(message='无权限.'), 403

    photo = Photo.query.get_or_404(photo_id)
    if current_user.is_collecting(photo):
        return jsonify(message='已收藏.'), 400

    current_user.collect(photo)
    return jsonify(message='照片已收藏.')


@ajax_bp.route('/uncollect/<int:photo_id>', methods=['POST'])
def uncollect(photo_id):
    if not current_user.is_authenticated:
        return jsonify(message='需要登录.'), 403

    photo = Photo.query.get_or_404(photo_id)
    if not current_user.is_collecting(photo):
        return jsonify(message='尚未收藏.'), 400

    current_user.uncollect(photo)
    return jsonify(message='已取消收藏.')
