PDX Council Minutes Data
==============

Attempting to extract and clean up the PDX Council Minutes data and make it searchable.  Currently the data is formatted in nasty PDFs which makes parsing more complex than desirable.
Demonstration project for using Luigi process framework to run ETL jobs.

##Overview
###Extract
Using requests, pull web assets and parse the html data for subject data. 
[Multnoma Board Records](http://multnomah.granicus.com/ViewPublisher.php?view_id=3)  
[Portland Council Records](http://www.portlandonline.com/auditor/index.cfm?c=56676)  
Pull up page of Portland Council meeting page, index the links each respective year's meeting list.
 * Construct list of available Minutes documents
 * Pull all Minute documents not previously processed
    * Each Minutes doc is it's own directory/Task which is delimited by a UID

###Transform
Sanitize example, clean/process/stem/nlp extracted data to record.  
 * Each Minutes file is a pdf which needs to be parsed to extract headers and content data.
    * Use PyPDF2 to extract text.
    * Decide if more than just text conversion is necessary.
 * Clean data
    * Stopword Blacklisting
        * Requires NLTK download of 'all-corpora'
        * In text list, keep indexes to all words including stopped for backtracing location of words to raw document.
    * Stemming for language analysis?

###Loading/Save
 * Index data to Elasticsearch 
    * Have alternative for simple filesystem storage
 * TODO: Write data to a graph/rdf data store for quick anlysis loading to D3
 * Feed interesting data to D3.

###Analysis
####Possibilities 
 * Group content of text analysis by speaker's name
     * Speaker->speech might be possible by splitting: 
     \w<SpeakerName>: <sentence> <words> <...>.  
 * Word content cloud

##Setup
> pip install -r requirements.txt

TODO: Luigi config file  
TODO: luigid daemon  
TODO: Elasticsearch from docker image  
TODO: Learn D3 for setup :/  

##Running

TODO: Running scheduler  
TODO: Running Elasticsearch docker image  
TODO: Kickoff end task  

