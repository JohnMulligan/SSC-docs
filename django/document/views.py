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
		
# 		for zs in this_page:
# 			for spc in zs.page_connection.all():
# 				print(spc.source_page.iiif_baseimage_url)
		
		return render(request, "gallery.html", {"page_obj": this_page})
	else:
		return HttpResponseForbidden("Forbidden")
		

#######################
# then the individual page view
def z_source_page(request,zotero_source_id=1):
	
	if request.user.is_authenticated:
		print(zotero_source_id)
		doc=ZoteroSource.objects.get(id=zotero_source_id)
		print(doc)
		return render(request, "single_doc.html", {'zs':doc})
	else:
		return HttpResponseForbidden("Forbidden")