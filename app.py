from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__, template_folder = "templates")

info = {
    'about':
    {
        'introduction': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'profession':'UI/UX Designer & Web Developer.',
        'first_description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'second_description':'Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis.Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.',
        'birthday':'1 May 1995',
        'website': 'www.example.com',
        'phone_number': '+123 456 7890',
        'city': 'New York, USA',
        'age': '30',
        'degree': 'Master',
        'email': 'email@example.com',
        'freelance': 'Available'
    },
    'facts':
    {
        'introduction':'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'items': 
        [
            {
                'icon':'bi-emoji-smile',
                'fact_name':'Happy Clients',
                'clarification':'consequuntur quae',
                'number':'232'
            },
            {
                'icon':'bi-journal-richtext',
                'fact_name':'Projects',
                'clarification':'adipisci atque cum quia aut',
                'number':'521'
            },
            {
                'icon':'bi-headset',
                'fact_name':'Hours Of Support',
                'clarification':'aut commodi quaerat',
                'number':'1453'
            },
            {
                'icon':'bi-people',
                'fact_name':'Hard Workers',
                'clarification':'rerum asperiores dolor',
                'number':'32'
            }
        ]
    },
    'skills':
    {
    'introduction':'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
    'items_column_left':
        [
            {'name':'HTML', 'value':'100'},
            {'name':'CSS', 'value':'90'},
            {'name':'JavaScript', 'value':'75'}
        ],
    'items_column_right':
        [
            {'name':'PHP', 'value':'80'},
            {'name':'WordPress/CMS', 'value':'90'},
            {'name':'Photoshop', 'value':'55'}
        ]
    },
    'resume':
    {
        'introduction':'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'Sumary':
        {
            'title':'Sumary',
            'items':
            [
                {
                'title':'Alex Smith',
                'from': '',
                'to': '',
                'detail':'Innovative and deadline-driven Graphic Designer with 3+ years of experience designing and developing user-centered digital/print marketing material from initial concept to final, polished deliverable.',
                'description':'',
                'sub_items':
                [
                    'Portland par 127,Orlando, FL',
                    '(123) 456-7891',
                    'alice.barkley@example.com'
                ]
                }
            ]
        },
        'Education':
        {
            'title':'Education',
            'items':
            [
                {
                'title':'Master of Fine Arts & Graphic Design',
                'from': '2015',
                'to': '2016',
                'detail':'Rochester Institute of Technology, Rochester, NY',
                'description':'Qui deserunt veniam. Et sed aliquam labore tempore sed quisquam iusto autem sit. Ea vero voluptatum qui ut dignissimos deleniti nerada porti sand markend',
                'sub_items':[]
                },
                {
                'title':'Bachelor of Fine Arts & Graphic Design',
                'from': '2010',
                'to': '2014',
                'detail':'Rochester Institute of Technology, Rochester, NY',
                'description':'Quia nobis sequi est occaecati aut. Repudiandae et iusto quae reiciendis et quis Eius vel ratione eius unde vitae rerum voluptates asperiores voluptatem Earum molestiae consequatur neque etlon sader mart dila',
                'sub_items':[]
                }
            ]
        },
        'Profesional Experience':
        {
            'title':'Professional Experience',
            'items':
            [
                {
                'title':'Senior graphic design specialist',
                'from': '2019',
                'to': 'Present',
                'detail':'Experion, New York, NY',
                'description':'',
                'sub_items':
                [
                    'Lead in the design, development, and implementation of the graphic, layout, and production communication materials',
                    'Delegate tasks to the 7 members of the design team and provide counsel on all aspects of the project.',
                    'Supervise the assessment of all graphic materials in order to ensure quality and accuracy of the design',
                    'Oversee the efficient use of production project budgets ranging from $2,000 - $25,000'
                ]
                },
                {
                'title':'Graphic design specialist',
                'from': '2017',
                'to': '2018',
                'detail':'Stepping Stone Advertising, New York, NY',
                'description':'',
                'sub_items':
                    [
                        'Developed numerous marketing programs (logos, brochures,infographics, presentations, and advertisements).',
                        'Managed up to 5 projects or tasks at a given time while under pressure',
                        'Recommended and consulted with clients on the most appropriate graphic design',
                        'Created 4+ design presentations and proposals a month for clients and account managers'
                    ]
                }
            ]
        }
    },
    'portfolio':
    {
        'introduction':'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'items':[
            {
                'is_web': False,
                'is_app': True,
                'is_card': False,
                'image_path':'../static/img/portfolio/portfolio-1.jpg',
                'title': 'App 1'
            },
            {
                'is_web': True,
                'is_app': False,
                'is_card': False,
                'image_path': '../static/img/portfolio/portfolio-2.jpg',
                'title': 'Web 3',
            },
            {
                'is_web': False,
                'is_app': True,
                'is_card': False,
                'image_path': '../static/img/portfolio/portfolio-3.jpg',
                'title': 'App 2',
            },
            {
                'is_web': False,
                'is_app': False,
                'is_card': True,
                'image_path': '../static/img/portfolio/portfolio-4.jpg',
                'title': 'Card 2',
            },
            {
                'is_web': True,
                'is_app': False,
                'is_card': False,
                'image_path': '../static/img/portfolio/portfolio-5.jpg',
                'title': 'Web 2',
            },
            {
                'is_web': False,
                'is_app': True,
                'is_card': False,
                'image_path': '../static/img/portfolio/portfolio-6.jpg',
                'title': 'App 3',
            },
            {
                'is_web': False,
                'is_app': False,
                'is_card': True,
                'image_path': '../static/img/portfolio/portfolio-7.jpg',
                'title': 'Card 1',
            },
            {
                'is_web': False,
                'is_app': False,
                'is_card': True,
                'image_path': '../static/img/portfolio/portfolio-8.jpg',
                'title': 'Card 3',
            },
            {
                'is_web': True,
                'is_app': False,
                'is_card': False,
                'image_path': '../static/img/portfolio/portfolio-9.jpg',
                'title': 'Web 3',
            }
        ]
    },
    'services':
    {
        'introduction':'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'items':[
            {
                'icon':'bi-briefcase',
                'title': 'Lorem Ipsum',
                'description': 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident'
            },
            {
                'icon':'bi-card-checklist',
                'title': 'Dolor Sitema',
                'description': 'Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata'
            },
            {
                'icon':'bi-bar-chart',
                'title': 'Sed ut perspiciatis',
                'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur'
            },
            {
                'icon':'bi-binoculars',
                'title': 'Magni Dolores',
                'description': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
            },
            {
                'icon':'bi-brightness-high',
                'title': 'Nemo Enim',
                'description': 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque'
            },
            {
                'icon':'bi-calendar4-week',
                'title': 'Eiusmod Tempor',
                'description': 'Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi'
            }
        ]
    },
    'testimonials':
    {
        'introduction': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'items':[
            {
                'testimony': 'Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.',
                'profile_picture_path': '../static/img/testimonials/testimonials-1.jpg',
                'full_name': 'Saul Goodman',
                'reference': 'Ceo & Founder'
            },
            {
                'testimony': 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.',
                'profile_picture_path': '../static/img/testimonials/testimonials-2.jpg',
                'full_name': 'Sara Wilsson',
                'reference': 'Designer'
            },
            {
                'testimony': 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.',
                'profile_picture_path': '../static/img/testimonials/testimonials-3.jpg',
                'full_name': 'Jena Karlis',
                'reference': 'Store Owner'
            },
            {
                'testimony': 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.',
                'profile_picture_path': '../static/img/testimonials/testimonials-4.jpg',
                'full_name': 'Matt Brandon',
                'reference': 'Freelancer'
            },
            {
                'testimony': 'Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.',
                'profile_picture_path': '../static/img/testimonials/testimonials-5.jpg',
                'full_name': 'John Larson',
                'reference': 'Entrepreneur'
            }
        ]
    },
    'contact':
    {
        'introduction':'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'location': 'A108 Adam Street, New York, NY 535022',
        'email': 'info@example.com',
        'phone_number': '+1 5589 55488 55s',
        'google_maps_shareable_link':'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12097.433213460943!2d-74.0062269!3d40.7101282!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xb89d1fe6bc499443!2sDowntown+Conference+Center!5e0!3m2!1smk!2sbg!4v1539943755621'
    }
}

@app.route("/")
def index():
    return render_template("index.html", info = info)


if __name__ == "__main__":

    app.run(debug = True)