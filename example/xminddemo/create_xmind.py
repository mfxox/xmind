# -*- coding: utf-8 -*-
import xmind
from xmind.core.const import TOPIC_DETACHED
from xmind.core.markerref import MarkerId
from xmind.core.topic import TopicElement

# load an existing file or create a new workbook if nothing is found
workbook_document = xmind.load("test.xmind")


# ***** sheet1 *****
# get the first sheet(a new workbook has a blank sheet by default)
sheet1 = workbook_document.getPrimarySheet()
sheet1.setTitle("first sheet")  # set its title

# get the root topic of this sheet(a sheet has  a blank root topic by default)
root_topic1 = sheet1.getRootTopic()
root_topic1.setTitle("root node")  # set its title

# create some sub topic element
sub_topic1 = root_topic1.addSubTopic()
sub_topic1.setTitle("first sub topic")

sub_topic2 = root_topic1.addSubTopic()
sub_topic2.setTitle("second sub topic")

sub_topic3 = root_topic1.addSubTopic()
sub_topic3.setTitle("third sub topic")

sub_topic4 = root_topic1.addSubTopic()
sub_topic4.setTitle("fourth sub topic")

# create a detached topic(attention: only root topic can add a detached topic)
detached_topic1 = root_topic1.addSubTopic(topics_type=TOPIC_DETACHED)
detached_topic1.setTitle("detached topic")
detached_topic1.setPosition(0, 30)

sub_topic1_1 = sub_topic1.addSubTopic()
sub_topic1_1.setTitle("I'm a sub topic too")
sub_topic1_1.setLabel("I'm a label")
sub_topic1_1.addMarker(MarkerId.starBlue)
sub_topic1_1.addMarker(MarkerId.flagGreen)  # can add different marker


# ***** sheet2 *****
# create a new sheet and add to the workbook by default
sheet2 = workbook_document.createSheet()
sheet2.setTitle("second sheet")

# a sheet has a blank sheet by default
root_topic2 = sheet2.getRootTopic()
root_topic2.setTitle("root node")

# use other methods to create some sub topic element
topic1 = TopicElement(ownerWorkbook=workbook_document)
# set a topic hyperlink from this topic to the first sheet given by s1.getID()
topic1.setTopicHyperlink(sheet1.getID())
topic1.setTitle("redirection to the first sheet")  # set its title

topic2 = TopicElement(ownerWorkbook=workbook_document)
topic2.setTitle("second node")
topic2.setURLHyperlink("https://xmind.net")  # set an url hyperlink

topic3 = TopicElement(ownerWorkbook=workbook_document)
topic3.setTitle("third node")
topic3.setPlainNotes("notes for this topic")  # set notes (F4 in XMind)
topic3.setTitle("topic with \n notes")

topic4 = TopicElement(ownerWorkbook=workbook_document)
topic4.setFileHyperlink("logo.jpeg")  # set a file hyperlink
topic4.setTitle("topic with a file")

topic1_1 = TopicElement(ownerWorkbook=workbook_document)
topic1_1.setTitle("sub topic")
topic1_1.setLabel("a label")

# then the topics must be added to the root element
root_topic2.addSubTopic(topic1)
root_topic2.addSubTopic(topic2)
root_topic2.addSubTopic(topic3)
root_topic2.addSubTopic(topic4)
topic1.addSubTopic(topic1_1)

# to loop on the subTopics
topics = root_topic2.getSubTopics()
for index, topic in enumerate(topics):
    topic.addMarker("priority-" + str(index + 1))

# create a relationship
sheet2.createRelationship(topic1.getID(), topic2.getID(), "test")


# and we save
xmind.save(workbook_document)
