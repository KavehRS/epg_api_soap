# Epg_API


This Project by KavehRS is licensed under a

<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">Creative Commons 
Attribution Non-Commercial 3.0 License</a>.

Python version
--------------

First things first: This project fully works on Python versions 3.6

Installation Guide:

1- Create virtual environment:

    virtualenv epg-env
    
2- Activate virtual environment:

    source epg-env/bin/activate
    
3- Install requirements:

    pip install -r requirements.txt
    
4- Install spyne:

    easy_install spyne==2.13.14b0
    
6- Apply migrations:

    python manage.py migrate
    
7- Start project on desired port:

    python manage.py runserver
    
Test Service:
1- SOAP Service is available on this address: (Be aware of ending slash)

    http://localhost:8000/api/epg/
    
1- Post this Message for testing get_notes: (Retrieve all notes)

    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope 
       xmlns:ns0="epg.aban"
       xmlns:ns2="aban.views"
       xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
       xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
      <ns1:Body>
        <ns0:get_notes>
        </ns0:get_notes>
      </ns1:Body>
    </SOAP-ENV:Envelope>

2- Post this Message for testing get_note: (Retrieve a single note)

    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope 
       xmlns:ns0="epg.aban"
       xmlns:ns2="aban.views"
       xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
       xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
      <ns1:Body>
        <ns0:get_note>
          <ns0:pk>[your note id]</ns0:pk>
        </ns0:get_note>
      </ns1:Body>
    </SOAP-ENV:Envelope>

1- Post this Message for testing create_note: (Create a single note)

    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope 
       xmlns:ns0="epg.aban"
       xmlns:ns2="aban.views"
       xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
       xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
      <ns1:Body>
        <ns0:create_note>
          <ns0:note>
            <ns2:channel>[your channel]</ns2:channel>
            <ns2:program>[your program]</ns2:program>
            <ns2:start_date>[your start_date]</ns2:start_date>              # date format example: 2014-02-03T00:00:00
            <ns2:duration>[your ]</ns2:duration>
            <ns2:visit>[your visit]</ns2:visit>
            <ns2:month>[your month]</ns2:month>
          </ns0:note>
        </ns0:create_note>
      </ns1:Body>
    </SOAP-ENV:Envelope>