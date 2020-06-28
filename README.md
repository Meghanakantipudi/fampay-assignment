# fampay-assignment
fampay interview assignment

==================================================

API DETAILS WHICH SATISFIES THE BELOW REQUREMENT: 
================================================
Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.


API 1 FORMAT: http://<server_name>:<port>/assignment/insertdata/<search_keyword>

SAMPLE API 1: http://<server_name>:<port>/assignment/insertdata/develop%20a%20django%20project/

SAMPLE O/P:

SUCCESSFULLY INSERTED!

====================================================

REQUIREMENT:
============
A basic search API to search the stored videos using their title and description.


API 2 FORMAT: http://<server_name>:<port>/assignment/searchvideos/<title>/<description>

SAMPLE API 2: http://<server_name>:<port>/assignment/searchvideos/10.%20Creating%20Django%20Project%20|%20Practicle%20|%20Full%20Explanation/In%20this%20video,%20we%20will%20see%20how%20to%20create%20a%20Django%20project%20using%20django-admin%20command%20and%20we%20will%20understand%20the%20project%20structure%20of%20Django.%20Python%20Django%20.../


SAMPLE O/P:

{'Content': [{'Published At': datetime.datetime(2020, 5, 11, 5, 18, 55, tzinfo=), 'Description': 'In this video, we will see how to create a Django project using django-admin command and we will understand the project structure of Django. Python Django ...', 'VideoId': '_xwJnd5m6C8', 'Thumbnails Default Url': 'https://i.ytimg.com/vi/_xwJnd5m6C8/default.jpg', 'Title': '10. Creating Django Project | Practicle | Full Explanation'}], 'Description': 'In this video, we will see how to create a Django project using django-admin command and we will understand the project structure of Django. Python Django ...', 'Title': '10. Creating Django Project | Practicle | Full Explanation'}

=====================================================

REQUIREMNT:
===========
A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

API 3 FORMAT: http://<server_name>:<port>/assignment/getvideos/

SAMPLE API 3: http://<server_name>:<port>/assignment/getvideos/

SAMPLE O/P:

ALL THE CONTENT IN THE YOUTUBE_VIDEOS TABLE in DB

{'Published At': datetime.datetime(2020, 4, 15, 12, 38, 36, tzinfo=), 'Description': u'Step By Step Python Django Project Development By Pankaj Panjwani. https://yctacademy.blogspot.com/p/major.html YCT Academy is the No.1 Software ...', 'VideoId': u'-VRmM3dQVXk', 'Thumbnails Default Url': u'https://i.ytimg.com/vi/-VRmM3dQVXk/default.jpg', 'Title': u'#8 Python Django Project Development | Hospital Management | Hindi'},....

=====================================================

