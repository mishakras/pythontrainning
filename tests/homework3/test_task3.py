from homework.homework3 import task3

sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]

sample_data_2 = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "andy"
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "name": "polly"
     },
     {
         "is_dead": True,
         "kind": "calibre",
         "type": "bird",
     },
]


def test_positive_case_simple():
    assert task3.make_filter(name='polly', type='bird')\
               .apply(sample_data) == [{
                "is_dead": True,
                "kind": "parrot",
                "type": "bird",
                "name": "polly"
                }]


def test_positive_case_complex():
    assert task3.make_filter(name='polly', type='bird')\
               .apply(sample_data_2) == [{
                "is_dead": True,
                "kind": "parrot",
                "type": "bird",
                "name": "polly"
                }]