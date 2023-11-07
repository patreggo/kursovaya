from templates_view.base_view import View
from render_template import render_template

class ContactUs2View(View):
    template = 'templates/2.html'
    content_type = 'text/html; charset=UTF-8'
    
    def get(self, environ):
        
        return render_template(template_name=self.template, context={})
