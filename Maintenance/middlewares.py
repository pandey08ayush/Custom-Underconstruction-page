from django.shortcuts import render
from Maintenance.models import UnderConstruction
from decouple import config
class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # print('One Time Intializations')

    def __call__(self,request):
        if request.user.is_staff:
            return self.get_response(request)
        
        # BY pass
        uc_key = config("MAINTENANCE_BYPASS_KEY") # isko env file me likenge 
        if 'u' in request.GET and request.GET['u'] == uc_key: # IT Means is should be check it person mentioned key our not
            request.session['bypass_maintenance'] = True # It Means session should be save for user
            request.session.set_expiry(0) # Means it session should be end when we close the browser

        if request.session.get('bypass_maintenance'):
            return self.get_response(request)    # we have to serach /?u=123 after login page
       
       
        try:
            uc = UnderConstruction.objects.first()
            if uc and uc.is_under_construction:
                context={
                    'uc_note':uc.uc_note,
                    'uc_duration':uc.uc_durartion
                }
                return render(request, 'undercons.html',context)
        except:
            return self.get_response(request)
