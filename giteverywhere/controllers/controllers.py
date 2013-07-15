from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound



from ..models import (
    DBSession,
    Repository,
    )

from ..forms import ContactForm
from pyck.controllers import CRUDController



@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    one = None
    return {'one': one, 'project': 'giteverywhere'}
        
    
#@view_config(route_name='add_repo_names', renderer='add_repo_names.mako')
#def say_add(request):
#  varrr=request.POST['addd'];
#  varrr=str(varrr);
  
#  model2=RepoName(repo_name=varrr);
#  DBSession.add(model2);
  
#  accc2 = DBSession.query(RepoName).all()
#  return {'accc2':accc2}
  
@view_config(route_name='view_repo_names', renderer='view_repo_names.mako')
def view_rnames(request):
  
  view = DBSession.query(Repository).all()
  return {'view':view}
 
#@view_config(route_name='delete_product')
#def delete_product(request):
    
#    id = int(request.matchdict['repo_id'])
#    R = DBSession.query(RepoName).filter_by(repo_id=id).first()
    
#    if R:
#        DBSession.delete(R)
    
#    return HTTPFound(location=request.route_url('view_repo_names'))

#@view_config(route_name='display', renderer='display.mako')
#def say_display(request):
# return {}

@view_config(route_name='contact', renderer="contact.mako")
def contact_form(request):

    f = ContactForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'contact_form': f}



    
    

