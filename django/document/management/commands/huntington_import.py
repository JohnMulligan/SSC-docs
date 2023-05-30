import csv
import re
from pyzotero import zotero
from django.core.management.base import BaseCommand, CommandError
from document.models import *
from past.models import *
from voyage.models import *
from SSC.settings import *
import requests
import json
import os

class Command(BaseCommand):
	help = 'imports michigan collections -- purpose-built'
	def handle(self, *args, **options):
		basepath="document/management/commands/"
		tsvs=[i for i in os.listdir(basepath) if "mssST" in i]
		
		library_id=zotero_credentials['library_id']
		library_type=zotero_credentials['library_type']
		api_key=zotero_credentials['api_key']
		zot = zotero.Zotero(library_id, library_type, api_key)
		
		template={
			'itemType': 'Manuscript',
			'title': '',
			'creators': [
				{
					'creatorType': 'author',
					'firstName': '',
					'lastName': ''
				}
			],
			'abstractNote': '',
			'series': '',
			'seriesNumber': '',
			'volume': '',
			'numberOfVolumes': '',
			'edition': '',
			'place': '',
			'publisher': '',
			'date': '',
			'numPages': '',
			'language': '',
			'ISBN': '',
			'shortTitle': '',
			'url': '',
			'accessDate': '',
			'archive': '',
			'archiveLocation': '',
			'libraryCatalog': '',
			'callNumber': '',
			'rights': '',
			'extra': '',
			'tags': [],
			'collections': [],
			'relations': {}
		}
		for tsv in tsvs:
			fpath=os.path.join(basepath,tsv)
			print(fpath)
			with open(fpath,'r') as tsvfile:
				reader=csv.DictReader(tsvfile,delimiter='\t')
# 				frontmatter=True
# 				firstrow=True
				doc_title=None
				for row in reader:
					
					call_no=row["Call Number"]
					physical_collection=row["Physical Collection"]
					rights=row["Rights"]
					digital_collection=row["Digital Collection"]
					object_file_name=row["Object File Name"]
					iiif_manifest_url=row["IIIF Page Manifest Link"]
					iiif_page_url=row["IIIF Page Image Manifest Link"]
					part_of_object=row["Part of Object"]
					reference_url=row["Reference URL"]
					
					collection_number=re.search("(?<=mssST)\s+[0-9]+",call_no).group(0).strip()
					collection_volume=re.search("(?<=v\.)\s+[0-9]+",call_no).group(0).strip()
					
					if row["Description"]!="":
						doc_title=row["Description"]
						doc_date=row["Date"]
					
					full_ref=" ".join(
						[
							"SSC",
							physical_collection,
							part_of_object,
							"Huntington Library"
						]
					)
					
					short_ref=" ".join(
						[
							"SSC",
							"Stowe",
							collection_number,
							collection_volume,
							"(Huntington)"
						]
					)
					
					template["callNumber"]=call_no
					template["title"]=doc_title
					template["libraryCatalog"]=digital_collection
					template["rights"]=rights
					template["archive"]=physical_collection
					template["archiveLocation"]=part_of_object
					template["shortTitle"]=short_ref
					template["url"]=reference_url
					template["date"]=doc_date
					
					
					legacy_source,lc_isnew=LegacySource.objects.get_or_create(
						full_ref=full_ref,
						short_ref=short_ref
					)
					
					django_zotero_object,django_zotero_object_isnew=ZoteroSource.objects.get_or_create(
						legacy_source=legacy_source,
						zotero_title=doc_title,
						zotero_date=doc_date
					)
					
					if django_zotero_object_isnew:
						resp = zot.create_items([template])
						zotero_url=resp['successful']['0']['links']['self']['href']
						django_zotero_object.zotero_url=zotero_url
							

					sp,sp_isnew=SourcePage.objects.get_or_create(
						item_url=iiif_manifest_url,
						iiif_baseimage_url=iiif_page_url
					)
					print(sp,django_zotero_object)
# 					print(sp.id,sp)
# 					print(django_zotero_object.id,django_zotero_object)
					spc,spc_isnew=SourcePageConnection.objects.get_or_create(
						zotero_source=django_zotero_object,
						source_page=sp
					)