PDX Council Minutes Data
==============

Attempting to extract and clean up the PDX Council Minutes data and make it searchable.  Currently the data is formatted in nasty PDFs which makes parsing more complex than desirable.  

The project is also a demonstration for using Luigi process framework to run ETL jobs of web data.  

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
    * Breaking out Heading information from the PDF-text
        * Contains meeting information but mostly unhelpful text and characters
    * Analyzing meeting minute data
        * Break apart statements by participant
            * eg: "Adams: I'm a pretty sweet mayor" "Fritz: I concur" "GAVEL"
            * When indexing in ES, set participant and statement as fields
    * Stopword Blacklisting(Degrades context, bad and will be removed)
        * Requires NLTK download of 'all-corpora'
        * In text list, keep indexes to all words including stopped for backtracing location of words to raw document.
    * Stemming for language analysis?

###Loading/Save
 * Index data to Elasticsearch 
    * Have alternative for simple filesystem storage
 * Statement Data Fields (made searchable via ES)
    * Speaker
    * Statement
    * Date
    * Statement position in document

####Visualization
 * TODO: Write data to a graph/rdf data store for quick analysis loading to D3
 * Index data into Elasticsearch
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
TODO: Dockerize visualization server
TODO: Kickoff end task  

