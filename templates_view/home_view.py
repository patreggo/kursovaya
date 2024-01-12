from templates_view.base_view import View
from render_template import render_template
from db.connect import get_products_from_db, generate_product_cards

class HomeView(View):
    template = 'templates/index.html'
    
    def get(self, environ):
        products = get_products_from_db()
        product_cards_html = generate_product_cards(products)
        return render_template(template_name=self.template, context={'product_cards': product_cards_html})