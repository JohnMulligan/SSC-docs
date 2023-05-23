from django.http import Http404, HttpResponse, HttpResponseForbidden, JsonResponse
from django.template import loader
from django.shortcuts import redirect,render
from django.core.paginator import Paginator
from document.models import *
import re

#######################
# default view will be a paginated gallery
def index(request,pagenumber=1):
	
	if request.user.is_authenticated:
		
		docs=ZoteroSource.objects.all()
		docs_paginator=Paginator(docs, 12)
		this_page=docs_paginator.get_page(pagenumber)
		
		for zs in this_page:
			for spc in zs.page_connection.all():
				print(spc.source_page.iiif_baseimage_url)
		
		print(this_page[0])
		
		return render(request, "gallery.html", {"page_obj": this_page})
# 		return HttpResponse("hola")
	else:
		return HttpResponseForbidden("Forbidden")
		
		
		
		
# 		
# 		
# 		#Update the user's db data from ldap if they're authenticated by sso
# 		thisUser=ldap_update_rcams_users([request.user])[0]
# 		#and then pull the user's data from the updated db record
# 		thisUserDict=getuserdict(thisUser)
# 		context={
# 			'auth_user':thisUserDict,
# 			'machines':get_machines_dict()
# 		}
# 		# right now, i'm immediately "activating" authenticated users within rcams, so this has no effect here.
# 		# but we might want to change that down the line.
# 		if thisUser.user.is_active:
# # 			print(thisUser.__dict__)
# 			# when the user's entry is first created in the RCAMS db, they have a rice designation from ldap:
# 			## e.g., "graduate student" "senior student" "staff" "faculty"
# 			# these need to be half-mapped/half-routed to our RCAMS designations:
# 			## "Sponsor" "Sponsee"
# 			## which are stored
# 			
# 			if thisUser.user_type is not None:
# 				if thisUser.user_type=="Sponsor":
# 					print(context)
# 					return render(request,'sponsoring_user_homepage.html',context=context)
# 				elif thisUser.user_type=="Sponsee":
# 					sponsorship=thisUser.sponsors.first()
# 					if sponsorship is None:
# 						allsponsors=getallsponsors()
# 						context['allsponsors']=allsponsors
# 					else:
# 						sponsor=getuserdict(sponsorship.sponsor)
# 						status=sponsorship.status
# 						context['sponsorship']={'sponsor':sponsor,'status':status}
# # 					print(context)
# 					return render(request,'sponsored_user_homepage.html',context=context)
# 				else:
# 					return HttpResponse("You have an active rcams account but are registered neither as a sponsor or as sponsored. This shouldn't happen.")
# 				
# 			else:
# 				# a user with no RCAMS type (sponsor, class, or sponsee) has to register
# 				# this page's template points them to the apply_for_usertype endpoint
# 				# staff & students will be given the option of becoming sponsees
# 				# faculty will be given the option of becoming sponsors
# 				context={'auth_user':thisUserDict}
# 				return render(request,'apply_for_usertype.html',context=context)
# 		else:
# 			return HttpResponse("You have a valid netid but your account internal to this system is inactive (this shouldn't happen)")
# 	#And if not, redirect them to SSO
# 	else:
# 		return redirect('accounts/login')





# then we need an individual item page