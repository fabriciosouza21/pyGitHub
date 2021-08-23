from Remove_trash import Remove_trash
import re

f = " fabricio '''metric.prefix=dev metric.kafka.report_period_ms=60000 metric.kafka.clusters.0.groupstopics.0.group_id=test1 metric.kafka.clusters.0.groupstopics.0.topics=test_topic1,test_topic2 metric.kafka.clusters.0.groupstopics.1.group_id=test2metric.kafka.clusters.0.groupstopics.1.topics=test_topic3,test_topic4metric.kafka.clusters.0.groupstopics.2.group_id=test3metric.kafka.clusters.0.groupstopics.2.topics=test_topic5,test_topic6'''"



class Remove_three_quotes(Remove_trash):
    @classmethod
    def clean(text):
        return re.sub(r'\'''[^)]*\'''', '',text)

