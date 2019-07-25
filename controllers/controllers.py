# -*- coding: utf-8 -*-
from odoo import http


class ClusterGame(http.Controller):
    @http.route('/cluster_game/cluster_game/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/cluster_game/cluster_game/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('cluster_game.listing', {
            'root': '/cluster_game/cluster_game',
            'objects': http.request.env['cluster_game.cluster_game'].search([]),
        })

    @http.route('/cluster_game/cluster_game/objects/<model("cluster_game.cluster_game"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('cluster_game.object', {
            'object': obj
        })

