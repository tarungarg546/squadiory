#couldn't test it
from django.test import Client

c = Client()
response = c.post('/upvote/',{'user_id':'prakhar_96','question_id':'1'})
self.assertEqual(response.status_code, 200)

response = c.post('/downvote',{'user_id':'prakhar_96','question_id':'1',})
self.assertEqual(response.status_code,200)

response = c.post('/satisfied/',{'user_id':'prakhar_96','question_id':'1'})
self.assertEqual(response.status_code, 200)

response = c.post('/disatisfied/',{'user_id':'prakhar_96','question_id':'1',})
self.assertEqual(response.status_code,200)

