from odoo import http

class Formation(http.Controller):
    @http.route('/fstep', type='http', auth='public', website=True)
    def render_web_page(self):
        return http.request.render('First_step.Step1', {})