from crosstex.objects import *

# Prefer long names.
string._addproducer(makegetterproducer('shortname'), 'value')
string._addproducer(makegetterproducer('longname'), 'value')

# Standard producers for top-level objects.
misc._addproducer(bibtexproducer, 'value')
location._addproducer(citystatecountryproducer, 'value')
entrylist._addlistformatter(andlistformatter, 'value')

# Use empty labels (irrelevant, but labels determine what is 'citeable' and thus produced.
misc._addproducer(emptyproducer, 'label')

# Preface conference tracks and workshops with the name of the conference.
conferencetrack._addfilter(conferencetrackfilter, 'value')

# Specialized publication information.
misc._addproducer(makegetterproducer('howpublished'), 'publication')
url._addproducer(accessedproducer, 'publication')
thesis._addproducer(thesistypeproducer, 'publication')

# Specialized type information.
patent._addproducer('United States Patent', 'numbertype')
techreport._addproducer('Technical Report', 'numbertype')
rfc._addproducer('IETF Request for Comments', 'numbertype')
mastersthesis._addproducer("Master's", 'thesistype')
phdthesis._addfilter('Ph.D.', 'thesistype')