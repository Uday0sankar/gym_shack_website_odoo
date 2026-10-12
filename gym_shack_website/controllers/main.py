import json

from odoo import http
from odoo.http import request


class GymShackWebsiteController(http.Controller):

    @http.route(['/gym-shack', '/gym-shack/'], type='http', auth='public', website=True, csrf=False)
    def gym_shack_home(self, **post):
        config = request.env['gym.shack.config'].sudo().search([], limit=1)
        if not config:
            config = request.env['gym.shack.config'].sudo().create({
                'name': 'Default',
            })
        programs = request.env['gym.shack.program'].sudo().search([
            ('active', '=', True),
        ], order='sequence asc, id asc')
        features = request.env['gym.shack.feature'].sudo().search([
            ('active', '=', True),
        ], order='sequence asc, id asc')
        plans = request.env['gym.shack.plan'].sudo().search([
            ('active', '=', True),
        ], order='sequence asc, id asc')
        values = {
            'config': config,
            'programs': programs,
            'features': features,
            'plans': plans,
            'submitted': 'submitted' in post and post.get('submitted') == '1',
        }
        return request.render('gym_shack_website.homepage_template', values)

    @http.route(['/gym-shack/contact'], type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def gym_shack_contact(self, **post):
        name = (post.get('name') or '').strip()
        email = (post.get('email') or '').strip()
        phone = (post.get('phone') or '').strip()
        subject = (post.get('subject') or '').strip() or 'Website inquiry'
        message = (post.get('message') or '').strip()

        if not name or not email or not message:
            return request.redirect('/gym-shack?error=1')

        lead = request.env['crm.lead'].sudo().create({
            'name': name,
            'email_from': email,
            'phone': phone,
            'subject': subject,
            'description': message,
            'partner_name': name,
            'type': 'lead',
        })
        if lead:
            lead.message_post(body=f"Website contact form submission.<br/>Email: {email}<br/>Phone: {phone}")

        return request.redirect('/gym-shack?submitted=1')
