import homework3.task3 as task3

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
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "andy"
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


def test_bug1():
    assert task3.make_filter(name='polly', type='bird')\
               .apply(sample_data) == []


def test_bug2():
    assert task3.make_filter_fix1(name='polly', type='bird')\
               .apply(sample_data_2) == []


def test_bug3():
    assert task3.make_filter_fix2(name='polly', type='bird')\
               .apply(sample_data_2) == [{
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
                     "kind": "calibre",
                     "type": "bird",
                 }]


def test_bug4():
    assert task3.make_filter_fix3(name='polly', type='bird')\
               .apply(sample_data_2) == [{
                "is_dead": True,
                "kind": "parrot",
                "type": "bird",
                "name": "polly"
                }]
