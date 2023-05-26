# SSC docs

A dockerized Django web application built for the South Seas Company documents grant with SlaveVoyages.org.

This app is where the machine-generated transcriptions of the digitized South Seas Company papers will land, in order to:

* Clean the transcriptions
* Manually & automatically extract named entities from the transcriptions
* Link those named entities to SV records of
	* Voyages
	* People
* Integrate our legacy SV sources with Zotero
* Link those Zotero records to page-level IIIF links wherever possible

This app is currently in a draft state, awaiting feedback from the P.I.'s. We are currently using test data from other sources 

## Installation

Easy!

### 1. Install Docker Desktop

https://www.docker.com/products/docker-desktop/

### 2. Clone this repository

Install git if you don't have it, and in your terminal, do:

	git clone https://github.com/JohnMulligan/SSC-docs/
	cd SSC-docs
	open .

You should now see a folder with the repository files (including this readme) in it

### 3. Build the container

Start up Docker Desktop if it's not already running

Then you should, in the terminal, be able simply to run:

	docker-compose up --build

Then run one more command to get the basic assets in place

	docker exec -i ssc-django bash -c "python3.9 manage.py collectstatic --noinput"

If it fails, you know who to call :)

### 4. Install the db

For ease of use and portability, I've built this version using a sqlite back-end. When it's ready for primetime, we'll probably use postgres or mysql.

So take the db.sqlite3 file sent to you by John Connor, and drop it into the SSC-docs/django folder

You should now be able to

#### 4A. View & edit the existing records

open the admin interface at http://127.0.0.1:8000/admin, logging in with u:voyages p:voyages

#### 4b. View the digitized documents & attached records

http://127.0.0.1:8000/docs/

## Open questions

* How do we want to link enslavers to this data?
* Are we satisfied with the way we're linking enslaved people?
* What metadata are we missing here?
* Do we want transcriptions to attach at the page level, or the document level?
* What about the other entities -- those are being linked at the document level.
* Above all, what changes do we need to fold in to make this work for SSC, not just Texas data?
* Do we fold in JKW's source data?