import json
import uuid
from cassandra.cluster import Cluster

def import_data(table_name, json_filename):
    cluster = Cluster()
    session = cluster.connect()
    insert_statement = 'INSERT INTO %s JSON %s' % (table_name, '%s')

    with open(json_filename) as data_file:
        for line in data_file:
            corrected_line = line.strip().replace('\n', '\\n')
            session.execute_async(insert_statement,[corrected_line])
    cluster.shutdown()

def import_data_without_primary_key(table_name, json_filename, name_of_id):
    cluster = Cluster()
    session = cluster.connect()
    insert_statement = 'INSERT INTO %s JSON %s' % (table_name, '%s')

    with open(json_filename) as data_file:
        for line in data_file:
            corrected_line = json.loads(line.strip().replace('\n','\\n'))
            corrected_line[name_of_id] = str(uuid.uuid1())
            corrected_line = json.dumps(corrected_line)
            session.execute_async(insert_statement,[corrected_line])
    cluster.shutdown()


if __name__ == '__main__':
    print "Importing business data..."
    import_data('yelp.businesses', 'yelp_academic_dataset_business.json')
    print "Finished importing business data".

    print "Importing review data..."
    import_data('yelp.reviews','yelp_academic_dataset_review.json')
    print "Finished importing review data."

    print "Importing user data..."
    import_data('yelp.users','yelp_academic_dataset_user.json')
    print "Finished importing user data."

    print "Importing tip data..."
    import_data_without_primary_key('yelp.tips','yelp_academic_dataset_tip.json', 'tip_id')
    print "Finished importing tip data."

    print "Importing checkin data..."
    import_data_without_primary_key('yelp.checkin_info','yelp_academic_dataset_checkin.json', 'checkin_id')
    print "Finished importing checkin data."
