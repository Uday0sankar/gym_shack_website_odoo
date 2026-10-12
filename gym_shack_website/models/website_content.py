from odoo import api, fields, models


class GymShackConfig(models.Model):
    _name = 'gym.shack.config'
    _description = 'Gym Shack Website Configuration'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, default='Default')
    website_id = fields.Many2one('website', string='Website', default=lambda self: self.env['website'].get_current_website())
    company_name = fields.Char(string='Company Name', default='Gym Shack Fitness')
    brand_tagline = fields.Char(string='Brand Tagline', default='Built different. Trained different.')
    hero_eyebrow = fields.Char(string='Hero Eyebrow', default='WELCOME TO GYM SHACK')
    hero_title = fields.Char(string='Hero Title', default='BUILT.')
    hero_title_alt = fields.Char(string='Hero Title Highlight', default='NOT BORN.')
    hero_subtitle = fields.Char(string='Hero Subtitle', default='Elite International Machines & Expert Trainers')
    hero_primary_text = fields.Char(string='Primary CTA', default='START YOUR JOURNEY')
    hero_secondary_text = fields.Char(string='Secondary CTA', default='EXPLORE PROGRAMS')
    hero_primary_url = fields.Char(string='Primary URL', default='/gym-shack')
    hero_secondary_url = fields.Char(string='Secondary URL', default='#programs')
    contact_phone = fields.Char(string='Phone', default='91885 26266')
    contact_email = fields.Char(string='Email', default='gymshack.club@gmail.com')
    address_line_1 = fields.Char(string='Address 1', default='Hat Complex, 2nd Floor')
    address_line_2 = fields.Char(string='Address 2', default='Near Federal Bank, Meloor')
    address_line_3 = fields.Char(string='Address 3', default='Chalakudy, Kerala 680311')
    morning_open = fields.Char(string='Morning Open', default='5:30 AM')
    morning_close = fields.Char(string='Morning Close', default='10:00 AM')
    evening_open = fields.Char(string='Evening Open', default='4:30 PM')
    evening_close = fields.Char(string='Evening Close', default='10:00 PM')
    social_facebook = fields.Char(string='Facebook URL', default='#')
    social_instagram = fields.Char(string='Instagram URL', default='#')
    social_youtube = fields.Char(string='YouTube URL', default='#')
    social_whatsapp = fields.Char(string='WhatsApp URL', default='#')
    active = fields.Boolean(default=True)


class GymShackProgram(models.Model):
    _name = 'gym.shack.program'
    _description = 'Gym Shack Program'
    _order = 'sequence, id'

    name = fields.Char(string='Program Name', required=True)
    subtitle = fields.Char(string='Subtitle')
    description = fields.Char(string='Short Description')
    long_description = fields.Text(string='Long Description')
    benefits = fields.Text(string='Benefits')
    image_url = fields.Char(string='Image URL', default='https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=900&q=80')
    icon_name = fields.Char(string='Icon Name', default='Dumbbell')
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    config_id = fields.Many2one('gym.shack.config', string='Configuration')


class GymShackFeature(models.Model):
    _name = 'gym.shack.feature'
    _description = 'Gym Shack Feature'
    _order = 'sequence, id'

    name = fields.Char(string='Feature Name', required=True)
    description = fields.Char(string='Description')
    image_url = fields.Char(string='Image URL', default='https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&w=900&q=80')
    icon_name = fields.Char(string='Icon Name', default='Dumbbell')
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    config_id = fields.Many2one('gym.shack.config', string='Configuration')


class GymShackPlan(models.Model):
    _name = 'gym.shack.plan'
    _description = 'Gym Shack Membership Plan'
    _order = 'sequence, id'

    name = fields.Char(string='Plan Name', required=True)
    plan_type = fields.Selection([
        ('gym_membership', 'Gym Membership'),
        ('registration', 'Registration Plan'),
        ('walk_in', 'Walk-in Pass'),
    ], string='Plan Type', default='gym_membership', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', default=0.0)
    original_price = fields.Float(string='Original Price', default=0.0)
    badge = fields.Char(string='Badge')
    featured = fields.Boolean(string='Featured', default=False)
    call_to_action = fields.Char(string='CTA Label', default='CHOOSE PLAN')
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    config_id = fields.Many2one('gym.shack.config', string='Configuration')


class GymShackContactMessage(models.Model):
    _name = 'gym.shack.contact.message'
    _description = 'Gym Shack Contact Message'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    subject = fields.Char(string='Subject')
    message = fields.Text(string='Message', required=True)
    create_date = fields.Datetime(string='Created On', readonly=True)

    @api.model
    def submit_message(self, vals):
        if not vals.get('name') or not vals.get('email') or not vals.get('message'):
            raise ValueError('Name, email and message are required.')
        return self.create(vals)

