
Usage


To use Python client for dataquality.pl in a project::

    from dq import DQClient, JobConfig


'<API_TOKEN>')


API token can be obtain on the page "Moje konto".


Account


Check account status::

 dq.account_status()

    print(account.email)          # user email
    print(account.balance)        # account balance
    print(account.total_records)  # processed records


Jobs


List jobs
---------
::

 dq.list_jobs()

    for job in jobs:
        print(job.id)                # job id
        print(job.name)              # human readable job name
        print(job.status)            # job status
        print(job.start_date)        # job start date
        print(job.end_date)          # job end date
        print(job.source_records)    # how many records were applied
        print(job.processed_record)  # how many records were processed
        print(job.price)             # price for processed records


Create new job
--------------
::

 '''"ID","ADRES"
    6876,"34-404, PYZÓWKA, PODHALAŃSKA 100"
    '''

 JobConfig('my job')
True)
'PRZEPISZ')
'DANE_OGOLNE')
1)
True)

input_data)                                         # with data in a variable

'windows-1250')  # with data inside file

    print(job.id)
    print(job.name)
    print(job.status)
    ...

Create new deduplication job
--------------
::

 '''unikalne_id;imie_i_nazwisko;kod_pocztowy;miejscowosc;adres;email;tel;CrmContactNumber;data
	1;Jan Kowalski;37-611;Cieszanów ;Dachnów 189;abc@wp.pl;605936000;abc123;2017-11-08 12:00:00.000
	2;Adam Mickiewicz Longchamps de Berier;66-400;Gorzów Wlkp.;Widok 24;qqq@ft.com;48602567000;a2b2c2;2017-11-08 12:00:00.000
	3;Barbara Łęcka;76-200;Słupsk;Banacha 7;bb@gazeta.pl;79174000;emc2;2017-11-08 12:00:00.000
	4;KAROL NOWAK;22-122;LEŚNIOWICE;RAKOLUPY DU—E 55;kn@ll.pp;0;f112358;2017-11-08 12:00:00.000
	5;Anna Maria Jopek;34-722;Podwilk;Podwilk 464;amj@gmail.com;606394000;eipi10;2017-11-08 12:00:00.000
	6;Mariusz Robert;37-611;Cieszanów ;Dachnów 189;abc@wp.pl;605936000;abc123;2017-11-08 12:00:00.000
	'''

 JobConfig('pr2')
True)
'ID_REKORDU')
'IMIE_I_NAZWISKO')
'KOD_POCZTOWY')
'MIEJSCOWOSC')
'ULICA_NUMER_DOMU_I_MIESZKANIA')
'EMAIL1')
'TELEFON1')
'PRZEPISZ')
'CZAS_AKTUALIZACJI')
True)
True)
True)

input_data)  

	print(job)
	...

Available column functions:

* addresses
    * KOD_POCZTOWY
    * MIEJSCOWOSC
    * ULICA_NUMER_DOMU_I_MIESZKANIA
    * ULICA
    * NUMER_DOMU
    * NUMER_MIESZKANIA
    * NUMER_DOMU_I_MIESZKANIA
    * WOJEWODZTWO
    * POWIAT
    * GMINA
* names
    * IMIE
    * NAZWISKO
    * NAZWA_PODMIOTU
    * IMIE_I_NAZWISKO
* people/companies
    * PESEL
    * NIP
    * REGON
* contact
    * EMAIL1
    * EMAIL2
    * TELEFON1
    * TELEFON2
* dates
    * DATA_URODZENIA
    * CZAS_AKTUALIZACJI
* mixed
    * DANE_OGOLNE
* id
    * ID_REKORDU
* others
    * PRZEPISZ
    * POMIN

Check job state
---------------
::

 dq.job_state('3f14e25e-9f6d-41ff-a4cb-942743a37b73')  # input parameter: job id

    print(state)                                                  # 'WAITING' or 'FINISHED'


Cancel job
----------
::

    dq.cancel_job('3f14e25e-9f6d-41ff-a4cb-942743a37b73')  # input parameter: job id


Retrieve job report
-------------------
::

 dq.job_report('3f14e25e-9f6d-41ff-a4cb-942743a37b73')  # input parameter: job id

    print(report.quantity_issues)
    print(report.quantity_names)
    print(report.results)


Save job results
----------------
::

    dq.job_results('3f14e25e-9f6d-41ff-a4cb-942743a37b73', 'output.csv')


Delete job and its results
--------------------------
::

    dq.delete_job('3f14e25e-9f6d-41ff-a4cb-942743a37b73')  # input parameter: job id
