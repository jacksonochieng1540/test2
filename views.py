from.models import home
from resf_framework.decorators import @api_views
def home(request):
    return render(request,home.html)